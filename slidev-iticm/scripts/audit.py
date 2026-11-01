#!/usr/bin/env python3
"""Audit deck slidev IT104 terhadap skill slidev-iticm.

    python3 slidev/_build/audit.py p01-konsep-dasar-algoritma ...

Cek: jumlah section, caption lihat sX, kuis 3 details, drill 3 uji + dev backup,
Prism (CDN + <code class="language-x"> + tombol Salin), balance div per section,
mermaid aman, identitas deck (nggak ada sisa "P05"), GLO, dan node --check script.
"""
import os
import re
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # slidev/


def sections_of(html):
    return re.findall(r'<section class="slide" id="s(\d+)">([\s\S]*?)</section>', html)


def audit(dirname):
    path = os.path.join(ROOT, dirname, 'index.html')
    html = open(path, encoding='utf-8').read()
    err = []
    warn = []
    secs = sections_of(html)
    ids = [int(i) for i, _ in secs]
    n = max(ids)
    if ids != list(range(n + 1)):
        err.append('id section bukan 0..%d: %s' % (n, ids))
    if len(secs) != n + 1:
        err.append('jumlah section %d != N+1 %d' % (len(secs), n + 1))

    # h2 bernomor 1..N-1
    nums = [int(m.group(1)) for m in
            (re.search(r'<h2[^>]*>(\d+)\.', body) for _, body in secs) if m]
    if nums != list(range(1, n)):
        err.append('nomor h2 tidak lengkap 1..%d: %s' % (n - 1, nums))

    # caption: lihat sX (kecuali cover, kuis, drill)
    for sid, body in secs:
        caps = re.findall(r'<p class="caption">(.*?)</p>', body, re.S)
        kind = 'kuis' if 'Kuis 3 Soal' in body else ('drill' if 'Drill ' in body else '')
        for c in caps:
            refs = re.findall(r'lihat s(\d+)', c)
            if not refs:
                if not kind:
                    err.append('s%s caption tanpa rujukan: %s' % (sid, c[:60]))
                continue
            for r in refs:
                if not (1 <= int(r) <= n - 1):
                    err.append('s%s caption rujuk s%s di luar rentang' % (sid, r))
                if int(r) == int(sid) and not kind:
                    err.append('s%s caption rujuk dirinya sendiri' % sid)

    # kuis: 3 details
    kuis = [b for _, b in secs if 'Kuis 3 Soal' in b]
    if len(kuis) != 1:
        err.append('slide kuis tidak ketemu (%d)' % len(kuis))
    else:
        det = re.findall(r'<details class="flow"><summary>Lihat Jawaban</summary>', kuis[0])
        if len(det) != 3:
            err.append('kuis punya %d details (harus 3)' % len(det))
        if 'lihat s' in kuis[0]:
            err.append('kuis tidak boleh pakai "lihat s"')

    # drill: 3 uji + dev backup
    dr = [b for _, b in secs if 'Sebab:' in b]
    if len(dr) != 1:
        err.append('slide drill tidak ketemu (%d)' % len(dr))
    else:
        if dr[0].count('Sebab:') != 3:
            err.append('drill punya %d uji (harus 3)' % dr[0].count('Sebab:'))
        if 'dev backup:' not in dr[0]:
            err.append('drill tanpa <!-- dev backup -->')

    # prism (hitung hanya isi deck, bukan string di dalam <script>)
    k = html.rfind('\n<script>')
    content = html[:k] if k > 0 else html
    code_blocks = len(re.findall(r'<code class="language-', content))
    pres = len(re.findall(r'<pre', content))
    cdn = html.count('prismjs@1.29.0')
    if code_blocks:
        if cdn != 7:
            err.append('ada %d blok kode tapi CDN Prism %d (harus 7)' % (code_blocks, cdn))
        if pres != code_blocks:
            err.append('<pre> %d tapi <code class="language-*> %d' % (pres, code_blocks))
        if 'codeBtn' not in html:
            err.append('tombol Salin (codeBtn) hilang')
        for m in re.finditer(r'<pre([^>]*)>(.*?)</pre>', content, re.S):
            if '<code class="language-' not in m.group(2):
                err.append('blok kode tanpa <code class="language-*">')
                break
    else:
        if cdn:
            err.append('tanpa blok kode tapi CDN Prism %d (harus 0)' % cdn)
        if 'codeBtn' in html:
            err.append('tanpa blok kode tapi tombol Salin masih ada')

    # balance div per section
    for sid, body in secs:
        if body.count('<div') != body.count('</div>'):
            err.append('s%s div tidak balance (%d vs %d)' % (sid, body.count('<div'), body.count('</div>')))
        if body.count('<details') != body.count('</details>'):
            err.append('s%s details tidak balance' % sid)

    # mermaid aman
    for mm in re.findall(r'<div class="mermaid">(.*?)</div>', html, re.S):
        if re.search(r'\+\s*\w', mm) and 'sequenceDiagram' not in mm:
            warn.append('mermaid pakai "+" (risiko translate NaN)')
        if 'Note over' in mm:
            err.append('mermaid pakai "Note over"')
    if '<div class="mermaid">' in html and 'mermaid.initialize' not in html:
        err.append('mermaid.initialize hilang')

    # identitas deck
    for bad in ('Glosarium P05', 'Peta Rangkuman P05', 'p05state_v1'):
        if bad in html:
            err.append('sisa identitas %s' % bad)
    title = re.search(r'<title>(.*?)</title>', html).group(1)
    if 'P05' in title:
        err.append('title masih P05')

    # GLO
    glo = re.search(r'const GLO=\[([\s\S]*?)\n\];', html)
    if not glo or len(re.findall(r'\["', glo.group(1))) < 10:
        err.append('GLO kosong / terlalu sedikit')
    if 'const GLO_CATS=[' not in html:
        err.append('GLO_CATS hilang')

    # script inline
    scripts = re.findall(r'<script>([\s\S]*?)</script>', html)
    if not scripts:
        err.append('tidak ada <script> inline')
    else:
        with tempfile.NamedTemporaryFile('w', suffix='.js', delete=False) as f:
            f.write(scripts[-1])
            tmp = f.name
        r = subprocess.run(['node', '--check', tmp], capture_output=True, text=True)
        os.unlink(tmp)
        if r.returncode != 0:
            err.append('node --check gagal: %s' % r.stderr.strip().split('\n')[0])

    return dirname, n, len(secs), code_blocks, err, warn


if __name__ == '__main__':
    dirs = sys.argv[1:]
    if not dirs:
        dirs = sorted(d for d in os.listdir(ROOT)
                      if re.match(r'^p\d\d-', d) and os.path.exists(os.path.join(ROOT, d, 'index.html')))
    bad = 0
    for d in dirs:
        name, n, ns, code, err, warn = audit(d)
        status = 'OK  ' if not err else 'FAIL'
        if err:
            bad += 1
        print('%s %-34s N=%-3s section=%-3s kode=%-2s' % (status, name, n, ns, code))
        for e in err:
            print('       ! ' + e)
        for w in warn:
            print('       ~ ' + w)
    print('\n%d deck gagal' % bad)
    sys.exit(1 if bad else 0)
