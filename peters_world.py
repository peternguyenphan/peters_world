from settings import Settings
import sys
import pygame
from sprite_sheet import Agent

image = pygame.image.load('images/sprites.png')
map = pygame.image.load('images/map.png')

class PetersWorld:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()

        self.settings = Settings()
        self.map = map
        self.map = pygame.transform.scale(self.map, (1464, 832))
        self.clock = pygame.time.Clock()
        self.map_rect = self.map.get_rect()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        self.screen_rect = self.screen.get_rect()
        self.sprite = Agent(self, image, 64, 64, 832, 1344)
        pygame.display.set_caption("Peter's World")

    def run_game(self):
        """Start the main loop for the game."""
        while True:                
            self._update_screen()
            self.clock.tick(30)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.screen.blit(self.map, self.screen_rect.topleft, (0, 
                          0, 
                          1464, 832))
        #self.sprite.sprite_rect.midtop = (self.sprite.rect.centerx+32, self.sprite.rect.centery+14)
        #pygame.draw.rect(self.screen, (200,200,200), self.sprite.sprite_rect)
        self.sprite.update_sprite()
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    pw = PetersWorld()
    pw.run_game()
