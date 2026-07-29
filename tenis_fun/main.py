import pygame

from core.settings import *
from scenes.menu_scene import MenuScene
from scenes.game_scene import GameScene


# Inicializa o pygame
pygame.init()

# Cria a janela do jogo
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Define o nome da janela
pygame.display.set_caption("TênisFun")

# Controla o FPS
clock = pygame.time.Clock()

# ==========================================
# CENAS
# ==========================================

menu_scene = MenuScene()
game_scene = GameScene()

# Cena ativa: "menu" ou "jogo"
active_scene = "menu"

# Loop principal
running = True

while running:

    # ==========================================
    # EVENTOS DO SISTEMA
    # ==========================================

    for event in pygame.event.get():

        # Fecha o jogo
        if event.type == pygame.QUIT:
            running = False

        # Repassa o evento para a cena ativa
        if active_scene == "menu":
            menu_scene.handle_event(event)

        elif active_scene == "jogo":
            game_scene.handle_event(event)

    # ==========================================
    # TRANSIÇÕES DE CENA
    # ==========================================

    if active_scene == "menu" and menu_scene.start_requested:

        menu_scene.start_requested = False
        game_scene.reset()
        active_scene = "jogo"

    elif active_scene == "jogo" and game_scene.return_to_menu:

        game_scene.return_to_menu = False
        active_scene = "menu"

    # ==========================================
    # ATUALIZA LÓGICA
    # ==========================================

    if active_scene == "menu":
        menu_scene.update()

    elif active_scene == "jogo":
        game_scene.update()

    # ==========================================
    # DESENHA ELEMENTOS
    # ==========================================

    if active_scene == "menu":
        menu_scene.draw(screen)

    elif active_scene == "jogo":
        game_scene.draw(screen)

    # Atualiza a tela
    pygame.display.flip()

    # Limita FPS
    clock.tick(FPS)

# Encerra pygame
pygame.quit()
