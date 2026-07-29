import pygame

from graphics.court import Court
from sprites.player import Player
from sprites.ball import Ball
from core.ui import Button

from core.settings import *
from core.colors import *
from core.assets import asset_path


RESTART_BUTTON_PATH = asset_path("game", "botao_jogar-novamente.png")
MENU_BUTTON_PATH = asset_path("game", "botao_menu.png")
WIN_CARD_PATH = asset_path("game", "box_ganho.png")
LOSE_CARD_PATH = asset_path("game", "box_perdeu.png")

# As artes possuem margens externas; este recorte mantém somente o botão.
END_BUTTON_CROP = pygame.Rect(274, 320, 990, 305)
RESTART_BUTTON_SIZE = (320, 99)
MENU_BUTTON_SIZE = (272, 84)

# Recorte comum que enquadra os dois cards e remove as margens transparentes.
END_CARD_CROP = pygame.Rect(235, 85, 1063, 705)
END_CARD_SIZE = (700, 464)

ROUND_BOX_SIZE = (336, 96)
ROUND_BOX_TOP = 15


class GameScene:
    def __init__(self):

        # ==========================================
        # FONTE HUD
        # ==========================================

        self.font = pygame.font.SysFont(
            "Arial",
            26,
            bold=True
        )

        # ==========================================
        # FONTES DA TELA DE FIM DE JOGO
        # ==========================================

        self.end_font = pygame.font.SysFont(
            "Arial",
            56,
            bold=True
        )

        self.subtext_font = pygame.font.SysFont(
            "Arial",
            24
        )

        self.button_font = pygame.font.SysFont(
            "Arial",
            26,
            bold=True
        )

        # ==========================================
        # BOTÕES DA TELA DE FIM DE JOGO
        # ==========================================

        self.restart_button = Button(
            rect=(
                WIDTH // 2 - RESTART_BUTTON_SIZE[0] // 2,
                HEIGHT // 2 + 25,
                *RESTART_BUTTON_SIZE
            ),
            label="",
            font=self.button_font
        )

        self.menu_button = Button(
            rect=(
                WIDTH // 2 - MENU_BUTTON_SIZE[0] // 2,
                HEIGHT // 2 + 105,
                *MENU_BUTTON_SIZE
            ),
            label="",
            font=self.button_font
        )

        self.restart_button_image = self.load_button_image(
            RESTART_BUTTON_PATH,
            RESTART_BUTTON_SIZE
        )
        self.menu_button_image = self.load_button_image(
            MENU_BUTTON_PATH,
            MENU_BUTTON_SIZE
        )

        self.restart_button_hover_image = self.create_hover_image(
            self.restart_button_image
        )
        self.menu_button_hover_image = self.create_hover_image(
            self.menu_button_image
        )

        self.win_card_image = self.load_card_image(WIN_CARD_PATH)
        self.lose_card_image = self.load_card_image(LOSE_CARD_PATH)

        self.round_box_images = []

        for round_number in range(1, 11):
            round_box = pygame.image.load(
                asset_path(
                    "game",
                    "box_rodada",
                    f"rodada_{round_number}_de_10.png"
                )
            ).convert_alpha()
            round_box = pygame.transform.smoothscale(
                round_box,
                ROUND_BOX_SIZE
            )
            self.round_box_images.append(round_box)

        # Cria os elementos da partida
        self.reset()

    def load_button_image(self, path, size):

        image = pygame.image.load(path).convert_alpha()
        image = image.subsurface(END_BUTTON_CROP).copy()
        image = pygame.transform.smoothscale(image, size)

        # Mantém apenas o formato arredondado do botão.
        button_mask = pygame.Surface(size, pygame.SRCALPHA)
        pygame.draw.rect(
            button_mask,
            WHITE,
            button_mask.get_rect(),
            border_radius=44
        )
        image.blit(
            button_mask,
            (0, 0),
            special_flags=pygame.BLEND_RGBA_MULT
        )

        return image

    def create_hover_image(self, image):

        width, height = image.get_size()

        return pygame.transform.smoothscale(
            image,
            (
                int(width * 1.04),
                int(height * 1.04)
            )
        )

    def load_card_image(self, path):

        image = pygame.image.load(path).convert_alpha()
        image = image.subsurface(END_CARD_CROP).copy()

        return pygame.transform.smoothscale(image, END_CARD_SIZE)

    def reset(self):

        # ==========================================
        # QUADRA
        # ==========================================

        self.court = Court()

        # ==========================================
        # JOGADOR PRINCIPAL
        # ==========================================

        self.player = Player(
            x=640,
            y=665,
            scale=1.35
        )

        # ==========================================
        # ADVERSÁRIO
        # ==========================================

        self.opponent = Player(
            x=640,
            y=320,
            scale=0.42,
            opponent=True
        )

        # ==========================================
        # BOLA
        # ==========================================

        self.ball = Ball()

        # Sinaliza pedido de voltar ao menu
        self.return_to_menu = False

    def handle_event(self, event):

        # Botões só respondem quando a partida terminou
        if not self.ball.game_over:
            return

        if self.restart_button.is_clicked(event):
            self.reset()

        elif self.menu_button.is_clicked(event):
            self.return_to_menu = True

    def update(self):

        # Atualiza jogador
        self.player.update()

        # Move o adversário para o lado escolhido para a bola
        self.opponent.update(self.ball.target_side)

        # Atualiza bola
        self.ball.update(self.player)

        # ==========================================
        # HOVER DOS BOTÕES
        # ==========================================

        if self.ball.game_over:

            mouse_pos = pygame.mouse.get_pos()

            self.restart_button.update(mouse_pos)
            self.menu_button.update(mouse_pos)

    def draw(self, screen):

        # ==========================================
        # DESENHA QUADRA
        # ==========================================

        self.court.draw(screen)

        # ==========================================
        # DESENHA ADVERSÁRIO
        # ==========================================

        self.opponent.draw(screen)

        # ==========================================
        # DESENHA BOLA
        # ==========================================

        self.ball.draw(screen)

        # ==========================================
        # DESENHA JOGADOR
        # ==========================================

        self.player.draw(screen)

        # ==========================================
        # HUD
        # ==========================================

        self.draw_hud(screen)

        # ==========================================
        # GAME OVER
        # ==========================================

        if self.ball.game_over:
            self.draw_game_over(screen)

    def draw_hud(self, screen):

        # ==========================================
        # BOX DA RODADA ATUAL
        # ==========================================

        round_number = min(self.ball.hits + 1, self.ball.max_hits)
        round_box = self.round_box_images[round_number - 1]
        round_box_rect = round_box.get_rect(
            midtop=(WIDTH // 2, ROUND_BOX_TOP)
        )

        screen.blit(round_box, round_box_rect)

    def draw_game_over(self, screen):

        # ==========================================
        # OVERLAY ESCURO
        # ==========================================

        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)

        overlay.fill((10, 15, 25, 165))

        screen.blit(overlay, (0, 0))

        # ==========================================
        # CARD DO RESULTADO
        # ==========================================

        card_image = (
            self.win_card_image
            if self.ball.player_won
            else self.lose_card_image
        )
        card_rect = card_image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(card_image, card_rect)

        # ==========================================
        # BOTÕES
        # ==========================================

        restart_image = (
            self.restart_button_hover_image
            if self.restart_button.hovered
            else self.restart_button_image
        )
        restart_rect = restart_image.get_rect(
            center=self.restart_button.rect.center
        )
        screen.blit(restart_image, restart_rect)

        menu_image = (
            self.menu_button_hover_image
            if self.menu_button.hovered
            else self.menu_button_image
        )
        menu_rect = menu_image.get_rect(
            center=self.menu_button.rect.center
        )
        screen.blit(menu_image, menu_rect)
