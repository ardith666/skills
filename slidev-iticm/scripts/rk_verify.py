#!/usr/bin/env python3
"""Verifikasi hasil injeksi Peta Rangkuman pada deck.

Cek: id section unik & berurutan, const N cocok, rkSvg ada satu kali,
modal + CSS + JS + state rko ada, slide rangkuman punya heading.

Jalankan: python3 knowledge/scripts/rk_verify.py <deckdir> [<deckdir> ...]
"""
import os
import re
import sys


def verify(deck_dir):
    path = os.path.join(deck_dir, "index.html")
    t = open(path, encoding="utf-8").read()
    errs = []
    secs = list(re.finditer(r"<section\b.*?</section>", t, re.S))
    ids = []
    for m in secs:
        mm = re.search(r'id="(s\d+)"', m.group(0))
        ids.append(mm.group(1) if mm else "?")
    exp = ["s%d" % i for i in range(len(secs))]
    if ids != exp:
        errs.append("id section tidak berurutan: %s" % ids)
    n_const = re.search(r"const N=(\d+);", t)
    if not n_const:
        errs.append("const N tidak ditemukan")
    elif int(n_const.group(1)) != len(secs) - 1:
        errs.append("const N=%s tapi jumlah section %d" % (n_const.group(1), len(secs)))
    if t.count('id="rkSvg"') != 1:
        errs.append("rkSvg jumlah %d (harus 1)" % t.count('id="rkSvg"'))
    for needle, label in (
        ('id="rkModal"', "modal HTML"),
        ('id="rkZoomInner"', "wadah zoom"),
        ('function rkClone()', "JS rkClone"),
        ('function rkZoom(', "JS rkZoom"),
        ('function toggleRk(', "JS toggleRk"),
        ('rko:(function()', "state rko"),
        ('if(st&&st.rko)', "restore rko"),
        (".rkWrap{", "CSS rkWrap"),
        ("#rkModal{", "CSS modal"),
        ("#gloModal,#rkModal,#jumpWidget", "aturan print"),
    ):
        if needle not in t:
            errs.append("%s hilang (%s)" % (label, needle))
    # slide rangkuman
    rk = [m.group(0) for m in secs if "rkSvg" in m.group(0)]
    if len(rk) != 1:
        errs.append("slide rangkuman %d (harus 1)" % len(rk))
    else:
        if "toggleRk(true)" not in rk[0]:
            errs.append("slide rangkuman tanpa tombol perbesar")
        if not re.search(r"<h2[^>]*>", rk[0]):
            errs.append("slide rangkuman tanpa judul h2")
    # tombol kembali di penutup harus ke slide isi terakhir
    tail = secs[-1].group(0)
    m_ret = re.search(r'onclick="goTo\((\d+)\)"', tail)
    if m_ret and int(m_ret.group(1)) != len(secs) - 2:
        errs.append("tombol penutup goTo(%s) harus %d" % (m_ret.group(1), len(secs) - 2))
    return os.path.basename(deck_dir), len(secs), errs


def main():
    bad = 0
    for d in sys.argv[1:]:
        name, n, errs = verify(d)
        print("%-34s section=%-3d %s" % (name, n, "OK" if not errs else "FAIL"))
        for e in errs:
            print("    ERROR  " + e)
        bad += len(errs)
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
