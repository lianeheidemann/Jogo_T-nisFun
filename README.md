<div align="center">

# 🎾 TÊNISFUN

### Jogo 2D em Python com Pygame

Simulação de tênis em perspectiva com foco em **transformações geométricas**

<p>
  <img src="https://github.com/user-attachments/assets/dd2a47f7-1201-4587-9e5c-4b2cf3e454d2" width="750">
</p>

</div>

---

## 📌 Sobre o Projeto

O **TênisFun** é um jogo desenvolvido para a disciplina de Computação Gráfica.

O objetivo é aplicar, na prática, conceitos fundamentais de transformação geométrica em um ambiente interativo usando Python e Pygame.

O jogador controla um atleta de tênis visto de costas e deve rebater bolas lançadas pelo oponente em uma quadra com perspectiva simulada.

---

## 🎯 Objetivo Acadêmico

Este projeto foi desenvolvido com foco em:

- Aplicação prática de **transformações geométricas**
- Desenvolvimento de jogos com gráficos 2D
- Organização modular de código
- Uso de eventos e interação com teclado

---

## 🧠 Transformações Geométricas Implementadas

### 📍 Translação
Movimento dos objetos na tela (jogador e bola):

```python
self.x += self.speed
self.y += self.speed_y
```

---

### 🔄 Rotação
A bola gira em torno do próprio eixo:

```python
pygame.transform.rotate(surface, angle)
```

---

### 📏 Escala
Simulação de profundidade (bola cresce ao se aproximar):

```python
pygame.transform.scale(surface, (w, h))
```

---

### 🔁 Reflexão (Flip)
A raquete muda de lado conforme posição do jogador:

```python
pygame.transform.flip(surface, True, False)
```

---

## 🎮 Gameplay

- A bola é lançada pelo adversário
- O jogador deve se mover para esquerda ou direita
- O objetivo é rebater corretamente por 10 rodadas
- A dificuldade aumenta progressivamente

---

## 🕹️ Controles

| Tecla | Ação |
|------|------|
| ← | Move o jogador para esquerda |
| → | Move o jogador para direita |

---

## 🧱 Estrutura do Projeto

```text
tenis_fun/
│
├── main.py
├── core/
│   └── config.py
│
├── graphics/
│   └── court.py
│
├── sprites/
│   ├── player.py
│   └── ball.py
│
├── scenes/
│   ├── menu_scene.py
│   └── game_scene.py
│
```

---

## ⚙️ Tecnologias Utilizadas

- Python 3.11
- Pygame 2.6
- PyCharm Community Edition

---

## 🚀 Como Executar

### 1. Instalar dependência
```bash
pip install pygame
```

### 2. Rodar o jogo
```bash
python main.py
```

---

## 👨‍💻 Autor(es)

Projeto acadêmico desenvolvido para a disciplina de Computação Gráfica.

- Nome: Liane F. Heidemann 
- Turma: CC7NA
- Professor(a): Suzana Lustosa de Sousa


