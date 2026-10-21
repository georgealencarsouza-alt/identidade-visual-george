#!/usr/bin/env python3
"""Renderiza cada <article class="post"> de um HTML em PNG 1080x1350.

    python scripts/render.py caminho/peca.html [--out pasta]

Copia marca.css e as fotos da skill para a pasta do HTML (se faltarem),
abre a página num Chromium headless e salva <id>.png para cada peça.
Usa o Playwright do Python; se não houver, tenta o Playwright do Node.
Ao final, imprime um aviso para cada elemento que estoura a peça ou o
próprio card (texto cortado é o defeito mais comum).
"""
import json, os, shutil, subprocess, sys, tempfile
from pathlib import Path

SKILL = Path(__file__).resolve().parent.parent
ASSETS = ['marca.css', 'george-ricardo.jpg', 'george-avatar.jpg']

# Procura elementos cortados: conteúdo maior que a caixa com overflow escondido,
# ou que passa da borda da peça.
CHECK_JS = r"""
(post) => {
  const out = [];
  const box = post.getBoundingClientRect();
  for (const el of post.querySelectorAll('*')) {
    if (el.closest('svg') && el.tagName !== 'svg') continue;
    const r = el.getBoundingClientRect();
    if (!r.width || !r.height) continue;
    const name = el.className && el.className.baseVal === undefined ? el.className : el.tagName;
    const cs = getComputedStyle(el);
    if (cs.overflow === 'hidden' && el.scrollHeight > el.clientHeight + 2 && !el.classList.contains('post'))
      out.push(`conteúdo cortado em .${String(name).split(' ')[0]} (${el.scrollHeight - el.clientHeight}px a mais)`);
    if (r.bottom > box.bottom + 1 || r.right > box.right + 1)
      if (!el.closest('.grain, [class*="ring"], [class*="beam"], [class*="ray"], .b2b-audience, .pr-diagram'))
        out.push(`.${String(name).split(' ')[0]} passa da borda da peça`);
  }
  return [...new Set(out)].slice(0, 12);
}
"""

NODE_SCRIPT = r"""
const { chromium } = require('playwright');
const [url, outDir, checkJs] = process.argv.slice(2);
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1200, height: 1400 } });
  await p.goto(url, { waitUntil: 'load' });
  await p.evaluate(() => document.fonts.ready);
  const res = [];
  for (const el of await p.$$('article.post')) {
    const id = await el.getAttribute('id');
    await el.screenshot({ path: `${outDir}/${id}.png` });
    res.push({ id, warnings: await el.evaluate(eval(checkJs)) });
  }
  console.log(JSON.stringify(res));
  await b.close();
})();
"""


def render_python(url, out_dir):
    from playwright.sync_api import sync_playwright
    res = []
    with sync_playwright() as pw:
        b = pw.chromium.launch()
        p = b.new_page(viewport={'width': 1200, 'height': 1400})
        p.goto(url, wait_until='load')
        p.evaluate('document.fonts.ready')
        for el in p.query_selector_all('article.post'):
            id_ = el.get_attribute('id')
            el.screenshot(path=str(out_dir / f'{id_}.png'))
            res.append({'id': id_, 'warnings': el.evaluate(CHECK_JS)})
        b.close()
    return res


def render_node(url, out_dir):
    with tempfile.NamedTemporaryFile('w', suffix='.cjs', delete=False) as f:
        f.write(NODE_SCRIPT)
    env = dict(os.environ)
    try:
        root = subprocess.run(['npm', 'root', '-g'], capture_output=True, text=True).stdout.strip()
        env['NODE_PATH'] = os.pathsep.join(filter(None, [env.get('NODE_PATH'), root]))
    except FileNotFoundError:
        pass
    r = subprocess.run(['node', f.name, url, str(out_dir), CHECK_JS], capture_output=True, text=True, env=env)
    if r.returncode != 0:
        raise RuntimeError(r.stderr.strip()[-600:])
    return json.loads(r.stdout.strip().splitlines()[-1])


def main():
    args = sys.argv[1:]
    if not args:
        sys.exit(__doc__)
    html = Path(args[0]).resolve()
    out_dir = Path(args[args.index('--out') + 1]).resolve() if '--out' in args else html.parent
    out_dir.mkdir(parents=True, exist_ok=True)
    for name in ASSETS:
        if not (html.parent / name).exists():
            shutil.copy(SKILL / 'assets' / name, html.parent / name)

    url = html.as_uri()
    try:
        res = render_python(url, out_dir)
    except ImportError:
        try:
            res = render_node(url, out_dir)
        except Exception as e:
            sys.exit('Não encontrei o Playwright. Instale com:\n'
                     '  pip install playwright && playwright install chromium\n'
                     f'(detalhe: {e})\nSe não for possível, entregue o HTML: ele abre em qualquer navegador.')

    for r in res:
        print(f"✓ {out_dir / (r['id'] + '.png')}")
        for w in r['warnings']:
            print(f"  ⚠ {w}")


if __name__ == '__main__':
    main()
