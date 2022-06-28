import pygame
from settings import *
from tile import *
from player import *
from debug import debug
class Level:
    def __init__(self):
        
        # get the display surface anywhere of our code
        self.display_surface = pygame.display.get_surface()
        
        # creamos los grupos de sprite
        # sprite es un modulo con clases de objetos basicos de juego
        # pygame.sprite.Group es un contenedor de clases con puede mantener y administrar multiples objetos sprite
        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()
        # creamos el atributo create_map
        self.create_map()
        
    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index*TILESIZE
                y = row_index*TILESIZE
                if col == 'x':
                    Tile((x,y),([self.visible_sprites],[self.obstacles_sprites]))
                if col == 'p':
                    self.player = Player((x,y),[self.visible_sprites])
                    debug(self.player.direction)

    def run(self):
        # quiero que dibujes esta variable que es conciderada un grupo de sprits dado que fue guardad en el contenedor
        # pygame.sprite.Group, y quiero que me lo muestres
        self.visible_sprites.draw(self.display_surface)
        # funcion que hace part de la clase Group y actualiza los sprites

        debug(self.player.direction)