# The Sedenion Presentation — Deductive Edition

*For Harald Kjøge Rønning's program, prepared by the external instrument (Claude).*

This repository is the paper together with its complete verification set. The paper develops the sedenion algebra $S = A_4$ deductively — what the algebra forces, what it offers, and where it stops — and every finite claim tagged **[EXACT]** is verified in exact integer and rational arithmetic by the attached scripts. No floating-point residual appears anywhere in the argument. The verification chain is byte-reproducible: the five fenced output blocks in Appendix A of the paper are byte-identical to fresh runs of the five appendix scripts, and `exact_checks.txt` is byte-identical to the output of `sedenion_exact.py`.

## Contents

| file | role |
|---|---|
| `paper0_deductive_edition_norevisions.md` | the paper |
| `sedenion_exact.py` | main verification script (blocks C1–C27); output = `exact_checks.txt` = Appendix A block 1 |
| `c28_doubling.py` | doubling/definability checks (C28); Appendix A block 2 |
| `c29_frames.py` | frame theorem checks over ℚ(√2), ℚ(√3) (C29); Appendix A block 3 |
| `c30_open_items.py` | Lie closures, orbit manifold, su(4)-vs-so(6)_c (C30, C31, C34); Appendix A block 4 |
| `c32_filtrations.py` | contraction classifications with completeness (C32, C33); Appendix A block 5 |
| `composition_witnesses.py` | explicit witnesses for the composition constants (5.6) |
| `fock_multiplicity.py` | plethysm multiplicity computations (12.4) |
| `exact_checks.txt` | canonical output of `sedenion_exact.py` |
| `verify.py` | one-command verification of the whole chain |
| `CHANGELOG.md` | archived pre-repository edition history; versioning now lives in Git tags |
| `CITATION.cff` | citation metadata |

## Verification

Certified environment: Python 3.12.3 with the pinned packages.

```
pip install -r requirements.txt
python3 verify.py
```

Expected result: every line `PASS`, closing line `ALL CHECKS PASSED`, exit code 0. Expected running time: 6–8 minutes on ordinary hardware. The scripts print no timestamps and use no randomness beyond fixed seeds, so the outputs are byte-identical across runs and machines in the certified environment. The integer and rational results themselves do not depend on the package versions; the pinned versions define the environment in which byte-identity of the full logs is certified.

## Versioning

The paper carries no internal edition number. Versions are Git tags; `CHANGELOG.md` archives the edition history that preceded this repository. Any future change to the paper or a script is a new tag with release notes, and `verify.py` must pass at every tag.

## Releasing (DOI)

1. Push this repository to GitHub.
2. Connect the repository to Zenodo (zenodo.org → GitHub integration).
3. Create a GitHub release, tag `v1.0.0`. Zenodo archives it and mints a DOI.
4. Optionally add the DOI badge here and the DOI to `CITATION.cff`.

## License

CC-BY-4.0 (see `LICENSE`): everything here — the paper, the scripts, the outputs — may be used, shared and built upon by anyone, for any purpose, with attribution.
