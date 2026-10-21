---
name: infografico-george
description: Transforma um texto do George Ricardo (Full Marketing Ops, @georgeric_) em peça visual pronta para Instagram/LinkedIn — infográfico ou post 1080×1350 na identidade visual dele (preto, azuis, Helvetica Neue, ponto luminoso) — escolhendo sozinho o melhor formato (grade, painel, níveis, funil, cadeia de causa, comparação, matriz 2×2, frase, dado, lista) e exportando PNG. Use sempre que George mandar um texto, roteiro, ideia, lista, framework ou referência de outro criador e pedir arte, post, infográfico, peça, carrossel, "transforma em imagem", "monta o visual", "faz no meu padrão", mesmo que não diga "infográfico".
---

# Infográficos e posts do George Ricardo

George é especialista em marketing ("Full Marketing Ops"). Ele escreve o conteúdo; esta skill decide **como mostrar** e entrega a peça pronta para publicar. A parte que ele mais valoriza é a escolha do formato e a revisão crítica: ele quer um parceiro estratégico, não alguém que só concorda.

## Fluxo

1. **Entender a estrutura do texto.** Antes de pensar em layout, responda: quantos itens existem? Eles são paralelos ou têm pesos diferentes? Existe hierarquia, sequência, causa e efeito, contraste ou dois eixos? Há números? A relação central que o leitor precisa enxergar é o que define o formato.
2. **Escolher o formato** pela tabela abaixo. Diga a escolha em uma linha, com o motivo e, se houver, a alternativa descartada ("Matriz 2×2, porque o texto cruza duas perguntas; uma comparação perderia o eixo da receita").
3. **Ajustar o texto aos limites do formato** (em `references/formatos.md`). Condense com a voz dele em vez de diminuir a fonte. Se não couber, proponha dividir em série ou carrossel; espremer é o erro mais comum.
4. **Montar o HTML.** Copie `assets/template.html` para uma pasta de trabalho e use como base o exemplo do formato em `assets/exemplos/` (cada arquivo é um `<article>` completo). Reaproveite as classes de `assets/marca.css`; visuais novos entram como SVG inline com as cores da marca. Para um layout novo, um `<style>` na página usando as variáveis de `:root` é melhor do que inventar cores.
5. **Renderizar e revisar.** Rode `python scripts/render.py <arquivo.html>`: ele gera `<id>.png` para cada `<article>` e avisa quando há texto cortado ou elemento fora da peça. Corrija os avisos e **abra o PNG para olhar**, porque o script não vê tudo (títulos que quebram feio, palavra sozinha na linha, visual desalinhado, hierarquia confusa). Itere até ficar limpo.
6. **Entregar** o PNG (e o HTML, se ele quiser editar) com uma revisão curta e honesta: dado sem fonte, número ilustrativo, risco de posicionamento, ponto fraco do argumento ou um formato melhor para alcance.

## Escolha do formato

| O texto tem… | Formato | Exemplo |
|---|---|---|
| Uma ideia ou frase de efeito | Post Frase | `post-01` |
| Um número forte com contexto | Post Dado (escuro) ou Dado claro | `post-02`, `post-05` |
| Uma dica com 3–5 itens curtos | Post Lista | `post-03` |
| Uma dica única com explicação curta | Post Feixe | `post-06` |
| Apresentação pessoal / sobre o George | Post com foto | `post-04` |
| 9–15 termos ou itens paralelos, uma linha cada | Grade de termos | `infografico-01` |
| 6–9 princípios com 2–3 linhas e um conceito visual cada | Grade de princípios | `infografico-08` |
| 4–6 conceitos de pesos diferentes, cada um com seu diagrama | Painel modular | `infografico-02` |
| Profundidade: sintoma → problema → causa-raiz | Níveis | `infografico-03` |
| Níveis que repetem as mesmas dimensões (empresa, pessoa, como acessar) | Tabela de níveis | `infografico-04` |
| Hierarquia que afunila (estratégia → execução), com feedback | Funil | `infografico-05` |
| Encadeamento causal: A leva a B, que leva a C, até um resultado | Cadeia de causa | `infografico-06` |
| Dois lados em pares (X vs. Y, antes/depois, errado/certo) | Comparação | `infografico-07` |
| Duas perguntas ou eixos que cruzam (pouco → muito) | Matriz 2×2 | `infografico-09` |

Quando dois formatos servirem, fique com o que torna visível a relação mais importante do texto. Os detalhes de cada formato (estrutura, limites de caracteres, armadilhas) estão em `references/formatos.md`; leia a seção do formato escolhido antes de montar.

## Regras da marca (resumo)

As regras completas, com o porquê de cada uma, estão em `references/marca.md`. Leia antes da primeira peça da conversa.

- **Peça 1080×1350.** Infográficos começam direto no título: sem nome nem etiqueta no topo.
- **Rodapé padrão:** foto sem nenhum efeito de cor, depois **George Ricardo** e **@georgeric_**, um divisor e a chamada. A chamada ideal é uma pergunta ligada ao tema, porque gera comentário. "**Salve** e **compartilhe** com quem precisa." é só a reserva.
- **Apagado → aceso:** contraste se faz com luz, nunca com vermelho ou verde. O que é ruim, comum ou superficial fica escuro; o que é certo, valioso ou profundo acende (Azul Sinal, Gelo, brilho).
- **Uma palavra-chave do título** pode ir na pílula Azul Sinal (`.lv-highlight`); o resto do título leva o gradiente branco → cinza.
- **Voz:** português do Brasil, frases curtas e diretas. Reescreva em vez de traduzir. Mantenha em inglês só os termos que o mercado usa assim (ICP, CAC, Champion).
- **Dados:** nunca invente número apresentado como fato. Número de exemplo fica marcado como ilustrativo, e todo dado real pede fonte na peça.
- **Posicionamento:** George vende Marketing Ops como a camada que liga estratégia, dados e execução. Nenhuma peça deve tratar "Ops" como tarefa operacional de baixo nível. Ao adaptar referências de outros criadores, procure esse tipo de armadilha.

## Ambiente

- `scripts/render.py` usa o Playwright (Python ou Node). Se não houver nenhum: `pip install playwright && playwright install chromium`. Se nada funcionar, entregue o HTML, que abre em qualquer navegador.
- A fonte é Helvetica Neue. Em máquinas sem ela, o navegador usa Arial, que é um pouco mais larga. Avise George quando o PNG sair com Arial e lembre que, no Mac dele, a fonte certa aparece.
- O script copia `marca.css` e as fotos para a pasta do HTML, então caminhos relativos (`george-avatar.jpg`, `george-ricardo.jpg`) funcionam.
