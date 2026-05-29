import pygame

from core.settings import *
from core.colors import *


class Court:
    def __init__(self):

        # Horizonte da quadra
        self.horizon_y = 140

        # Posição da rede
        self.net_y = 355

    def draw(self, screen):

        # ==================================================
        # CÉU / FUNDO
        # ==================================================

        screen.fill((25, 45, 80))

        # ==================================================
        # QUADRA EM PERSPECTIVA
        # ==================================================

        left_bottom = (120, HEIGHT)
        right_bottom = (1160, HEIGHT)

        left_top = (470, self.horizon_y)
        right_top = (810, self.horizon_y)

        court_points = [
            left_bottom,
            right_bottom,
            right_top,
            left_top
        ]

        pygame.draw.polygon(
            screen,
            (48, 150, 90),
            court_points
        )

        # ==================================================
        # ÁREA EXTERNA DA QUADRA
        # ==================================================

        outer_points = [
            (40, HEIGHT),
            (1240, HEIGHT),
            (860, 90),
            (420, 90)
        ]

        pygame.draw.polygon(
            screen,
            (35, 110, 65),
            outer_points
        )

        # ==================================================
        # LINHAS EXTERNAS
        # ==================================================

        pygame.draw.line(
            screen,
            WHITE,
            left_bottom,
            left_top,
            5
        )

        pygame.draw.line(
            screen,
            WHITE,
            right_bottom,
            right_top,
            5
        )

        pygame.draw.line(
            screen,
            WHITE,
            left_bottom,
            right_bottom,
            5
        )

        pygame.draw.line(
            screen,
            WHITE,
            left_top,
            right_top,
            3
        )

        # ==================================================
        # LINHA CENTRAL
        # ==================================================

        pygame.draw.line(
            screen,
            WHITE,
            (WIDTH // 2, HEIGHT),
            (WIDTH // 2, self.horizon_y),
            3
        )

        # ==================================================
        # LINHAS INTERNAS
        # ==================================================

        # Laterais internas
        pygame.draw.line(
            screen,
            WHITE,
            (300, HEIGHT),
            (545, self.horizon_y),
            3
        )

        pygame.draw.line(
            screen,
            WHITE,
            (980, HEIGHT),
            (735, self.horizon_y),
            3
        )

        # Linha horizontal superior
        pygame.draw.line(
            screen,
            WHITE,
            (545, self.horizon_y),
            (735, self.horizon_y),
            2
        )

        # ==================================================
        # REDE
        # ==================================================

        net_left = (260, self.net_y)
        net_right = (1020, self.net_y)

        # Faixa superior da rede
        pygame.draw.line(
            screen,
            WHITE,
            net_left,
            net_right,
            6
        )

        # Corpo da rede
        net_rect = pygame.Rect(
            260,
            self.net_y,
            760,
            70
        )

        pygame.draw.rect(
            screen,
            (180, 180, 180),
            net_rect
        )

        # ==================================================
        # MALHA DA REDE
        # ==================================================

        # Linhas verticais
        for x in range(260, 1020, 14):

            pygame.draw.line(
                screen,
                (120, 120, 120),
                (x, self.net_y),
                (x, self.net_y + 70),
                1
            )

        # Linhas horizontais
        for y in range(self.net_y, self.net_y + 70, 10):

            pygame.draw.line(
                screen,
                (120, 120, 120),
                (260, y),
                (1020, y),
                1
            )

        # ==================================================
        # POSTES DA REDE
        # ==================================================

        pygame.draw.rect(
            screen,
            (230, 230, 230),
            (248, self.net_y - 20, 10, 95)
        )

        pygame.draw.rect(
            screen,
            (230, 230, 230),
            (1020, self.net_y - 20, 10, 95)
        )

        # ==================================================
        # SOMBRA DA REDE
        # ==================================================

        pygame.draw.rect(
            screen,
            (30, 90, 50),
            (260, self.net_y + 70, 760, 8)
        )