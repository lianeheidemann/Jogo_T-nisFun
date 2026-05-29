import pygame

from core.colors import *
from core.settings import *


class Player:
    def __init__(self, x, y, scale=1.0, opponent=False):

        # Posição
        self.x = x
        self.y = y

        # Escala
        self.scale = scale

        # Adversário
        self.opponent = opponent

        # Direção da raquete
        self.racket_side = 1

        # Velocidade
        self.speed = 8

        # ==========================================
        # SUPERFÍCIE DA RAQUETE
        # ==========================================

        self.racket_surface = pygame.Surface(
            (50, 70),
            pygame.SRCALPHA
        )

        # Cabo
        pygame.draw.rect(
            self.racket_surface,
            (110, 70, 30),
            (22, 35, 6, 28)
        )

        # Aro
        pygame.draw.ellipse(
            self.racket_surface,
            RACKET_COLOR,
            (10, 0, 30, 40),
            4
        )

        # Cordas verticais
        for i in range(3):

            pygame.draw.line(
                self.racket_surface,
                WHITE,
                (18 + (i * 5), 4),
                (18 + (i * 5), 34),
                1
            )

        # Cordas horizontais
        for i in range(3):

            pygame.draw.line(
                self.racket_surface,
                WHITE,
                (12, 10 + (i * 8)),
                (38, 10 + (i * 8)),
                1
            )

    def update(self):

        # Apenas jogador principal
        if not self.opponent:

            keys = pygame.key.get_pressed()

            # ==========================================
            # MOVIMENTO PARA ESQUERDA
            # ==========================================

            if keys[pygame.K_LEFT]:

                self.x -= self.speed

                self.racket_side = -1

            # ==========================================
            # MOVIMENTO PARA DIREITA
            # ==========================================

            if keys[pygame.K_RIGHT]:

                self.x += self.speed

                self.racket_side = 1

            # ==========================================
            # LIMITES DA QUADRA
            # ==========================================

            if self.x < 260:
                self.x = 260

            if self.x > 1020:
                self.x = 1020

    def draw(self, screen):

        s = self.scale

        shirt_color = LIGHT_BLUE

        if self.opponent:
            shirt_color = (220, 80, 80)

        # ==========================================
        # SOMBRA
        # ==========================================

        pygame.draw.ellipse(
            screen,
            (30, 30, 30),
            (
                self.x - (25 * s),
                self.y + (20 * s),
                50 * s,
                12 * s
            )
        )

        # ==========================================
        # CABEÇA
        # ==========================================

        pygame.draw.rect(
            screen,
            PLAYER_COLOR,
            (
                self.x - (8 * s),
                self.y - (55 * s),
                16 * s,
                16 * s
            )
        )

        # ==========================================
        # CORPO
        # ==========================================

        pygame.draw.rect(
            screen,
            shirt_color,
            (
                self.x - (14 * s),
                self.y - (38 * s),
                28 * s,
                34 * s
            )
        )

        # ==========================================
        # PERNAS
        # ==========================================

        pygame.draw.rect(
            screen,
            WHITE,
            (
                self.x - (10 * s),
                self.y - (4 * s),
                8 * s,
                26 * s
            )
        )

        pygame.draw.rect(
            screen,
            WHITE,
            (
                self.x + (2 * s),
                self.y - (4 * s),
                8 * s,
                26 * s
            )
        )

        # ==========================================
        # BRAÇO
        # ==========================================

        arm_x = self.x + (12 * s)

        if self.racket_side == -1:
            arm_x = self.x - (28 * s)

        pygame.draw.rect(
            screen,
            PLAYER_COLOR,
            (
                arm_x,
                self.y - (30 * s),
                16 * s,
                6 * s
            )
        )

        # ==========================================
        # FLIP DA RAQUETE
        # ==========================================

        racket_image = self.racket_surface

        if self.racket_side == -1:

            racket_image = pygame.transform.flip(
                self.racket_surface,
                True,
                False
            )

        racket_image = pygame.transform.scale(
            racket_image,
            (int(50 * s), int(70 * s))
        )

        # ==========================================
        # POSIÇÃO DA RAQUETE
        # ==========================================

        racket_x = self.x + (10 * s)

        if self.racket_side == -1:
            racket_x = self.x - (55 * s)

        screen.blit(
            racket_image,
            (
                racket_x,
                self.y - (60 * s)
            )
        )