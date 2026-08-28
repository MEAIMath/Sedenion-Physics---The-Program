#!/usr/bin/env python3
"""One-command verification of the deductive edition.

Runs the seven scripts, then checks:
  1. the output of sedenion_exact.py is byte-identical to exact_checks.txt;
  2. the five fenced output blocks in the paper are byte-identical to the
     fresh outputs of sedenion_exact.py, c28_doubling.py, c29_frames.py,
     c30_open_items.py and c32_filtrations.py;
  3. every script exits 0, and every checking script reports "failures: 0".
Exit code 0 iff everything passes. Expected running time: 6-8 minutes.
"""
import re, subprocess, sys

SCRIPTS = ["sedenion_exact.py", "c28_doubling.py", "c29_frames.py",
           "c30_open_items.py", "c32_filtrations.py",
           "composition_witnesses.py", "fock_multiplicity.py"]
BLOCK_SOURCES = SCRIPTS[:5]          # order of the fenced blocks in the paper
CHECKING = SCRIPTS[:5]               # scripts that end with a failures count

def run(name):
    r = subprocess.run([sys.executable, name], capture_output=True, text=True)
    return r.returncode, r.stdout

def main():
    ok = True
    outputs = {}
    for s in SCRIPTS:
        code, out = run(s)
        outputs[s] = out
        line = out.rstrip("\n").splitlines()[-1] if out.strip() else ""
        good = (code == 0) and (s not in CHECKING or line == "failures: 0")
        print(f"[{'PASS' if good else 'FAIL'}] {s}: exit {code}" +
              (f", last line: {line!r}" if s in CHECKING else ""))
        ok &= good

    ec = open("exact_checks.txt").read()
    same = outputs["sedenion_exact.py"] == ec
    print(f"[{'PASS' if same else 'FAIL'}] sedenion_exact.py output == exact_checks.txt (byte-identical)")
    ok &= same

    paper = open("paper0_deductive_edition_norevisions.md").read()
    blocks = re.findall(r"^```\n(.*?)\n```", paper, flags=re.S | re.M)
    good = len(blocks) == 5
    print(f"[{'PASS' if good else 'FAIL'}] paper contains exactly 5 fenced output blocks (found {len(blocks)})")
    ok &= good
    for b, s in zip(blocks, BLOCK_SOURCES):
        same = b == outputs[s].rstrip("\n")
        print(f"[{'PASS' if same else 'FAIL'}] appendix block == fresh output of {s} (byte-identical)")
        ok &= same

    print("\n" + ("ALL CHECKS PASSED" if ok else "VERIFICATION FAILED"))
    return 0 if ok else 1

if __name__ == "__main__":
    sys.exit(main())
