import pygame

from core.settings import *
from scenes.game_scene import GameScene


# Inicializa o pygame
pygame.init()

# Cria a janela do jogo
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Define o nome da janela
pygame.display.set_caption("TênisFun")

# Controla o FPS
clock = pygame.time.Clock()

# Cena principal do jogo
game_scene = GameScene()

# Loop principal
running = True

while running:
    # Eventos do sistema
    for event in pygame.event.get():

        # Fecha o jogo
        if event.type == pygame.QUIT:
            running = False

    # Atualiza lógica
    game_scene.update()

    # Desenha elementos
    game_scene.draw(screen)

    # Atualiza a tela
    pygame.display.flip()

    # Limita FPS
    clock.tick(FPS)

# Encerra pygame
pygame.quit()