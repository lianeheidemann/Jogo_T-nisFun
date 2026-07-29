from pathlib import Path
import runpy
import sys


# Permite que o botão "Executar arquivo Python" do VS Code abra o jogo
# mesmo quando menu_scene.py é o arquivo ativo.
if __package__ in (None, ""):
    GAME_DIR = Path(__file__).resolve().parents[1]
    sys.path.insert(0, str(GAME_DIR))

import pygame

from core.settings import *
from core.colors import *
from core.assets import asset_path
from core.ui import Button


LOGO_PATH = asset_path("menu", "logo.png")
BACKGROUND_PATH = asset_path("menu", "background_home.png")
PLAY_BUTTON_PATH = asset_path("menu", "botao_jogar.png")

# Área com conteúdo visível dentro da imagem (o restante é transparente)
LOGO_CROP = pygame.Rect(220, 203, 1116, 393)

LOGO_WIDTH = 576

# Recorta apenas o botão da imagem-fonte, removendo as margens externas.
PLAY_BUTTON_CROP = pygame.Rect(274, 320, 990, 305)
PLAY_BUTTON_SIZE = (320, 99)


class MenuScene:
    def __init__(self):

        # ==========================================
        # FUNDO
        # ==========================================

        self.background = pygame.transform.smoothscale(
            pygame.image.load(BACKGROUND_PATH).convert(),
            (WIDTH, HEIGHT)
        )

        # ==========================================
        # FONTES
        # ==========================================

        self.subtitle_font = pygame.font.SysFont("Arial", 26)
        self.button_font = pygame.font.SysFont("Arial", 32, bold=True)
        self.hint_font = pygame.font.SysFont("Arial", 22, bold=True)
        self.hint_font_small = pygame.font.SysFont("Arial", 16)

        # ==========================================
        # LOGO
        # ==========================================

        logo_image = pygame.image.load(LOGO_PATH).convert_alpha()
        logo_image = logo_image.subsurface(LOGO_CROP)

        logo_height = int(
            LOGO_WIDTH * logo_image.get_height() / logo_image.get_width()
        )

        self.logo = pygame.transform.smoothscale(
            logo_image,
            (LOGO_WIDTH, logo_height)
        )

        self.logo_rect = self.logo.get_rect(
            center=(WIDTH // 2, 250)
        )

        # ==========================================
        # BOTÃO JOGAR
        # ==========================================

        play_button_image = pygame.image.load(PLAY_BUTTON_PATH).convert_alpha()
        play_button_image = play_button_image.subsurface(PLAY_BUTTON_CROP)

        self.play_button_image = pygame.transform.smoothscale(
            play_button_image,
            PLAY_BUTTON_SIZE
        )

        # A imagem-fonte possui um fundo nas extremidades. A máscara mantém
        # somente o formato arredondado do botão.
        button_mask = pygame.Surface(PLAY_BUTTON_SIZE, pygame.SRCALPHA)
        pygame.draw.rect(
            button_mask,
            WHITE,
            button_mask.get_rect(),
            border_radius=48
        )
        self.play_button_image.blit(
            button_mask,
            (0, 0),
            special_flags=pygame.BLEND_RGBA_MULT
        )

        self.play_button_hover_image = pygame.transform.smoothscale(
            self.play_button_image,
            (
                int(PLAY_BUTTON_SIZE[0] * 1.04),
                int(PLAY_BUTTON_SIZE[1] * 1.04)
            )
        )

        self.play_button = Button(
            rect=(
                WIDTH // 2 - PLAY_BUTTON_SIZE[0] // 2,
                431,
                *PLAY_BUTTON_SIZE
            ),
            label="",
            font=self.button_font
        )

        # Sinaliza que o jogador pediu para começar a partida
        self.start_requested = False

    def handle_event(self, event):

        # Clique no botão jogar
        if self.play_button.is_clicked(event):
            self.start_requested = True

        # Tecla Enter ou espaço também iniciam o jogo
        if event.type == pygame.KEYDOWN:

            if event.key in (pygame.K_RETURN, pygame.K_SPACE):
                self.start_requested = True

    def update(self):

        mouse_pos = pygame.mouse.get_pos()

        self.play_button.update(mouse_pos)

    def draw(self, screen):

        # ==========================================
        # FUNDO
        # ==========================================

        screen.blit(self.background, (0, 0))

        # ==========================================
        # LOGO
        # ==========================================

        screen.blit(self.logo, self.logo_rect)

        subtitle_surface = self.subtitle_font.render(
            "Rebata a bola por 10 rodadas!",
            True,
            (210, 220, 235)
        )

        subtitle_rect = subtitle_surface.get_rect(
            center=(WIDTH // 2, 375)
        )

        screen.blit(subtitle_surface, subtitle_rect)

        # ==========================================
        # BOTÃO JOGAR
        # ==========================================

        button_image = (
            self.play_button_hover_image
            if self.play_button.hovered
            else self.play_button_image
        )
        button_rect = button_image.get_rect(center=self.play_button.rect.center)
        screen.blit(button_image, button_rect)

        # ==========================================
        # INSTRUÇÕES
        # ==========================================

        hint_surface = self.hint_font.render(
            "←  →   para mover",
            True,
            WHITE
        )

        hint_rect = hint_surface.get_rect(
            center=(WIDTH // 2, 550)
        )

        screen.blit(hint_surface, hint_rect)

        hint_small_surface = self.hint_font_small.render(
            "Rebata a bola no lado certo da quadra",
            True,
            (200, 210, 225)
        )

        hint_small_rect = hint_small_surface.get_rect(
            center=(WIDTH // 2, 580)
        )

        screen.blit(hint_small_surface, hint_small_rect)


if __name__ == "__main__":
    runpy.run_path(str(GAME_DIR / "main.py"), run_name="__main__")
