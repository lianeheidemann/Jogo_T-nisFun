import pygame

from tenis_fun.graphics.court import Court
from tenis_fun.sprites.player import Player
from tenis_fun.sprites.ball import Ball

from tenis_fun.core.settings import *
from tenis_fun.core.colors import *


class GameScene:
    def __init__(self):

        # ==========================================
        # QUADRA
        # ==========================================

        self.court = Court()

        # ==========================================
        # JOGADOR PRINCIPAL
        # ==========================================

        self.player = Player(
            x=640,
            y=660,
            scale=1.9
        )

        # ==========================================
        # ADVERSÁRIO
        # ==========================================

        self.opponent = Player(
            x=640,
            y=190,
            scale=0.75,
            opponent=True
        )

        # ==========================================
        # BOLA
        # ==========================================

        self.ball = Ball()

        # ==========================================
        # FONTE HUD
        # ==========================================

        self.font = pygame.font.SysFont(
            "Arial",
            40,
            bold=True
        )

        # ==========================================
        # FONTE FINAL
        # ==========================================

        self.end_font = pygame.font.SysFont(
            "Arial",
            90,
            bold=True
        )

    def update(self):

        # Atualiza jogador
        self.player.update()

        # Atualiza bola
        self.ball.update(self.player)

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
        # CONTADOR DE RODADAS
        # ==========================================

        remaining_hits = (
            self.ball.max_hits - self.ball.hits
        )

        text = self.font.render(
            f"Restam: {remaining_hits}",
            True,
            WHITE
        )

        screen.blit(text, (30, 30))

        # ==========================================
        # GAME OVER
        # ==========================================

        if self.ball.game_over:

            # ======================================
            # VITÓRIA
            # ======================================

            if self.ball.player_won:

                end_text = self.end_font.render(
                    "VOCÊ VENCEU!",
                    True,
                    (255, 255, 80)
                )

            # ======================================
            # DERROTA
            # ======================================

            else:

                end_text = self.end_font.render(
                    "VOCÊ PERDEU!",
                    True,
                    (255, 80, 80)
                )

            # ======================================
            # CENTRALIZA TEXTO
            # ======================================

            text_rect = end_text.get_rect(
                center=(WIDTH // 2, HEIGHT // 2)
            )

            screen.blit(end_text, text_rect)