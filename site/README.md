# George Ricardo — Identidade visual

Manual de identidade (capa, logotipo, paleta, tipografia) e 6 modelos de post 1080×1350, implementados em HTML/CSS estático a partir do design em `project/Identidade George Ricardo.dc.html`.

## Ver o manual

Abra `site/index.html` no navegador. O canvas original tem 3480 px e é reduzido para caber na janela. Os controles no canto inferior direito ligam/desligam a textura granulada e alternam a foto entre duotone azul e cores originais.

## Infográficos

`site/infograficos.html` reúne os infográficos 1080×1350 (01 a 09: glossário, painel, níveis, tabela de níveis, funil, cadeia de causa, comparação, grade de princípios e matriz 2×2). Cada um é um `<article class="post">` com estilos em `site/infograficos.css`, e sai na mesma exportação dos posts.

## Exportar os posts em PNG

```bash
npm install
npm run export                         # export/post-0N.png, infografico-0N.png e manual-identidade.png
npm run export:sem-textura             # sem textura granulada
node scripts/export-posts.mjs --photo=original
```

Instale a Helvetica Neue na máquina antes de exportar; sem ela o navegador usa Helvetica ou Arial.

## Editar os textos

Cada post é um `<article class="post" id="post-0N">` em `site/index.html`. Troque os textos ali e exporte de novo. Os dados dos posts 02 e 05 ("3x", "−40%") e as linhas "Fonte" são exemplos. Substitua pelos seus números reais antes de publicar.

Cores e gradientes ficam como variáveis no topo de `site/styles.css`.
