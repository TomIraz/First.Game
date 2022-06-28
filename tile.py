import pygame
from settings import *

# pygame.sprite.Sprite: es la clase base para objetos de juego visibles
class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        # super() devuelve un objeto temporal que nos permite acceder a metodos de la clase base
        # basicamente le decimos coloque la variable groups como objeto de del
        super().__init__(groups)
        # vamos a buscar una imagen de nuestro disco para mostrarla y la guardamos en la variable self.iamge
        self.image = pygame.image.load("graphics\Zelda-main\level\graphics\prueba\prueba-roca.png").convert_alpha()
        # le decimos donde queremos que aparezca nuestra imagen y como la guardamos en la variable self.image lo hacemos asi
        self.rect = self.image.get_rect(topleft = pos)
        print('hola')