import pygame

class Level:
    def __init__(self):
        
        # get the display surface anywhere of our code
        self.display_surface = pygame.display.get_surface()
        
        # creamos los grupos de sprite
        # sprite es un modulo con clases de objetos basicos de juego
        # pygame.sprite.Group es un contenedor de clases con puede mantener y administrar multiples objetos sprite
        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()

    def run(self):
        # update and draw the game
        pass