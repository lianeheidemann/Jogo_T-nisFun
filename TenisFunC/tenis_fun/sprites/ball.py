import pygame
import math
import random

from core.colors import *


class Ball:
    def __init__(self):

        # ==========================================
        # TEMPO INICIAL
        # ==========================================

        # Tempo inicial
        self.travel_time = 2000

        # Tempo mínimo
        self.minimum_time = 1000

        # Estado do jogo
        self.game_over = False
        self.player_won = False

        # Quantidade de acertos
        self.hits = 0
        # Quantidade necessária para vencer
        self.max_hits = 10

        # Inicia bola
        self.reset()

    def reset(self):

        # ==========================================
        # POSIÇÃO INICIAL
        # ==========================================

        self.x = 640
        self.y = 210

        # ==========================================
        # ESCOLHE LADO
        # ==========================================

        self.target_side = random.choice(
            ["left", "right"]
        )

        # ==========================================
        # DESTINO DA BOLA
        # ==========================================

        if self.target_side == "left":
            self.target_x = 400

        else:
            self.target_x = 880

        # ==========================================
        # VELOCIDADE
        # ==========================================

        frames = self.travel_time / 16

        self.speed_x = (
            self.target_x - self.x
        ) / frames

        self.speed_y = (
            700 - self.y
        ) / frames

        # ==========================================
        # ESCALA
        # ==========================================

        self.scale = 0.3

        self.scale_speed = 1.8 / frames

        # ==========================================
        # ROTAÇÃO
        # ==========================================

        self.rotation = 0

    def update(self, player):

        # ==========================================
        # GAME OVER
        # ==========================================

        if self.game_over:
            return

        # ==========================================
        # MOVIMENTO
        # ==========================================

        self.x += self.speed_x
        self.y += self.speed_y

        # ==========================================
        # ESCALA
        # ==========================================

        self.scale += self.scale_speed

        # ==========================================
        # ROTAÇÃO
        # ==========================================

        self.rotation += 10

        # ==========================================
        # CHEGOU NO JOGADOR
        # ==========================================

        if self.y >= 640:

            hit = False

            # Bola esquerda
            if self.target_side == "left":

                if player.x < 640:
                    hit = True

            # Bola direita
            else:

                if player.x >= 640:
                    hit = True

            # ==========================================
            # ACERTOU
            # ==========================================

            if hit:

                # Conta acertos
                self.hits += 1

                # Aumenta velocidade
                self.travel_time -= 100

                # Vitória
                if self.hits >= self.max_hits:

                    self.player_won = True
                    self.game_over = True

                else:

                    # Limite mínimo
                    if self.travel_time < self.minimum_time:
                        self.travel_time = self.minimum_time

                    self.reset()

            # ==========================================
            # ERROU
            # ==========================================

            else:

                self.game_over = True

    def draw(self, screen):

        # ==========================================
        # TAMANHO
        # ==========================================

        radius = int(20 * self.scale)

        if radius < 2:
            radius = 2

        # ==========================================
        # SOMBRA
        # ==========================================

        pygame.draw.ellipse(
            screen,
            (35, 35, 35),
            (
                self.x - radius,
                self.y + radius,
                radius * 2,
                radius
            )
        )

        # ==========================================
        # SUPERFÍCIE
        # ==========================================

        size = radius * 4

        ball_surface = pygame.Surface(
            (size, size),
            pygame.SRCALPHA
        )

        center = size // 2

        # Corpo da bola
        pygame.draw.circle(
            ball_surface,
            (215, 255, 60),
            (center, center),
            radius
        )

        # Brilho
        pygame.draw.circle(
            ball_surface,
            (240, 255, 140),
            (
                center - int(radius * 0.35),
                center - int(radius * 0.35)
            ),
            int(radius * 0.45)
        )

        # Curvas
        line_size = max(
            1,
            int(radius * 0.18)
        )

        pygame.draw.arc(
            ball_surface,
            WHITE,
            (
                center - radius,
                center - radius,
                radius,
                radius * 2
            ),
            math.radians(-90),
            math.radians(90),
            line_size
        )

        pygame.draw.arc(
            ball_surface,
            WHITE,
            (
                center,
                center - radius,
                radius,
                radius * 2
            ),
            math.radians(90),
            math.radians(270),
            line_size
        )

        # ==========================================
        # ROTAÇÃO
        # ==========================================

        rotated_ball = pygame.transform.rotate(
            ball_surface,
            self.rotation
        )

        rect = rotated_ball.get_rect(
            center=(self.x, self.y)
        )

        # ==========================================
        # DESENHA
        # ==========================================

        screen.blit(rotated_ball, rect)