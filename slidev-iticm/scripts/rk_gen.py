#!/usr/bin/env python3
"""Generator Peta Rangkuman (slidev-iticm aturan 11).

Model: BARIS (tier) berisi rantai node; baris berselang-seling (serpentine).
Tautan utama antar baris = garis vertikal; tautan tambahan = bus di koridor.

Spec:
{
 "id","title","desc","eyebrow","subtitle","slide_title",
 "narasi":[..],"kp":[..],"chips":[..],"caption",
 "tiers":[{"label":"KONSEP","nodes":[{"id","t","s","tag","focal","type"}]}],
 "links":[{"from":"a","to":"b"}]
}

Jalankan: python3 knowledge/scripts/rk_gen.py <spec.json> [--svg-out f] [--slide-out f]
"""
import argparse
import json

# ---- token ITICM (kartu putih, aksen oranye, teks navy) ----
PAPER = "#ffffff"
INK = "#1a1a2e"
MUTED = "#6b7280"
SOFT = "#9aa1b1"
ACCENT = "#e86c00"
ACCENT_TINT = "#fff4e8"
RULE = "#e0e0e0"
BAND = "#f7f7f9"
SANS = "system-ui,-apple-system,'Segoe UI',Roboto,sans-serif"
MONO = "ui-monospace,SFMono-Regular,Menlo,Consolas,monospace"

W = 720
MARGIN = 20
NODE_H = 64
GAP = 18
TIER_LABEL_H = 20
TIER_PAD = 16
HEADER_H = 68
LEGEND_H = 46
CORNER = 8


def esc(s):
    return (str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            .replace('"', "&quot;"))


def wrap_title(t, limit):
    t = str(t)
    if len(t) <= limit:
        return [t]
    words = t.split()
    lines, cur = [], ""
    for w in words:
        if cur and len(cur) + 1 + len(w) > limit:
            lines.append(cur)
            cur = w
        else:
            cur = (cur + " " + w).strip()
    if cur:
        lines.append(cur)
    return lines[:2]


class Deck:
    def __init__(self, spec):
        self.s = spec
        self.pid = spec["id"]
        self.nodes = {}
        self.order = []
        self.tier_of = {}
        self.tiers = []
        self.edges = []
        self._collect()
        self._layout()
        self._ports()
        self._paths()

    # ---------------- model ----------------
    def _collect(self):
        for ti, tier in enumerate(self.s["tiers"]):
            self.tiers.append({"ti": ti, "label": tier.get("label", ""),
                               "nodes": [n["id"] for n in tier["nodes"]], "y": 0, "h": 0})
            for n in tier["nodes"]:
                self.nodes[n["id"]] = {"n": n, "ti": ti}
                self.tier_of[n["id"]] = ti
                self.order.append(n["id"])
        # rantai dalam satu baris
        for tier in self.tiers:
            for i in range(len(tier["nodes"]) - 1):
                self.edges.append({"from": tier["nodes"][i], "to": tier["nodes"][i + 1],
                                   "case": "chain"})
        # tautan utama antar baris (ujung rantai ke ujung rantai berikutnya)
        for i in range(len(self.tiers) - 1):
            self.edges.append({"from": self.tiers[i]["nodes"][-1],
                               "to": self.tiers[i + 1]["nodes"][0], "case": "main"})
        # tautan tambahan
        for l in self.s.get("links", []):
            self.edges.append({"from": l["from"], "to": l["to"], "case": "extra",
                               "accent": l.get("accent", False)})

    # ---------------- layout ----------------
    def _layout(self):
        y = HEADER_H
        for tier in self.tiers:
            tier["y"] = y
            tier["h"] = TIER_LABEL_H + NODE_H + TIER_PAD
            y += tier["h"]
        # tinggi koridor: jalur untuk tautan tambahan
        self.gaps = []
        for z in range(len(self.tiers) - 1):
            n = sum(1 for e in self.edges if e["case"] == "extra"
                    and min(self.tier_of[e["from"]], self.tier_of[e["to"]]) == z)
            self.gaps.append({"h": 30 + 16 * n})
        for z, g in enumerate(self.gaps):
            for tier in self.tiers:
                if tier["ti"] > z:
                    tier["y"] += g["h"]
        # posisi node (serpentine: baris ganjil dibalik)
        for tier in self.tiers:
            ids = tier["nodes"]
            cols = len(ids)
            usable = W - 2 * MARGIN
            col_w = (usable - (cols - 1) * GAP) // cols
            col_w = max(110, min(col_w, 190))
            total = cols * col_w + (cols - 1) * GAP
            x0 = MARGIN + (usable - total) // 2
            for ci, nid in enumerate(ids):
                col = (cols - 1 - ci) if tier["ti"] % 2 else ci
                self.nodes[nid].update({"x": x0 + col * (col_w + GAP),
                                        "y": tier["y"] + TIER_LABEL_H,
                                        "w": col_w, "h": NODE_H, "col": col})
            tier["col_w"] = col_w
        self.bottom = self.tiers[-1]["y"] + self.tiers[-1]["h"]
        self.legend_y = self.bottom + 14
        self.H = self.legend_y + LEGEND_H

    # ---------------- ports ----------------
    def _ports(self):
        out_g, in_g = {}, {}
        for e in self.edges:
            if e["case"] == "chain":
                if self.nodes[e["to"]]["col"] > self.nodes[e["from"]]["col"]:
                    e["out_side"], e["in_side"] = "R", "L"
                else:
                    e["out_side"], e["in_side"] = "L", "R"
            else:
                e["out_side"], e["in_side"] = "B", "T"
            out_g.setdefault((e["from"], e["out_side"]), []).append(e)
            in_g.setdefault((e["to"], e["in_side"]), []).append(e)
        for grp, side_key, is_out in ((out_g, "out_side", True), (in_g, "in_side", False)):
            for (nid, side), lst in grp.items():
                box = self.nodes[nid]
                mains = [e for e in lst if e["case"] == "main"]
                lst.sort(key=lambda e: self.nodes[e["to"] if is_out else e["from"]]["x"])
                if mains:
                    for e in mains:
                        e["_port"] = 0.5
                    others = [e for e in lst if e["case"] != "main"]
                    n = len(others)
                    for i, e in enumerate(others):
                        e["_port"] = 0.82 if n == 1 else 0.5 + 0.32 * (2 * i / (n - 1) - 1)
                else:
                    for i, e in enumerate(lst):
                        e["_port"] = (i + 1) / (len(lst) + 1)
                for e in lst:
                    if side in ("R", "L"):
                        e["pos"] = box["y"] + box["h"] * e["_port"]
                    else:
                        e["pos"] = box["x"] + box["w"] * e["_port"]
                    if is_out:
                        e["out"] = e["pos"]
                    else:
                        e["in"] = e["pos"]

    # ---------------- routing ----------------
    def _paths(self):
        for e in self.edges:
            fb, tb = self.nodes[e["from"]], self.nodes[e["to"]]
            if e["case"] == "chain":
                right = self.nodes[e["to"]]["col"] > self.nodes[e["from"]]["col"]
                p1 = ((fb["x"] + fb["w"], e["out"]) if right else (fb["x"], e["out"]))
                p2 = ((tb["x"], e["in"]) if right else (tb["x"] + tb["w"], e["in"]))
                if abs(p1[1] - p2[1]) < 0.5:
                    e["pts"] = [p1, p2]
                else:
                    mx = (p1[0] + p2[0]) / 2
                    e["pts"] = [p1, (mx, p1[1]), (mx, p2[1]), p2]
            elif e["case"] == "main":
                e["pts"] = [(e["out"], fb["y"] + fb["h"]), (e["in"], tb["y"])]
            else:
                z = min(fb["ti"], tb["ti"])
                g = self.gaps[z]
                gtop = self.tiers[z]["y"] + self.tiers[z]["h"]
                cross = [x for x in self.edges if x["case"] == "extra"
                         and min(self.tier_of[x["from"]], self.tier_of[x["to"]]) == z]
                cross.sort(key=lambda x: self.nodes[x["from"]]["x"], reverse=True)
                idx = cross.index(e)
                corr = gtop + g["h"] - 14 - idx * 16
                p1 = (e["out"], fb["y"] + fb["h"])
                p2 = (e["in"], tb["y"])
                e["pts"] = [p1, (p1[0], corr), (p2[0], corr), p2]

    def _corner(self, pts, r=CORNER):
        if len(pts) < 3:
            return "M " + " L ".join("%.0f,%.0f" % (x, y) for x, y in pts)
        d = ["M %.0f,%.0f" % (pts[0][0], pts[0][1])]
        for i in range(1, len(pts) - 1):
            x0, y0 = pts[i - 1]
            x1, y1 = pts[i]
            x2, y2 = pts[i + 1]
            r1 = max(0.5, min(r, abs(x1 - x0) / 2, abs(y1 - y0) / 2))
            r2 = max(0.5, min(r, abs(x2 - x1) / 2, abs(y2 - y1) / 2))
            if abs(x1 - x0) < 0.5:
                d.append("L %.0f,%.0f" % (x1, y1 - r1 if y2 > y1 else y1 + r1))
                d.append("Q %.0f,%.0f %.0f,%.0f" % (x1, y1, x1 + (r2 if x2 > x1 else -r2), y1))
            else:
                d.append("L %.0f,%.0f" % (x1 - r1 if x2 > x0 else x1 + r1, y1))
                d.append("Q %.0f,%.0f %.0f,%.0f" % (x1, y1, x1, y1 + (r2 if y2 > y1 else -r2)))
        d.append("L %.0f,%.0f" % (pts[-1][0], pts[-1][1]))
        return " ".join(d)

    # ---------------- svg ----------------
    def svg(self):
        p = self.pid
        o = []
        o.append('<svg id="rkSvg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" '
                 'width="100%%" height="auto" style="max-width:720px" role="img" '
                 'aria-labelledby="rk-%s-title rk-%s-desc">' % (W, self.H, p, p))
        o.append('<title id="rk-%s-title">%s</title>' % (p, esc(self.s["title"])))
        o.append('<desc id="rk-%s-desc">%s</desc>' % (p, esc(self.s["desc"])))
        o.append("<defs>")
        o.append('<marker id="rk-%s-arrow" markerWidth="8" markerHeight="6" refX="7" refY="3" '
                 'orient="auto"><polygon points="0 0, 8 3, 0 6" fill="%s"/></marker>' % (p, MUTED))
        o.append('<marker id="rk-%s-arrow-accent" markerWidth="8" markerHeight="6" refX="7" '
                 'refY="3" orient="auto"><polygon points="0 0, 8 3, 0 6" fill="%s"/></marker>'
                 % (p, ACCENT))
        o.append("</defs>")
        o.append('<rect width="%d" height="%d" fill="%s"/>' % (W, self.H, PAPER))

        o.append('<text x="%d" y="30" fill="%s" font-size="8" font-family="%s" '
                 'letter-spacing="0.14em">%s</text>'
                 % (MARGIN, MUTED, MONO, esc(self.s.get("eyebrow", "RANGKUMAN"))))
        o.append('<text x="%d" y="52" fill="%s" font-size="17" font-weight="700" '
                 'font-family="%s">%s</text>'
                 % (MARGIN, INK, SANS, esc(self.s.get("title", ""))))
        if self.s.get("subtitle"):
            o.append('<text x="%d" y="%d" fill="%s" font-size="10" font-family="%s">%s</text>'
                     % (MARGIN, HEADER_H - 8, MUTED, SANS, esc(self.s["subtitle"])))

        for tier in self.tiers:
            o.append('<rect x="%d" y="%.0f" width="%d" height="%.0f" rx="8" fill="%s" '
                     'stroke="%s" stroke-width="1"/>'
                     % (MARGIN - 8, tier["y"], W - 2 * MARGIN + 16, tier["h"], BAND, RULE))
            o.append('<text x="%d" y="%.0f" fill="%s" font-size="8" font-family="%s" '
                     'letter-spacing="0.14em">%s</text>'
                     % (MARGIN, tier["y"] + 14, MUTED, MONO, esc(tier["label"].upper())))

        for e in self.edges:
            focal = e.get("accent") or (self.nodes[e["from"]]["n"].get("focal")
                                        and self.nodes[e["to"]]["n"].get("focal"))
            col = ACCENT if focal else MUTED
            mk = "rk-%s-arrow-accent" % p if focal else "rk-%s-arrow" % p
            o.append('<path d="%s" fill="none" stroke="%s" stroke-width="1.3" '
                     'marker-end="url(#%s)"/>' % (self._corner(e["pts"]), col, mk))

        for nid in self.order:
            b = self.nodes[nid]
            n = b["n"]
            focal = n.get("focal")
            typ = n.get("type", "step")
            if focal:
                fill, stroke, tcol = ACCENT_TINT, ACCENT, ACCENT
            elif typ == "store":
                fill, stroke, tcol = "rgba(26,26,46,0.05)", SOFT, INK
            elif typ == "boundary":
                fill, stroke, tcol = "rgba(232,108,0,0.05)", "rgba(232,108,0,0.5)", INK
            else:
                fill, stroke, tcol = PAPER, INK, INK
            dash = ' stroke-dasharray="4,4"' if typ == "boundary" else ""
            o.append('<rect x="%.0f" y="%.0f" width="%d" height="%d" rx="6" fill="%s" '
                     'stroke="%s" stroke-width="1"%s/>'
                     % (b["x"], b["y"], b["w"], b["h"], fill, stroke, dash))
            cx = b["x"] + b["w"] / 2
            if n.get("tag"):
                tw = len(n["tag"]) * 4.2 + 10
                o.append('<rect x="%.0f" y="%.0f" width="%.0f" height="12" rx="2" fill="none" '
                         'stroke="%s" stroke-opacity="0.4" stroke-width="0.8"/>'
                         % (b["x"] + 8, b["y"] + 6, tw, stroke))
                o.append('<text x="%.0f" y="%.0f" fill="%s" fill-opacity="0.8" font-size="6" '
                         'font-family="%s" text-anchor="middle" letter-spacing="0.08em">%s</text>'
                         % (b["x"] + 8 + tw / 2, b["y"] + 15, stroke, MONO, esc(n["tag"].upper())))
            lines = wrap_title(n["t"], max(9, int((b["w"] - 16) / 7.2)))
            name_y = b["y"] + (32 if n.get("tag") else 28) - (len(lines) - 1) * 7
            for i, ln in enumerate(lines):
                o.append('<text x="%.0f" y="%.0f" fill="%s" font-size="13" font-weight="600" '
                         'font-family="%s" text-anchor="middle">%s</text>'
                         % (cx, name_y + i * 15, tcol, SANS, esc(ln)))
            if n.get("s"):
                o.append('<text x="%.0f" y="%.0f" fill="%s" font-size="9.5" font-family="%s" '
                         'text-anchor="middle">%s</text>'
                         % (cx, b["y"] + b["h"] - 12, MUTED, MONO, esc(n["s"])))

        ly = self.legend_y
        o.append('<line x1="%d" y1="%.0f" x2="%d" y2="%.0f" stroke="%s" stroke-width="1"/>'
                 % (MARGIN, ly, W - MARGIN, ly, RULE))
        items = [("Fokus", ACCENT, True), ("Langkah / alat", INK, False),
                 ("Data / bukti", SOFT, False)]
        x = MARGIN
        for label, col, foc in items:
            fill = ACCENT_TINT if foc else ("rgba(26,26,46,0.05)" if col == SOFT else PAPER)
            o.append('<rect x="%.0f" y="%.0f" width="14" height="10" rx="2" fill="%s" '
                     'stroke="%s" stroke-width="1"/>' % (x, ly + 13, fill, col))
            o.append('<text x="%.0f" y="%.0f" fill="%s" font-size="8" font-family="%s" '
                     'letter-spacing="0.1em">%s</text>'
                     % (x + 20, ly + 22, MUTED, MONO, esc(label.upper())))
            x += 26 + len(label) * 5.6
        o.append("</svg>")
        return "\n".join(o)

    # ---------------- slide html ----------------
    def slide_html(self):
        s = self.s
        kp = "".join("<li>%s</li>" % esc(x) for x in s.get("kp", []))
        chips = "".join('<span class="chip">%s</span>' % esc(c) for c in s.get("chips", []))
        nar = "".join('<p class="mt-3">%s</p>' % esc(x) for x in s.get("narasi", []))
        cap_top = ('<p class="caption">%s</p>\n' % esc(s["caption_top"])) if s.get("caption_top") else ""
        return (
            '<div class="narrow">\n'
            '<h2 class="text-2xl font-bold border-l-8 border-orange-500 pl-3">%s</h2>\n'
            '%s</div>\n'
            '<div class="narrow kp"><div class="t">Ringkasan</div><ul>%s</ul></div>\n'
            % (esc(s["slide_title"]), nar, kp)
            + (('<div class="narrow">%s</div>\n' % chips) if chips else "")
            + cap_top
            + '<div class="rkWrap">\n%s\n'
              '<div style="text-align:center;margin-top:10px">'
              '<button class="rkBtn" onclick="toggleRk(true)">&#128269; Perbesar Peta Rangkuman</button></div>\n'
              '<p class="caption">%s</p>\n</div>\n'
              % (self.svg(), esc(s.get("caption", "")))
        )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("spec")
    ap.add_argument("--svg-out")
    ap.add_argument("--slide-out")
    a = ap.parse_args()
    spec = json.load(open(a.spec, encoding="utf-8"))
    d = Deck(spec)
    if a.svg_out:
        open(a.svg_out, "w", encoding="utf-8").write(d.svg())
    if a.slide_out:
        open(a.slide_out, "w", encoding="utf-8").write(d.slide_html())
    if not a.svg_out and not a.slide_out:
        print(d.svg())
    else:
        print("viewBox 0 0 %d %d | svg %d B | slide %d B"
              % (W, d.H, len(d.svg()), len(d.slide_html())))


if __name__ == "__main__":
    main()
