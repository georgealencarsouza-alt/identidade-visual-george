// Exporta posts e infográficos em PNG 1080×1350, além do manual completo.
//
//   node scripts/export-posts.mjs [--no-grain] [--photo=original] [--out=export]
//
// Requer Playwright (npm i -D playwright). A Helvetica Neue precisa estar
// instalada na máquina; sem ela o navegador usa Helvetica ou Arial.
import { chromium } from 'playwright';
import { mkdir } from 'node:fs/promises';
import { fileURLToPath, pathToFileURL } from 'node:url';
import path from 'node:path';

const root = path.dirname(path.dirname(fileURLToPath(import.meta.url)));
const args = process.argv.slice(2);
const flag = (name) => args.find((a) => a.startsWith(`--${name}`));

const outDir = path.resolve(root, flag('out')?.split('=')[1] ?? 'export');
const query = new URLSearchParams({ export: '1' });
if (flag('no-grain')) query.set('grain', '0');
if (flag('photo')?.split('=')[1] === 'original') query.set('photo', 'original');

const pages = ['index.html', 'infograficos.html'];
const urlFor = (page) => `${pathToFileURL(path.join(root, 'site', page)).href}?${query}`;

await mkdir(outDir, { recursive: true });

const browser = await chromium.launch(
  process.env.PLAYWRIGHT_CHROMIUM_PATH ? { executablePath: process.env.PLAYWRIGHT_CHROMIUM_PATH } : {},
);
const page = await browser.newPage({ viewport: { width: 3480, height: 1400 }, deviceScaleFactor: 1 });
for (const name of pages) {
  await page.goto(urlFor(name), { waitUntil: 'load' });
  await page.evaluate(() => document.fonts.ready);

  for (const post of await page.$$('article.post')) {
    const id = await post.getAttribute('id');
    const file = path.join(outDir, `${id}.png`);
    await post.screenshot({ path: file });
    console.log(`✓ ${path.relative(root, file)}`);
  }
}

await page.goto(urlFor('index.html'), { waitUntil: 'load' });
const manual = path.join(outDir, 'manual-identidade.png');
await page.locator('#canvas').screenshot({ path: manual });
console.log(`✓ ${path.relative(root, manual)}`);

await browser.close();
