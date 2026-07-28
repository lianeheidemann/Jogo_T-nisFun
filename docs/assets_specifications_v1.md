# Asset Specification - TênisFun

> Guia técnico e visual para criação, exportação e integração dos assets do jogo **TênisFun**.

## 1. Informações do projeto

| Campo | Especificação |
|---|---|
| Plataforma | Windows |
| Linguagem | Python |
| Biblioteca | Pygame |
| Resolução-base | 1280 x 720 px |
| Orientação | Horizontal |
| Janela | Tamanho fixo |
| Estilo | Ilustração 2D cartoon retrô moderna |
| Formato principal | PNG |

## 2. Direção visual global

### Estilo visual

Ilustração 2D cartoon retrô moderna, divertida e amigável, inspirada na estética de videogames portáteis clássicos reinterpretada com acabamento contemporâneo. Utilizar formas arredondadas, volumes simplificados, proporções levemente exageradas e aparência desenhada à mão. O conjunto deve parecer parte de um jogo casual alegre, coeso e profissional.

### Traços e contornos

- Contornos externos grossos, arredondados e bem definidos.
- Cor principal dos contornos: `#32152E`.
- Evitar preto puro.
- Linhas internas mais finas e orgânicas.
- Curvas suaves, pontas arredondadas e pequenas irregularidades controladas.

### Paleta oficial

| Cor | Hex | Aplicações sugeridas |
|---|---|---|
| Contorno escuro | `#32152E` | Contornos, divisões e sombras profundas |
| Azul-turquesa | `#69BFC3` | Interface, detalhes e céu |
| Azul profundo | `#3E7180` | Painéis, sombras e áreas secundárias |
| Verde-menta | `#91CFA7` | Quadra, roupa do jogador e botões |
| Verde claro | `#B9DEB5` | Luzes, vegetação e variações claras |
| Amarelo quente | `#FFD475` | Bola, raquete, estrela e destaques |
| Amarelo-creme | `#FFE6A2` | Fundos claros e brilhos |
| Coral | `#F4775E` | Roupa da oponente e estados de alerta |
| Laranja suave | `#F69A5B` | Detalhes e luzes quentes |
| Branco quente | `#F7F2E8` | Textos, roupas e áreas claras |

Podem ser usadas variações derivadas da paleta para luz e sombra, desde que permaneçam visualmente coerentes.

### Sombreamento e iluminação

- Cel shading suave com 2 ou 3 tonalidades por área.
- Luz principal vindo da parte superior esquerda.
- Sombras arredondadas e bem delimitadas.
- Pequenos brilhos curvos para reforçar volume.
- Sem realismo fotográfico.

### Composição padrão

Para assets isolados:

- Elemento totalmente visível e centralizado.
- Aproximadamente 10% de margem transparente ao redor.
- Silhueta clara e reconhecível em escala reduzida.
- Sem cortes, cenário, moldura ou objetos extras, salvo indicação específica.

## 3. Padrões técnicos

- Assets isolados em PNG com fundo transparente.
- Plano de fundo da quadra em PNG opaco.
- Bordas nítidas e sem artefatos.
- Sem marcas-d'água.
- Sem texto embutido, exceto no logo.
- Textos de botões, HUDs e tela final serão renderizados pelo código.
- Criar preferencialmente em 2x o tamanho de exibição e reduzir com `pygame.transform.smoothscale`.

### Pontos de ancoragem

| Asset | Âncora recomendada |
|---|---|
| Personagens | Centro inferior (`midbottom`) |
| Bola | Centro |
| Botões | Centro |
| HUDs | Centro |
| Rede | Centro |
| Logo | Centro |

## 4. Resumo dos 12 assets

| # | Asset | Exibição no jogo | Arquivo recomendado | Fundo |
|---:|---|---:|---:|---|
| 1 | Logo | 420 x 150 px | 840 x 300 px | Transparente |
| 2 | Plano de fundo da quadra | 1280 x 720 px | 1920 x 1080 px | Opaco |
| 3 | Jogador | 160 x 210 px por frame | 320 x 420 px por frame | Transparente |
| 4 | Oponente | 112 x 147 px por frame | 320 x 420 px por frame | Transparente |
| 5 | Bola de tênis | 28 x 28 px | 128 x 128 px | Transparente |
| 6 | Rede da quadra | 1040 x 96 px | 2080 x 192 px | Transparente |
| 7 | Botão principal | 300 x 84 px | 600 x 168 px | Transparente |
| 8 | Botão secundário | 280 x 72 px | 560 x 144 px | Transparente |
| 9 | HUD de pontos | 180 x 64 px | 360 x 128 px | Transparente |
| 10 | HUD de velocidade | 180 x 64 px | 360 x 128 px | Transparente |
| 11 | Painel de mensagem final | 460 x 440 px | 920 x 880 px | Transparente |
| 12 | Ícone de pausa | 80 x 80 px | 160 x 160 px | Transparente |

## 5. Especificação detalhada

### 5.1 Logo

**Arquivo:** `assets/logo/logo_tenisfun.png`

- Logo final com o texto **TênisFun** integrado à arte.
- Letras grandes, amigáveis, volumosas e legíveis.
- Contorno grosso em `#32152E`.
- Combinação de amarelo quente, azul-turquesa e branco quente.
- Pode incluir uma bola de tênis estilizada como detalhe.
- Fundo transparente e sem cenário.

### 5.2 Plano de fundo da quadra

**Arquivo:** `assets/backgrounds/court_background.png`

- Perspectiva longitudinal levemente elevada.
- Câmera centralizada atrás do jogador, voltada para a oponente.
- Incluir quadra, áreas laterais, cercas, árvores, arbustos, céu e natureza ao redor.
- Reservar boa leitura no topo para os HUDs e o botão de pausa.
- Não incluir rede, personagens, bola, textos ou interface.

### 5.3 Jogador

**Pasta:** `assets/characters/player/`

- Personagem masculino visto de costas, na parte inferior da quadra.
- Cabelo castanho.
- Camiseta verde-menta `#91CFA7`.
- Short cinza-azulado derivado de `#3E7180` e `#F7F2E8`.
- Tênis `#F7F2E8` com detalhes `#69BFC3`.
- Raquete `#FFD475`, com detalhes `#F69A5B` e contorno `#32152E`.
- Todos os frames devem manter o mesmo ponto de apoio nos pés.

#### Arquivos de animação

| Arquivo | Frames | Dimensão total |
|---|---:|---:|
| `player_idle.png` | 1 | 320 x 420 px |
| `player_move_left.png` | 2 | 640 x 420 px |
| `player_move_right.png` | 2 | 640 x 420 px |
| `player_hit.png` | 3 | 960 x 420 px |
| `player_victory.png` | 3 | 960 x 420 px |

### 5.4 Oponente

**Pasta:** `assets/characters/opponent/`

- Personagem feminina vista de frente, na parte superior da quadra.
- Blusa sem manga em branco quente `#F7F2E8`.
- Saia rosa derivada de `#F4775E`.
- Detalhes esportivos em `#69BFC3`, `#FFD475` ou `#F69A5B`.
- Mesma lógica de iluminação, proporção e animação do jogador.

#### Arquivos de animação

| Arquivo | Frames | Dimensão total |
|---|---:|---:|
| `opponent_idle.png` | 1 | 320 x 420 px |
| `opponent_move_left.png` | 2 | 640 x 420 px |
| `opponent_move_right.png` | 2 | 640 x 420 px |
| `opponent_hit.png` | 3 | 960 x 420 px |
| `opponent_victory.png` | 3 | 960 x 420 px |

### 5.5 Bola de tênis

**Arquivo:** `assets/objects/tennis_ball.png`

- Bola cartoon com leitura clara em 28 x 28 px.
- Base em amarelo quente com leve tendência esverdeada.
- Contorno em `#32152E` e brilho superior esquerdo.
- Sem sombra externa exagerada.

### 5.6 Rede da quadra

**Arquivo:** `assets/objects/court_net.png`

- Asset horizontal separado do fundo.
- Postes laterais incluídos.
- Malha simplificada, legível e compatível com a perspectiva.
- Fundo transparente.

### 5.7 Botão principal

**Arquivo:** `assets/ui/button_primary.png`

- Usado para ações principais, como Jogar e Jogar novamente.
- Formato grande, arredondado e convidativo.
- Área central vazia para texto e ícones inseridos pelo código.
- Cor-base sugerida: verde-menta.
- O código poderá alterar a cor conforme o estado.

### 5.8 Botão secundário

**Arquivo:** `assets/ui/button_secondary.png`

- Usado para Instruções, Sair e Voltar ao início.
- Mesma família visual do botão principal, porém menos chamativo.
- Área central vazia.
- Cor-base sugerida: azul-turquesa ou azul profundo.
- O código poderá alterar cor e texto conforme a função.

### 5.9 HUD de pontos

**Arquivo:** `assets/ui/hud_score.png`

- Painel horizontal com cantos arredondados.
- Ícone fixo de estrela à esquerda.
- Área livre para o número renderizado pelo código.
- Fundo em azul profundo ou azul-turquesa.
- Estrela em amarelo quente ou amarelo-creme.

### 5.10 HUD de velocidade

**Arquivo:** `assets/ui/hud_speed.png`

- Painel horizontal da mesma família do HUD de pontos.
- Ícone fixo de velocímetro à esquerda.
- Área livre para o número renderizado pelo código.
- Detalhes em branco quente, coral ou amarelo.

### 5.11 Painel de mensagem final

**Arquivo:** `assets/ui/final_panel.png`

- Painel central comemorativo com bordas arredondadas.
- Troféu decorativo fixo no topo.
- Áreas livres para título, pontuação e mensagem inseridos pelo código.
- Botões adicionados separadamente.
- Base clara em branco quente ou amarelo-creme.

### 5.12 Ícone de pausa

**Arquivo:** `assets/ui/icon_pause.png`

- Ícone circular com símbolo de pausa integrado.
- Base em azul profundo.
- Símbolo em branco quente.
- Contorno em `#32152E`.
- Deve permanecer legível em 80 x 80 px.

## 6. Animações dos personagens

Cada personagem possui 11 frames distribuídos em 5 arquivos:

| Animação | Frames | Descrição |
|---|---:|---|
| Idle | 1 | Posição de espera, joelhos levemente flexionados e raquete pronta |
| Movimento para esquerda | 2 | Deslocamento lateral com leitura clara do passo |
| Movimento para direita | 2 | Movimento equivalente no sentido oposto |
| Rebatida | 3 | Preparação, contato e finalização |
| Vitória | 3 | Impulso, salto e comemoração com mãos e raquete erguidas |

## 7. Estrutura de pastas

```text
assets/
├── backgrounds/
│   └── court_background.png
├── logo/
│   └── logo_tenisfun.png
├── characters/
│   ├── player/
│   │   ├── player_idle.png
│   │   ├── player_move_left.png
│   │   ├── player_move_right.png
│   │   ├── player_hit.png
│   │   └── player_victory.png
│   └── opponent/
│       ├── opponent_idle.png
│       ├── opponent_move_left.png
│       ├── opponent_move_right.png
│       ├── opponent_hit.png
│       └── opponent_victory.png
├── objects/
│   ├── tennis_ball.png
│   └── court_net.png
└── ui/
    ├── button_primary.png
    ├── button_secondary.png
    ├── hud_score.png
    ├── hud_speed.png
    ├── final_panel.png
    └── icon_pause.png
```

## 8. Prompt mestre de estilo

```text
Crie um asset para o jogo TênisFun.

ESTILO VISUAL:
Ilustração 2D cartoon retrô moderna, divertida e amigável, inspirada na estética de videogames portáteis clássicos reinterpretada com acabamento contemporâneo. Formas arredondadas, volumes simplificados, proporções levemente exageradas e aparência desenhada à mão.

TRAÇOS E CONTORNOS:
Contornos externos grossos, arredondados e bem definidos em #32152E, evitando preto puro. Linhas internas mais finas, curvas suaves e pequenas irregularidades controladas.

PALETA:
#32152E, #69BFC3, #3E7180, #91CFA7, #B9DEB5, #FFD475, #FFE6A2, #F4775E, #F69A5B e #F7F2E8.

SOMBREAMENTO:
Cel shading suave com duas a três tonalidades por área. Luz principal vindo da parte superior esquerda. Sombras arredondadas e pequenos brilhos curvos.

COMPOSIÇÃO:
Elemento totalmente visível, centralizado, sem cortes e com aproximadamente 10% de margem livre ao redor. Silhueta clara e reconhecível.

REQUISITOS TÉCNICOS:
Imagem limpa, alta resolução, PNG, fundo transparente, bordas nítidas, sem marcas-d'água, sem moldura, sem letras e sem texto, salvo quando especificado.
```

## 9. Convenções de nomes

- Usar letras minúsculas.
- Não usar espaços ou acentos.
- Separar palavras com underscore.
- Manter nomes em inglês para facilitar a integração com o código.

## 10. Checklist de aprovação

- [ ] Dimensão e proporção corretas.
- [ ] Fundo transparente quando exigido.
- [ ] Contorno em `#32152E`.
- [ ] Iluminação superior esquerda.
- [ ] Paleta compatível com o guia.
- [ ] Boa leitura no tamanho real de exibição.
- [ ] Elemento sem cortes e com margem segura.
- [ ] Ausência de texto indevido e marcas-d'água.
- [ ] Ponto de ancoragem consistente.
- [ ] Animações alinhadas quadro a quadro.
