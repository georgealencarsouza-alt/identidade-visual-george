# Catálogo de formatos

Cada formato tem um exemplo completo em `assets/exemplos/<id>.html`. Comece copiando o exemplo e trocando o conteúdo: as classes já estão afinadas para caber em 1080×1350. Os limites abaixo foram medidos nas peças reais; passar deles quase sempre corta texto ou deixa a peça ilegível no celular.

Medida útil: no feed, 1080 px viram cerca de 390 pt. Texto de 15 px aparece com uns 5–6 pt, e só funciona em peça feita para salvar e ampliar. Quando o objetivo for alcance, prefira menos itens e fonte maior.

## Índice
- Posts (peça única): Frase, Dado, Lista, Foto, Dado claro, Feixe
- Infográficos: 01 Grade de termos · 02 Painel modular · 03 Níveis · 04 Tabela de níveis · 05 Funil · 06 Cadeia de causa · 07 Comparação · 08 Grade de princípios · 09 Matriz 2×2
- Quando nada serve: série, carrossel ou formato novo

---

## Posts

Estes modelos vêm do manual e ainda têm nome e etiqueta no topo ("Frase 01"). Pergunte ao George se a regra dos infográficos (sem topo, rodapé com foto e @) vale para eles antes de entregar.

| id | Uso | Limites |
|---|---|---|
| `post-01` Frase | Uma frase de efeito com assinatura | Frase ≤ 60 caracteres (120 px, até 4 linhas) |
| `post-02` Dado | Número grande + o que ele significa, com uma curva subindo | Número ≤ 4 caracteres ("3x", "72%"); frase ≤ 80; **fonte obrigatória** |
| `post-03` Lista | Título + 3–5 pílulas em zigue-zague | Título ≤ 45; pílula ≤ 30 |
| `post-04` Foto | Apresentação do George, com foto em duotone | Card de vidro: título ≤ 25, texto ≤ 70 |
| `post-05` Dado claro | Versão clara do Dado (gradiente Gelo), para variar o feed | Número ≤ 5 caracteres; frase ≤ 70; fonte |
| `post-06` Feixe | Uma dica: afirmação + explicação curta | Afirmação ≤ 90; apoio ≤ 80 |

---

## 01 Grade de termos — `infografico-01`
**Quando:** de 9 a 15 itens paralelos (termos, métricas, ferramentas, erros), cada um explicável em uma linha.
**Estrutura:** título em 2 linhas → grade 3×5 de `.ig-card` (número, título, texto e mini visual) → rodapé.
- Corpo lateral (`.ig-card__body`): texto à esquerda, visual de 118 px à direita. Texto ≤ 55 caracteres.
- Corpo empilhado (`.ig-card__body--stack`): texto e visual em largura total, para fórmulas, gráficos de linha e calendários. Texto ≤ 70 caracteres.
- Título do card ≤ 20 caracteres, para caber em uma linha. Use a sigla como título ("CAC") e o nome por extenso na definição.
- Cada card precisa de um mini visual (barras, rosca, tabela A/B, chips, ícones). Sem visual, vira lista de texto. As classes `.ig-*` cobrem os casos comuns.
- Com menos de 12 itens, mude o `grid-template-rows` (`repeat(4, …)`) ou use a Grade de princípios.

## 02 Painel modular — `infografico-02`
**Quando:** de 4 a 6 conceitos com pesos diferentes, em que alguns pedem um diagrama próprio (proporção, fluxo, funil interno).
**Estrutura:** linhas `.b2b-row` com grades próprias (`1fr 1fr`, `1.62fr 1fr`) e cards `.ig-card--lg`. Um card grande pode carregar um framework inteiro.
- Texto de card ≤ 120 caracteres; título ≤ 26.
- É o formato mais trabalhoso, porque cada card é desenhado à mão. Só use quando os itens não forem paralelos; se forem, uma grade resolve.
- Diagramas: círculos concêntricos (público), canais convergindo (influência), funil em faixas com notas laterais, rosca de proporção.

## 03 Níveis — `infografico-03`
**Quando:** 3 camadas de profundidade (superfície → estratégico → raiz), em que o leitor descobre que o problema real está embaixo.
**Estrutura:** título com pílula → 3 blocos `.lv` (fala típica e ícone à esquerda; 3 afirmações tracejadas à direita; rótulo do nível com linha) → rodapé. Um feixe de luz `.lv-beam` se abre e acende para baixo.
- Afirmação ≤ 45 caracteres, com a palavra-chave em `<b>`.
- A fala típica é uma frase de reunião (≤ 35 caracteres), entre aspas.
- A intensidade cresce do `.lv--1` ao `.lv--3`. Não inverta: a raiz é o que acende.

## 04 Tabela de níveis — `infografico-04`
**Quando:** 3 níveis que repetem as mesmas dimensões (por exemplo, Empresa / Pessoa / Como acessar), com itens curtos em cada uma.
**Estrutura:** `.icp` com 3 `.icp-level` separados por tracejado → cada nível com cabeçalho (`Nível N` + frase), linhas `.icp-row` de tags e uma linha de ação com `.ig-label`.
- Até 5 tags por linha, cada uma com ≤ 20 caracteres.
- O selo `.icp-stop` ("A maioria para aqui") marca o nível onde o mercado se acomoda.

## 05 Funil — `infografico-05`
**Quando:** 4 etapas hierárquicas que afunilam (estratégia de negócio → estratégia de marketing → táticas → execução), muitas vezes com retorno (feedback) de baixo para cima.
**Estrutura:** `.fn` com um trapézio SVG atrás (`.fn__shape`) e uma sobreposição (`.fn__overlay`) com o eixo vertical e a seta tracejada de feedback → 4 `.fn-band` (rótulo, descrição e tags).
- Descrição ≤ 60 caracteres (1 linha). Tags: 4–5 por faixa.
- A faixa de baixo é estreita: no máximo 5 tags curtas, e `max-width` já limita a 470 px.
- As coordenadas do feedback e do eixo estão em pixels no SVG da sobreposição. Ao mudar o número de faixas, recalcule e confira no PNG.
- O selo `.fn-start` ("A maioria começa aqui") marca o erro comum.

## 06 Cadeia de causa — `infografico-06`
**Quando:** um encadeamento em que cada etapa causa a seguinte, da raiz emocional ou estratégica até um resultado ruim (ou bom).
**Estrutura:** `.chain-root` (causa-raiz, com selo "O problema começa aqui") → 3–5 `.chain-step` ligados por `.chain-link` → linha opcional `.chain-line` ("O mercado só enxerga daqui para baixo") → `.chain-result` aceso.
- Cada etapa tem um rótulo (≤ 30) e um texto ou fala (≤ 65, em uma linha).
- O que o mercado não vê fica apagado; o que fica visível ganha `.chain-step--visible`.

## 07 Comparação — `infografico-07`
**Quando:** dois lados contrastados em pares (X vs. Y, antes/depois, amador/profissional), mais um desfecho para cada lado.
**Estrutura:** `.vs` com duas colunas: cabeçalhos (fraco / forte), selo `vs` no meio, 5–7 linhas de `.vs__cell--weak` / `.vs__cell--strong` e `.vs__outcome` com seta.
- Célula ≤ 40 caracteres. **Envolva o conteúdo da célula em `<span>`**, senão o flexbox come os espaços em volta do `<b>`.
- O lado bom é o aceso. O fraco fica apagado, mas legível: ninguém compara o que não consegue ler.
- Com mais de 7 pares, divida em duas peças.

## 08 Grade de princípios — `infografico-08`
**Quando:** de 6 a 9 princípios ou ideias em que cada um pede 2–3 linhas e um diagrama conceitual.
**Estrutura:** `.pr-grid` 3×3 (para 6 itens, use `grid-template-rows: repeat(2, …)`) com `.ig-card`: número, título, texto e `.pr-diagram` (SVG de 280×130).
- Texto ≤ 90 caracteres; título ≤ 22.
- Os diagramas usam os símbolos `#i-person` e `#i-building` (`<use href="#i-person" …>`), elipses de mercado, cones de luz e setas. Mantenha cada um simples: no máximo 3 elementos e rótulos de 11 px.

## 09 Matriz 2×2 — `infografico-09`
**Quando:** o texto cruza duas perguntas ou eixos (pouco → muito) e posiciona 4 situações.
**Estrutura:** título + subtítulo (`.ig-subtitle`) → `.mx` com eixo Y (rótulo girado, muito em cima e pouco embaixo), grade de 4 `.mx-q` e eixo X → rodapé com a pergunta.
- Em cada quadrante: título ≤ 22, descrição ≤ 60 e uma lista de chips (como "Mesa: …"), com até 7 chips curtos.
- **Ordem no HTML:** em cima à esquerda, em cima à direita, embaixo à esquerda, embaixo à direita.
- O quadrante mais valioso fica aceso (`.mx-q--market`), com selo branco ("Onde está o dinheiro"). O do erro comum leva o selo tracejado `.mx-badge--most`.
- Para destacar um ator dentro dos chips, use `.ig-tag--mkt` e, se precisar, a etiqueta interna `.mx-note`.

---

## Quando nada serve

- **Texto grande demais** para os limites: proponha uma **série** (duas ou três peças do mesmo formato, numeradas) ou um **carrossel**. O carrossel ainda não tem modelo aprovado. Monte cada lâmina como um `<article>` de 1080×1350 com os mesmos componentes (capa = título com pílula; lâminas = um bloco cada; última = rodapé com a pergunta) e avise George que é a primeira versão do formato.
- **Estrutura nova** (linha do tempo, ciclo, pirâmide…): combine os componentes existentes (cards de vidro, chips, selos, `.ig-label`, setas tracejadas, apagado → aceso) num `<article class="post post--ig">`. Avise que é um formato novo e sugira guardá-lo nos exemplos se ele aprovar.
