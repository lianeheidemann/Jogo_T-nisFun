import pygame

from core.settings import *
from core.colors import *
from core.assets import asset_path


BACKGROUND_PATH = asset_path("game", "background.png")
NET_PATH = asset_path("game", "rede.png")

# Remove as margens transparentes da arte antes de dimensionar.
NET_CROP = pygame.Rect(54, 55, 2963, 426)
NET_WIDTH = 720
NET_TOP_Y = 350


class Court:
    def __init__(self):

        # ==================================================
        # IMAGEM DE FUNDO
        # ==================================================

        self.background = pygame.transform.scale(
            pygame.image.load(BACKGROUND_PATH).convert(),
            (WIDTH, HEIGHT)
        )

        # ==================================================
        # IMAGEM DA REDE
        # ==================================================

        net_image = pygame.image.load(NET_PATH).convert_alpha()
        net_image = net_image.subsurface(NET_CROP).copy()

        net_height = int(
            NET_WIDTH * net_image.get_height() / net_image.get_width()
        )

        self.net = pygame.transform.smoothscale(
            net_image,
            (NET_WIDTH, net_height)
        )

        self.net_rect = self.net.get_rect(
            midtop=(WIDTH // 2, NET_TOP_Y)
        )

    def draw(self, screen):

        # ==================================================
        # FUNDO
        # ==================================================

        screen.blit(self.background, (0, 0))

        # ==================================================
        # REDE
        # ==================================================

        screen.blit(self.net, self.net_rect)
