from settings import Settings
import sys
import pygame
import sprite_sheet

image = pygame.image.load('images/sprites.png')

class PetersWorld:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()

        self.settings = Settings()
        #self.sprite = sprite_sheet.SpriteSheet(self, image)
        self.sheet = image
        self.clock = pygame.time.Clock()
        self.next_frame = 0
        self.sprite_right = False
        self.sprite_left = False
        self.sprite_up = False
        self.sprite_down = False

        self.frame = 0 
        self.row = 11
        self.width = 64
        self.height = 64

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption("Peter's World")

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.row = 11
                        self.sprite_right = True
                    elif event.key == pygame.K_LEFT:
                        self.row = 9
                        self.sprite_left = True
                    elif event.key == pygame.K_UP:
                        self.row = 8
                        self.sprite_up = True
                    elif event.key == pygame.K_DOWN:
                        self.row = 10
                        self.sprite_down = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.sprite_right = False
                        self.frame = 0
                    if event.key == pygame.K_LEFT:
                        self.sprite_left = False
                        self.frame = 0
                    if event.key == pygame.K_UP:
                        self.sprite_up = False
                        self.frame = 0
                    if event.key == pygame.K_DOWN:
                        self.sprite_down = False
                        self.frame = 0
            self._update_screen()
            self.clock.tick(30)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.blit_sprite()
        if self.sprite_right or self.sprite_left or self.sprite_up or self.sprite_down:
            self.frame = (self.frame+1)%9 
        pygame.display.flip()

    def blit_sprite(self):
        self.screen.blit(self.sheet, 
                         self.screen_rect.center, 
                         ((self.frame * self.width), 
                          (self.row * self.height), 
                          self.width, self.height))
        
    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
        
    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

if __name__ == '__main__':
    # Make a game instance, and run the game.
    pw = PetersWorld()
    pw.run_game()
