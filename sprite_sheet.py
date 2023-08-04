import pygame
import sys

class Sprite():
    def __init__(self, current_game, image):
        self.current_game = current_game
        self.screen = current_game.screen
        self.sheet = image
        self.sheet = pygame.transform.scale(self.sheet, (832*0.6, 1344*0.6))
        self.right = False
        self.left = False
        self.up = False
        self.down = False
        self.rect = self.sheet.get_rect()
        self.frame = 0 
        self.row = 11
        self.width = 64*0.6
        self.height = 64*0.6

    def update_sprite(self):
        """Draw the sprite to the sceen and update"""
        self.screen.blit(self.sheet, 
                         self.rect.center, 
                         ((self.frame * self.width), 
                          (self.row * self.height), 
                          self.width, self.height))
        self._check_events()
        self._update_frame()
        self._update_position()

    def _update_frame(self):
        """Update the frame of the sprite"""
        if self.right or self.left or self.up or self.down:
            self.frame = (self.frame+1)%9

    def _update_position(self):
        """Updates the position of the sprite"""
        if self.right:
            self.rect.x += 2
        elif self.left:
            self.rect.x -= 2
        elif self.up:
            self.rect.y -= 2
        elif self.down:
            self.rect.y += 2

    def _check_events(self):
        """Respond to keypresses."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.row = 11
            self.right = True
            self.left = False
            self.up = False
            self.down = False
        elif event.key == pygame.K_LEFT:
            self.row = 9
            self.right = False
            self.left = True
            self.up = False
            self.down = False
        elif event.key == pygame.K_UP:
            self.row = 8
            self.right = False
            self.left = False
            self.up = True
            self.down = False
        elif event.key == pygame.K_DOWN:
            self.row = 10
            self.right = False
            self.left = False
            self.up = False
            self.down = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.right = False
            self.frame = 0
        if event.key == pygame.K_LEFT:
            self.left = False
            self.frame = 0
        if event.key == pygame.K_UP:
            self.up = False
            self.frame = 0
        if event.key == pygame.K_DOWN:
            self.down = False
            self.frame = 0