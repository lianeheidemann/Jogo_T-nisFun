import os

import pygame

from core.colors import *
from core.settings import *
from core.assets import asset_path


PLAYER_SPRITE_FOLDER = asset_path("characters", "jogador-1")
OPPONENT_SPRITE_FOLDER = asset_path("characters", "jogador-2")

# Tamanho de exibição do sprite, em pixels de altura, para scale=1.0
SPRITE_DISPLAY_HEIGHT = 260

# Duração de cada quadro das animações, em frames de jogo (60 fps)
WALK_FRAME_DURATION = 8
HIT_FRAME_DURATION = 65

OPPONENT_LEFT_X = 590
OPPONENT_RIGHT_X = 690
OPPONENT_SPEED = 1.5


class Player:

    # Cache dos sprites, compartilhado entre instâncias de cada personagem.
    _sprite_sets = {}

    @classmethod
    def _load_sprites(cls, opponent):

        sprite_set = "opponent" if opponent else "player"

        if sprite_set in cls._sprite_sets:
            return cls._sprite_sets[sprite_set]

        folder = OPPONENT_SPRITE_FOLDER if opponent else PLAYER_SPRITE_FOLDER
        prefix = "jogadora" if opponent else "jogador"
        left_suffix = "right" if opponent else "left"
        right_suffix = "left" if opponent else "right"

        def load(name):
            return pygame.image.load(
                os.path.join(folder, name)
            ).convert_alpha()

        sprites = {
            "idle": [load(f"{prefix}_idle.png")],
            "walk_left": [load(f"{prefix}_move_{left_suffix}.png")],
            "walk_right": [load(f"{prefix}_move_{right_suffix}.png")],
            "hit_left": [load(f"{prefix}_hit_{left_suffix}.png")],
            "hit_right": [load(f"{prefix}_hit_{right_suffix}.png")]
        }

        cls._sprite_sets[sprite_set] = sprites

        return sprites

    def __init__(self, x, y, scale=1.0, opponent=False):

        # Posição
        self.x = x
        self.y = y

        # Escala
        self.scale = scale

        # Adversário
        self.opponent = opponent

        # Direção da raquete / do sprite
        self.racket_side = 1

        # Velocidade
        self.speed = 8

        # ==========================================
        # SPRITES E ANIMAÇÃO
        # ==========================================

        self._sprites = self._load_sprites(self.opponent)

        self.state = "idle"
        self.anim_index = 0
        self.anim_timer = 0

        # Cache de frames já escalados.
        self._scaled_cache = {}

        # ==========================================
        # SUPERFÍCIE DA RAQUETE (adversário, desenho antigo)
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

    def play_hit(self):

        # Dispara a animação de rebatida (apenas jogador principal)
        if self.opponent:
            return

        self.state = "hit"
        self.anim_index = 0
        self.anim_timer = 0

    def update(self, target_side=None):

        if self.opponent:
            self._update_opponent(target_side)
            return

        # Apenas jogador principal
        if not self.opponent:

            keys = pygame.key.get_pressed()

            moving = False

            # ==========================================
            # MOVIMENTO PARA ESQUERDA
            # ==========================================

            if keys[pygame.K_LEFT]:

                self.x -= self.speed

                self.racket_side = -1

                moving = True

            # ==========================================
            # MOVIMENTO PARA DIREITA
            # ==========================================

            if keys[pygame.K_RIGHT]:

                self.x += self.speed

                self.racket_side = 1

                moving = True

            # ==========================================
            # LIMITES DA QUADRA
            # ==========================================

            if self.x < 260:
                self.x = 260

            if self.x > 1020:
                self.x = 1020

            # ==========================================
            # ANIMAÇÃO
            # ==========================================

            self._update_animation(moving)

    def _update_opponent(self, target_side):

        if target_side not in ("left", "right"):
            self._update_animation(False)
            return

        target_x = (
            OPPONENT_LEFT_X
            if target_side == "left"
            else OPPONENT_RIGHT_X
        )

        distance = target_x - self.x

        if abs(distance) <= OPPONENT_SPEED:
            self.x = target_x
            self._update_animation(False)
            return

        self.racket_side = -1 if distance < 0 else 1
        self.x += OPPONENT_SPEED * self.racket_side
        self._update_animation(True)

    def _update_animation(self, moving):

        if self.state == "hit":

            self.anim_timer += 1

            if self.anim_timer >= HIT_FRAME_DURATION:

                self.anim_timer = 0
                self.state = "walk" if moving else "idle"
                self.anim_index = 0

            return

        self.state = "walk" if moving else "idle"

        if self.state == "idle":

            self.anim_index = 0

            return

        frames = self._sprites[self._get_sprite_key()]

        self.anim_timer += 1

        if self.anim_timer >= WALK_FRAME_DURATION:

            self.anim_timer = 0
            self.anim_index = (self.anim_index + 1) % len(frames)

    def _get_sprite_key(self):

        if self.state == "idle":
            return "idle"

        direction = "left" if self.racket_side == -1 else "right"

        return f"{self.state}_{direction}"

    def _get_scaled_frame(self):

        sprite_key = self._get_sprite_key()
        frame = self._sprites[sprite_key][self.anim_index]

        cache_key = (sprite_key, self.anim_index)

        cached = self._scaled_cache.get(cache_key)

        if cached is not None:
            return cached

        display_height = SPRITE_DISPLAY_HEIGHT * self.scale

        scale_factor = display_height / frame.get_height()

        size = (
            int(frame.get_width() * scale_factor),
            int(frame.get_height() * scale_factor)
        )

        scaled = pygame.transform.smoothscale(frame, size)

        self._scaled_cache[cache_key] = scaled

        return scaled

    def draw(self, screen):

        self._draw_sprite(screen)

    def _draw_sprite(self, screen):

        frame = self._get_scaled_frame()

        sprite_key = self._get_sprite_key()
        source_frame = self._sprites[sprite_key][self.anim_index]
        visible_rect = source_frame.get_bounding_rect(min_alpha=16)

        ground_offset = int(
            frame.get_height() * visible_rect.bottom / source_frame.get_height()
        )

        # ==========================================
        # SOMBRA
        # ==========================================

        shadow_width = 50 * self.scale

        pygame.draw.ellipse(
            screen,
            (30, 30, 30),
            (
                self.x - shadow_width / 2,
                self.y - (6 * self.scale),
                shadow_width,
                12 * self.scale
            )
        )

        # ==========================================
        # SPRITE
        # ==========================================

        rect = frame.get_rect()
        rect.centerx = self.x
        rect.y = self.y - ground_offset

        screen.blit(frame, rect)

    def _draw_shape(self, screen):

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
