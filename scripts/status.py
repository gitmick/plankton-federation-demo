#!/usr/bin/env python3
"""Render the federated union as STATUS.md — who has done what, across all participants.

Reads the content-addressed union (federation/plankton-data + nekton-data), decodes each signed
record, and reports the facts: every foton (a reproducible result, by output hash + signer +
what it built on) and every nekton claim (a signed statement, by subject + predicate + signer).
The aggregator reruns nothing; it reports what the hashes say.
"""
import base64, json, os, sys, glob, datetime

def envs(regdir, kind):
    out = []
    for path in sorted(glob.glob(os.path.join(regdir, kind, "objects", "sha256", "*.json"))):
        try:
            wrap = json.load(open(path))
        except Exception:
            continue
        env = wrap.get("envelope", wrap)
        try:
            payload = json.loads(base64.b64decode(env["payload"]))
        except Exception:
            continue
        keyid = (env.get("signatures") or [{}])[0].get("keyid", "?")
        out.append((wrap.get("fotonId") or wrap.get("claimId") or "?", payload, keyid))
    return out

def short(h):
    h = (h or "").replace("sha256:", "")
    return h[:12] if h else "?"

def main():
    fed = sys.argv[1] if len(sys.argv) > 1 else "federation"
    partfile = sys.argv[2] if len(sys.argv) > 2 else "participants.json"
    parts = json.load(open(partfile)).get("participants", []) if os.path.exists(partfile) else []

    fotons = envs(fed, "plankton-data")
    claims = envs(fed, "nekton-data")

    p = print
    p("# Federation status\n")
    p(f"_Union of {len(parts)} registered participant(s): "
      + (", ".join(f"`{x['name']}`" for x in parts) if parts else "none yet") + "._\n")
    p(f"**{len(fotons)} fotons** (reproducible results) · **{len(claims)} claims** "
      f"(signed statements) in the union.\n")

    # who signed what — group by keyid
    signers = {}
    for _, _, k in fotons + claims:
        signers.setdefault(k, [0, 0])
    for _, _, k in fotons:
        signers[k][0] += 1
    for _, _, k in claims:
        signers[k][1] += 1
    p("## Signers\n")
    p("| keyid | fotons | claims |")
    p("|---|--:|--:|")
    for k, (nf, nc) in sorted(signers.items()):
        p(f"| `{k}` | {nf} | {nc} |")
    p("")

    # fotons: output, inputs (the build-on edges), signer
    p("## Fotons (reproducible results)\n")
    p("| output | built on (inputs) | kind / cmd | signer |")
    p("|---|---|---|---|")
    produced = {}  # output hash -> foton id
    for fid, pl, k in fotons:
        outs = [short(s.get("digest", {}).get("sha256")) for s in pl.get("subject", [])]
        pred = pl.get("predicate", {})
        ins = [short(i.get("digest", {}).get("sha256")) for i in pred.get("inputs", [])]
        proto = pred.get("protocol", {})
        cmd = (proto.get("descriptor", {}) or {}).get("cmd", proto.get("kind", ""))
        for o in pl.get("subject", []):
            produced[short(o.get("digest", {}).get("sha256"))] = short(fid)
        p(f"| `{', '.join(outs)}` | {', '.join('`'+i+'`' for i in ins) or '—'} | "
          f"{cmd[:48]} | `{k}` |")
    p("")

    # cross-participant lineage: which fotons consumed an output another produced
    p("## Build-on edges (who built on whose result)\n")
    edges = 0
    for fid, pl, k in fotons:
        pred = pl.get("predicate", {})
        for i in pred.get("inputs", []):
            ih = short(i.get("digest", {}).get("sha256"))
            if ih in produced:
                out0 = short((pl.get("subject", [{}])[0]).get("digest", {}).get("sha256"))
                p(f"- foton `{out0}` (signer `{k}`) builds on `{ih}`")
                edges += 1
    if not edges:
        p("_none yet_")
    p("")

    # claims
    p("## Claims (signed statements)\n")
    p("| about (subject) | predicate | by | signer |")
    p("|---|---|---|---|")
    for cid, pl, k in claims:
        subj = short((pl.get("subject", [{}])[0]).get("digest", {}).get("sha256")
                     or (pl.get("subject", [{}])[0]).get("uri"))
        body = pl.get("predicate", {})
        pred = (body.get("predicate", {}) or {}).get("uri", "").split("/")[-1]
        by = body.get("by", "")
        p(f"| `{subj}` | {pred} | {by[:24]} | `{k}` |")
    p("")
    p(f"_Generated {datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')} from the content-addressed union._")

if __name__ == "__main__":
    main()
