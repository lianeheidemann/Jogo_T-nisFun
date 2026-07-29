import pygame

from core.colors import *


class Button:
    def __init__(self, rect, label, font, base_color=BUTTON_COLOR, hover_color=BUTTON_HOVER_COLOR, text_color=WHITE):

        # Área clicável
        self.rect = pygame.Rect(rect)

        # Texto do botão
        self.label = label

        # Fonte
        self.font = font

        # Cores
        self.base_color = base_color
        self.hover_color = hover_color
        self.text_color = text_color

        # Estado de hover
        self.hovered = False

    def update(self, mouse_pos):

        # Verifica se o mouse está sobre o botão
        self.hovered = self.rect.collidepoint(mouse_pos)

    def is_clicked(self, event):

        # Clique esquerdo dentro da área do botão
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            return self.rect.collidepoint(event.pos)

        return False

    def draw(self, screen):

        color = self.hover_color if self.hovered else self.base_color

        # ==========================================
        # FUNDO DO BOTÃO
        # ==========================================

        pygame.draw.rect(
            screen,
            color,
            self.rect,
            border_radius=14
        )

        pygame.draw.rect(
            screen,
            WHITE,
            self.rect,
            width=2,
            border_radius=14
        )

        # ==========================================
        # TEXTO
        # ==========================================

        text_surface = self.font.render(self.label, True, self.text_color)

        text_rect = text_surface.get_rect(center=self.rect.center)

        screen.blit(text_surface, text_rect)
