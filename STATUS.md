# Federation status

_Union of 5 registered participant(s): `pfed-a`, `pfed-b`, `pfed-c`, `pfed-demo`, `aggTest02`._

**12 fotons** (reproducible results) · **38 claims** (signed statements) in the union.

## Signers

| keyid | fotons | claims |
|---|--:|--:|
| `04beccabc4b7e1ca` | 0 | 1 |
| `1cc05d29616098c3` | 0 | 7 |
| `3d6428cc7ca58ac8` | 8 | 0 |
| `41689cef7a320957` | 0 | 2 |
| `66fd55ee56c8ac29` | 0 | 1 |
| `69cb06daaf69b642` | 0 | 5 |
| `70bb2c8898612eb9` | 0 | 1 |
| `815abf449909eb0c` | 0 | 2 |
| `8f69f0f5b834f833` | 0 | 3 |
| `96262b3619fc6903` | 2 | 2 |
| `ae6a2d9c56220894` | 0 | 11 |
| `bf2bd55457281324` | 0 | 1 |
| `c3af895761b197a8` | 0 | 1 |
| `cdb01ecbba16065a` | 1 | 0 |
| `df5be38c3b2fc3f8` | 0 | 1 |
| `ee0f0c123665bcbb` | 1 | 0 |

## Fotons (reproducible results)

| output | built on (inputs) | kind / cmd | signer |
|---|---|---|---|
| `eed552dbff99` | `61d6e3dc4c2e`, `b4fff526596d` | python work/step3_hvg.py | `3d6428cc7ca58ac8` |
| `b827998c0c49` | `6c46fc939ed9`, `f09b1c375d4c` | python work/step0_load.py | `3d6428cc7ca58ac8` |
| `795372847744` | `eed552dbff99`, `30fa01a85437` | python work/step4_pca.py | `3d6428cc7ca58ac8` |
| `d03f2846911a, fe768db44af2` | `1891f92d1f2c`, `5c1e49fdab74` | python work/coarse_map.py | `ee0f0c123665bcbb` |
| `fbcdd3116ba0` | `ac3bcf10a700`, `d46ca0f3f196` | python work/step7_split.py | `3d6428cc7ca58ac8` |
| `ac3bcf10a700, a6cc7d1a61ef` | `1891f92d1f2c`, `db41c334dd18` | python work/step6_cluster.py | `3d6428cc7ca58ac8` |
| `61d6e3dc4c2e` | `58fb727f1f19`, `183187c66d9c` | python work/step2_norm.py | `3d6428cc7ca58ac8` |
| `ceb4108170d2` | `0d6dab2320cf`, `3bb4a58e2138` | Rscript eda_warfarin.R | `96262b3619fc6903` |
| `58fb727f1f19` | `b827998c0c49`, `3fe657401f35` | python work/step1_qc.py | `3d6428cc7ca58ac8` |
| `c05e961f8524, c402694bf9c6` | `1891f92d1f2c`, `5bf57ea454be` | python work/fine_split2.py | `cdb01ecbba16065a` |
| `9e3703d8ffd9, 771e54e5e1b2, de5a1ce61311` | `0d6dab2320cf`, `3bb4a58e2138` | Rscript pk_model_warfarin.R | `96262b3619fc6903` |
| `1891f92d1f2c` | `795372847744`, `d2df4751162c` | python work/step5_neighbors.py | `3d6428cc7ca58ac8` |

## Build-on edges (who built on whose result)

- foton `eed552dbff99` (signer `3d6428cc7ca58ac8`) builds on `61d6e3dc4c2e`
- foton `795372847744` (signer `3d6428cc7ca58ac8`) builds on `eed552dbff99`
- foton `d03f2846911a` (signer `ee0f0c123665bcbb`) builds on `1891f92d1f2c`
- foton `fbcdd3116ba0` (signer `3d6428cc7ca58ac8`) builds on `ac3bcf10a700`
- foton `ac3bcf10a700` (signer `3d6428cc7ca58ac8`) builds on `1891f92d1f2c`
- foton `61d6e3dc4c2e` (signer `3d6428cc7ca58ac8`) builds on `58fb727f1f19`
- foton `58fb727f1f19` (signer `3d6428cc7ca58ac8`) builds on `b827998c0c49`
- foton `c05e961f8524` (signer `cdb01ecbba16065a`) builds on `1891f92d1f2c`
- foton `1891f92d1f2c` (signer `3d6428cc7ca58ac8`) builds on `795372847744`

## Claims (signed statements)

| about (subject) | predicate | by | signer |
|---|---|---|---|
| `246192ddce52` | located-at | CN=Participant-A | `69cb06daaf69b642` |
| `183187c66d9c` | located-at | CN=Participant-A | `ae6a2d9c56220894` |
| `cd61f3f0e492` | located-at | CN=Participant-C | `1cc05d29616098c3` |
| `f09b1c375d4c` | located-at | CN=Participant-A | `ae6a2d9c56220894` |
| `796e4c8c3f64` | located-at | CN=Participant-C | `1cc05d29616098c3` |
| `18dda5659158` | located-at | CN=Participant-C | `1cc05d29616098c3` |
| `a6cc7d1a61ef` | located-at | CN=Participant-A | `ae6a2d9c56220894` |
| `b313f8992e77` | reviewed | CN=Participant-A | `c3af895761b197a8` |
| `fe768db44af2` | located-at | CN=Participant-B | `8f69f0f5b834f833` |
| `3fe657401f35` | located-at | CN=Participant-A | `ae6a2d9c56220894` |
| `b4fff526596d` | located-at | CN=Participant-A | `ae6a2d9c56220894` |
| `b8b35240d3d1` | qualifies-as | CN=Participant-A | `69cb06daaf69b642` |
| `246192ddce52` | describes | CN=Participant-A | `69cb06daaf69b642` |
| `db41c334dd18` | located-at | CN=Participant-A | `ae6a2d9c56220894` |
| `b313f8992e77` | refines | CN=Participant-C | `66fd55ee56c8ac29` |
| `d46ca0f3f196` | located-at | CN=Participant-A | `ae6a2d9c56220894` |
| `f90b314cf558` | describes | CN=Participant-A | `41689cef7a320957` |
| `6899d057107e` | finding | CN=Participant-B | `df5be38c3b2fc3f8` |
| `f90b314cf558` | environment | CN=Participant-A | `69cb06daaf69b642` |
| `896fdf25781b` | finding | CN=Participant-A | `41689cef7a320957` |
| `f3a2740adceb` | authored | wolfgang | `96262b3619fc6903` |
| `6c46fc939ed9` | located-at | CN=Participant-A | `ae6a2d9c56220894` |
| `d2df4751162c` | located-at | CN=Participant-A | `ae6a2d9c56220894` |
| `5c1e49fdab74` | located-at | CN=Participant-B | `8f69f0f5b834f833` |
| `58e761b78782` | located-at | CN=Participant-C | `1cc05d29616098c3` |
| `b2629b72eec7` | authored | wolfgang | `815abf449909eb0c` |
| `d03f2846911a` | located-at | CN=Participant-B | `8f69f0f5b834f833` |
| `1891f92d1f2c` | located-at | CN=Participant-A | `ae6a2d9c56220894` |
| `ea209e0e6263` | finding | CN=Participant-C | `bf2bd55457281324` |
| `b8d48ed1410b` | authored | wolfgang | `96262b3619fc6903` |
| `5bf57ea454be` | located-at | CN=Participant-C | `1cc05d29616098c3` |
| `c402694bf9c6` | located-at | CN=Participant-C | `1cc05d29616098c3` |
| `b8b35240d3d1` | located-at | CN=Participant-A | `69cb06daaf69b642` |
| `6bea601f1f71` | reviewed | CN=Participant-C | `70bb2c8898612eb9` |
| `30fa01a85437` | located-at | CN=Participant-A | `ae6a2d9c56220894` |
| `7e9e052871eb` | authored | wolfgang | `815abf449909eb0c` |
| `c05e961f8524` | located-at | CN=Participant-C | `1cc05d29616098c3` |
| `f90b314cf558` | reviewed | CN=Participant-B | `04beccabc4b7e1ca` |

_Generated 2026-07-20T13:08:22Z from the content-addressed union._
