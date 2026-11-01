#!/usr/bin/env python3
"""Periksa kepatuhan narasi deck slidev terhadap skill humanizer-indonesia.

Pemakaian:
    python3 check_humanizer.py <path/to/index.html> [--preset {ajar,akademik,semiformal}]
"""
import os
import re
import subprocess
import sys
import tempfile

def extract_prose(html_path):
    with open(html_path, "r", encoding="utf-8") as f:
        html = f.read()

    texts = []
    # Paragraf utama
    for p in re.findall(r'<p class="mt-3">(.*?)</p>', html, flags=re.DOTALL):
        clean = re.sub(r'<[^>]+>', '', p).strip()
        if clean:
            texts.append(clean)

    # Kotak maksud
    for p in re.findall(r'<p class="maksud-text">(.*?)</p>', html, flags=re.DOTALL):
        clean = re.sub(r'<[^>]+>', '', p).strip()
        if clean:
            texts.append(clean)

    return "\n\n".join(texts)

def main():
    if len(sys.argv) < 2:
        print("Penggunaan: python3 check_humanizer.py <path/to/index.html> [--preset {ajar,akademik,semiformal}]")
        sys.exit(1)

    html_path = sys.argv[1]
    preset = "ajar"
    if "--preset" in sys.argv:
        p_idx = sys.argv.index("--preset")
        if p_idx + 1 < len(sys.argv):
            preset = sys.argv[p_idx + 1]

    if not os.path.exists(html_path):
        print(f"Galat: berkas {html_path} tidak ditemukan.")
        sys.exit(1)

    # Cari metrik.py di humanizer-indonesia
    script_dir = os.path.dirname(os.path.abspath(__file__))
    candidates = [
        os.path.join(script_dir, "..", "..", "humanizer-indonesia", "scripts", "metrik.py"),
        os.path.expanduser("~/.agents/skills/humanizer-indonesia/scripts/metrik.py"),
        os.path.expanduser("~/.openclaw/skills/humanizer-indonesia/scripts/metrik.py"),
    ]
    metrik_script = None
    for c in candidates:
        if os.path.exists(c):
            metrik_script = os.path.abspath(c)
            break

    if not metrik_script:
        print("Galat: skrip metrik.py dari humanizer-indonesia tidak ditemukan.")
        sys.exit(1)

    prose = extract_prose(html_path)
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", suffix=".txt", delete=False) as tf:
        tf.write(prose)
        tmp_txt = tf.name

    try:
        cmd = [sys.executable, metrik_script, "--preset", preset, tmp_txt]
        res = subprocess.run(cmd, capture_output=True, text=True)
        print(res.stdout)
        if res.stderr:
            print(res.stderr, file=sys.stderr)
        sys.exit(res.returncode)
    finally:
        if os.path.exists(tmp_txt):
            os.remove(tmp_txt)

if __name__ == "__main__":
    main()
