class SpriteSheet():
    def __init__(self, current_game, image):
        self.sheet = image 
        self.screen = current_game.screen
        self.screen_rect = current_game.screen.get_rect()

    #def get_image(self):
        #image = pygame.Surface((self.width, self.height)).convert_alpha()
        #image.blit(self.sheet, (0,0), ((frame * width), (row * height), width, height))
        #image = pygame.transform.scale(image, (self.width * self.scale, self.height * self.scale))
        #return image 
    
    def blit_sprite(self, frame, row, width, height):
        self.screen.blit(self.sheet, 
                         (0,0), 
                         ((frame * width), 
                          (row * height), 
                          width, height))