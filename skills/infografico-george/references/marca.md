# Regras da marca George Ricardo

Identidade construída a partir do manual "Identidade George Ricardo" e refinada com o próprio George ao longo de 9 infográficos. Cada regra traz o motivo, para que você saiba aplicar o espírito dela em casos novos.

## Essência

**Full Marketing Ops** é o marketing que opera de ponta a ponta: estratégia, dados e execução conectados. O sinal da marca é o **ponto luminoso** no fim do nome, "a operação ativa, o dado que acende". Por isso, na linguagem visual, **luz é significado**: o que acende é o que importa.

## Cores

Use as variáveis de `marca.css`, nunca hex soltos fora desta lista.

| Token | Hex | Uso |
|---|---|---|
| `--preto` | #000000 | Fundo base (cerca de 50% da peça) |
| `--noite` | #0A1628 | Superfícies, cards escuros |
| `--oceano` | #0E4A7E | Profundidade, estados intermediários |
| `--azul-sinal` | #1E7BD6 | Destaque (cerca de 10%): números dos cards, pílula do título, o "certo" |
| `--gelo` | #A9D3F5 | Luz, palavras-chave, linhas de diagrama |
| `--branco` | #FFFFFF | Texto principal e o ponto de luz |
| `--brilho` | #6FB6F5 | Só no `box-shadow` / `drop-shadow` dos brilhos |
| textos de apoio | `--texto-suave` #C9D4E0, `--texto-medio` #9AA7B6, `--texto-apagado` #8090A3 | Hierarquia de texto |

Gradientes da marca: **Horizonte** (brilho azul que nasce de baixo, usado no fundo das peças), **Feixe** (luz num canto) e **Gelo** (peças claras, como o post Dado claro).

**Nada de vermelho, verde ou amarelo**, mesmo quando a referência usa. Esse contraste de semáforo é o vocabulário de outros criadores. O de George é **apagado → aceso**:
- ruim, comum, superficial, "o que a maioria faz" → fundo `rgba(255,255,255,.03)`, texto `--texto-apagado`, bordas fracas;
- intermediário → `--oceano` translúcido;
- certo, valioso, profundo, "onde está o dinheiro" → Azul Sinal ou gradiente azul, borda Gelo, `box-shadow` com `--brilho`, texto branco.

Nas peças de profundidade (níveis, funil), a luz cresce rumo ao ponto mais importante.

## Tipografia

Uma família só: **Helvetica Neue** (com Helvetica e Arial de reserva).
- **Título:** Light 300, de 56 a 76 px, `letter-spacing` de −0.04 a −0.045em, com o gradiente vertical branco → #8A9BB0 (`.ig-title.gradient-text`). No máximo 2 linhas.
- **Destaque no título:** uma palavra ou expressão curta na pílula `.lv-highlight` (Azul Sinal com brilho). Use uma por peça; duas competem.
- **Título de card:** Regular 400, de 21 a 27 px, −0.02em.
- **Corpo:** 15–24 px, conforme a densidade, com cor `--texto-suave` ou `--texto-medio`. Negrito (500) em branco ou Gelo para a palavra que carrega o sentido.
- **Tags e chips:** de 11 a 17 px. Nada abaixo de 10 px; abaixo disso, ninguém lê nem com zoom.

## Estrutura de toda peça

- **Tamanho:** 1080×1350 (`<article class="post ...">` com `id` único, que vira o nome do PNG).
- **Textura:** a primeira coisa dentro do article é `<svg class="grain">`, que dá o grão de filme da identidade.
- **Infográficos sem cabeçalho:** nada de nome nem etiqueta nos cantos de cima; a peça começa direto no título. Decisão do George: o rodapé já assina.
- **Rodapé obrigatório nos infográficos** (`.ig-footer`): foto `george-avatar.jpg` **sem efeito de cor**, depois **George Ricardo** / **@georgeric_**, um divisor e a chamada.
  - Chamada preferida: uma pergunta que puxe o leitor para o tema ("Onde o marketing está sentado na **sua** empresa?"). Pergunta gera comentário; "salve" é passivo.
  - Reserva: "**Salve** e **compartilhe** com quem precisa."
  - Em peças de diagnóstico, sugira a George uma chamada comercial ("Seu problema está em qual nível? Me chama no direct"), porque esse conteúdo vende o serviço dele.
- **Os modelos de post do manual** (`post-01` a `post-06`) ainda usam o nome no topo e a etiqueta de série ("Frase 01"). George não decidiu se a regra dos infográficos vale também para eles. Na primeira vez que usar um post, pergunte.
- **Cards** são de vidro: gradiente branco de .075 → .025, borda branca de .12, raio de 22 a 26 px. Os números dos cards vão em círculo Azul Sinal com brilho.
- **Selos de alerta** ("A maioria das empresas para aqui") têm borda tracejada branca e um × num círculo branco (`.ig-badge-x`). É um componente recorrente da série; reaproveite.

## Voz e conteúdo

- **Português do Brasil, direto**, como quem fala com diretoria. Frase curta, verbo forte, sem jargão vazio.
- **Reescreva, não traduza.** Referências de outros criadores (Pierre Herubel e outros) servem para estrutura e formato. O texto final precisa ser do George, com exemplos e falas que soem a reunião brasileira ("A gente decide isso depois.").
- **Termos em inglês:** mantenha os que o mercado usa assim (ICP, CAC, LTV, USP, Champion, Job to be Done, frameworks com nome próprio). Quando houver equivalente natural para executivos brasileiros, prefira o português (Precificação em vez de Pricing) e avise George.
- **Números:** nunca invente número como fato. Exemplo de layout fica marcado como ilustrativo. Dado real pede a linha "Fonte: …" na peça. Se George não deu a fonte, peça, porque um perfil de Ops e dados não pode publicar estatística solta.
- **Posicionamento:** "Ops" nunca aparece como o degrau operacional mais baixo (escrever copy, subir anúncio). Se uma referência fizer isso, renomeie (por exemplo, para "Execução") e explique o motivo.
- **Seja crítico.** George pediu explicitamente um parceiro estratégico. Na entrega, aponte com franqueza: excesso de densidade para o celular, formato saturado no LinkedIn, mensagem que pode ser mal lida, oportunidade de série ou carrossel.
