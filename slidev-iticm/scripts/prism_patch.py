#!/usr/bin/env python3
# Suntik aturan 12 skill slidev-iticm (Prism.js + tombol Salin) ke deck slidev.
# Idempotent: jalankan ulang aman, blok yang sudah dibungkus <code> dilewati.
# Pola acuan: Basis Data/slidev/p06-sql-dml-dan-crud-php/index.html
import re, sys, glob, os

CDN = '''<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/prismjs@1.29.0/themes/prism-tomorrow.min.css">
<script src="https://cdn.jsdelivr.net/npm/prismjs@1.29.0/components/prism-core.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/prismjs@1.29.0/components/prism-markup.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/prismjs@1.29.0/components/prism-clike.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/prismjs@1.29.0/components/prism-markup-templating.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/prismjs@1.29.0/components/prism-php.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/prismjs@1.29.0/components/prism-sql.min.js"></script>
'''

PRE_OLD = 'pre{background:#2d2d3a;color:#c0c5d0;padding:14px;border-radius:10px;overflow:auto;font-size:.82rem;max-width:720px;margin:12px auto}'
PRE_NEW = 'pre{background:#2d2d3a;color:#c0c5d0;padding:14px;border-radius:10px;overflow:auto;font-size:.82rem;max-width:720px;margin:12px auto;text-align:left;position:relative}'

PRISM_CSS = '''
pre code{background:none;padding:0;border-radius:0;font-size:inherit}
pre[class*=language-]{background:#2d2d3a;color:#c0c5d0;padding:14px;margin:12px auto;max-width:720px;border-radius:10px;font-size:.82rem;line-height:1.45}
pre code[class*=language-]{color:inherit}
.codeBtn{position:absolute;top:6px;right:6px;z-index:2;background:#1a1a2e;color:#c0c5d0;border:1px solid #4a4a60;border-radius:6px;font-size:.68rem;padding:2px 8px;cursor:pointer;opacity:0;transition:opacity .18s}
pre:hover .codeBtn,.codeBtn:focus{opacity:1}
.codeBtn:hover{background:#e86c00;border-color:#e86c00;color:#fff}
@media (hover:none){.codeBtn{opacity:1}}
@media print{.codeBtn{display:none!important}}
'''

PRISM_JS = '''function kodeTeks(pre){var c=pre.querySelector('code');return c?c.textContent:pre.textContent;}
function salinLama(t,ok){var ta=document.createElement('textarea');ta.value=t;ta.setAttribute('readonly','');ta.style.position='fixed';ta.style.left='-9999px';document.body.appendChild(ta);ta.select();try{document.execCommand('copy');ok();}catch(e){}document.body.removeChild(ta);}
function salinTeks(t,btn){var ok=function(){btn.textContent='Tersalin';setTimeout(function(){btn.textContent='Salin';},1400);};if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(t).then(ok,function(){salinLama(t,ok);});}else{salinLama(t,ok);}}
document.querySelectorAll('pre').forEach(function(pre){if(!pre.querySelector('code'))return;var b=document.createElement('button');b.className='codeBtn';b.type='button';b.textContent='Salin';b.setAttribute('aria-label','Salin kode');b.onclick=function(e){e.preventDefault();salinTeks(kodeTeks(pre),b);};pre.appendChild(b);});
'''


def lang_for(attrs, body):
    """Pilih grammar Prism: php / markup / none (pseudo, teks polos)."""
    if 'background:#fff' in attrs and re.search(r'\b(PROGRAM|DEKLARASI)\b', body):
        return 'none'  # pseudocode Indonesia: tanpa grammar, blok tetap polos
    if re.search(r'&lt;\s*/?\s*(form|input|label|button|html|div|select)\b', body, re.I):
        return 'markup'
    if '<?php' in body or re.search(r'\$|echo\s|function\s+\w+\s*\(', body):
        return 'php'
    if re.search(r'\b(SELECT|INSERT|UPDATE|DELETE|CREATE TABLE|WHERE)\b', body, re.I):
        return 'sql'
    return 'none'


def patch(path):
    src = open(path, encoding='utf-8').read()
    if 'prismjs@1.29.0' in src:
        return 'skip (sudah ada Prism)'

    k = src.index('\n<script>')  # isi deck ada sebelum script inline
    content, script = src[:k], src[k:]
    if '<pre' not in content:
        return 'skip (tanpa blok kode)'

    # 1. head: 7 baris CDN sebelum <style> deck
    i = content.index('<style>')
    content = content[:i] + CDN + content[i:]

    # 2. CSS: pre relatif + override Prism (tema Prism kalah spesifisitas)
    if PRE_OLD not in content:
        raise SystemExit(path + ': aturan pre tidak ketemu')
    content = content.replace(PRE_OLD, PRE_NEW + PRISM_CSS, 1)

    # 3. JS: tombol Salin di awal <script> inline
    script = '\n<script>\n' + PRISM_JS + script[len('\n<script>'):]

    # 4. markup: bungkus isi <pre> dengan <code class="language-x">
    n = [0]

    def repl(m):
        attrs, inner = m.group(1), m.group(2)
        if '<code' in inner:
            return m.group(0)
        n[0] += 1
        return '<pre%s><code class="language-%s">%s</code></pre>' % (attrs, lang_for(attrs, inner), inner)

    content = re.sub(r'<pre([^>]*)>(.*?)</pre>', repl, content, flags=re.S)

    open(path, 'w', encoding='utf-8').write(content + script)
    return 'ok %d blok' % n[0]


if __name__ == '__main__':
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    for f in sorted(glob.glob(os.path.join(root, 'p*', 'index.html'))):
        code = os.path.basename(os.path.dirname(f))
        print('%-38s %s' % (code, patch(f)))
