import random

import pygame

from core.colors import *
from core.assets import asset_path


BALL_PATH = asset_path("game", "bola.png")

BALL_CROP = pygame.Rect(546, 263, 450, 450)
HIT_DISTANCE = 135
HIT_ANTICIPATION_MS = 1000


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

        # Recorta a bola e remove o fundo da imagem-fonte.
        ball_image = pygame.image.load(BALL_PATH).convert_alpha()
        self.image = ball_image.subsurface(BALL_CROP).copy()

        ball_mask = pygame.Surface(self.image.get_size(), pygame.SRCALPHA)
        pygame.draw.circle(
            ball_mask,
            WHITE,
            (BALL_CROP.width // 2, BALL_CROP.height // 2),
            BALL_CROP.width // 2
        )
        self.image.blit(
            ball_mask,
            (0, 0),
            special_flags=pygame.BLEND_RGBA_MULT
        )

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

        # Controla a antecipação da animação de rebatida nesta trajetória.
        self.hit_animation_started = False

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
        # ANTECIPAÇÃO DA REBATIDA
        # ==========================================

        if not self.hit_animation_started and self.speed_y > 0:

            remaining_frames = max(0, (640 - self.y) / self.speed_y)
            remaining_time_ms = remaining_frames * 16

            if remaining_time_ms <= HIT_ANTICIPATION_MS:
                player.play_hit()
                self.hit_animation_started = True

        # ==========================================
        # CHEGOU NO JOGADOR
        # ==========================================

        if self.y >= 640:

            # Só rebate quando o jogador realmente alcança a bola.
            hit = abs(player.x - self.x) <= HIT_DISTANCE

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

        ball_surface = pygame.transform.smoothscale(
            self.image,
            (radius * 2, radius * 2)
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
