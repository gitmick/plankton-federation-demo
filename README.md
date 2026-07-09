# plankton-federation-demo

A neutral **aggregator** for a federation of independent repositories. Participants each keep their
own repo of signed, content-addressed records (plankton fotons + nekton claims); this repo pulls them
into one **union** and reports *who has done what* — without ever re-running anything or trusting a
participant's word over the hash.

The point: three people who **do not share a repo** can still discover and build on each other's work,
by content hash, through a hub that only *reports facts*.

## How it works

- **Register** — open a *Register a participant* issue (repo URL + optional pubkey). The `register`
  Action appends you to [`participants.json`](participants.json) and kicks off an aggregate run.
- **Aggregate** — the `aggregate` Action clones each registered repo and `kton mirror`s its
  `plankton-data/` / `nekton-data/` into [`federation/`](federation). Records are named by content
  hash, so the union is **conflict-free by construction** — git is the federation transport.
- **Read** — [`STATUS.md`](STATUS.md) is regenerated each run: every foton (by output hash, signer,
  and what it built on), every claim (subject, predicate, signer), and the **build-on edges** showing
  who built on whose result across repos.

## What the aggregator does NOT do

It does not execute protocols, re-run fotons, or decide whom to trust. It mirrors signed records and
reports. Trust in a result comes from **re-running it**; trust in a statement comes from **its
signature** — both verifiable by anyone against the union, independent of this hub.

## Participate

1. Put a `plankton-data/` and/or `nekton-data/` registry at your repo root (e.g. `plankton add` /
   `nekton add` your signed records, commit the registry).
2. Open a **Register a participant** issue here.
3. Push new records anytime; a scheduled (or dispatched) aggregate run folds them in.
