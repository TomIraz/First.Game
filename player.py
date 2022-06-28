import pygame
import pygame.key
from settings import *

# pygame.sprite.Sprite: es la clase base para objetos de juego visibles
class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        # super() devuelve un objeto temporal que nos permite acceder a metodos de la clase base
        # basicamente le decimos coloque la variable groups como objeto de del
        super().__init__(groups)
        # vamos a buscar una imagen de nuestro disco para mostrarla y la guardamos en la variable self.iamge
        self.image = pygame.image.load('graphics\Zelda-main\level\graphics\prueba\player.png').convert_alpha()
        # le decimos donde queremos que aparezca nuestra imagen y como la guardamos en la variable self.image lo hacemos asi
        self.rect = self.image.get_rect(topleft = pos)
        
        # vamos a darle crear un eje x e y para donde se movera el jugador
        # vector 2 es un vectro [x = 0, y = 0] siendo 0 el valor por defecto
        # x e y representan cuantos pixeles se mueven por frame en eje x e y
        self.direction = pygame.math.Vector2()
        
    def inputs(self):
        # esta funcion se da cuenta cuando una tecla y cual tecla se esta presionando
        # es una funcion bool por lo que su valor tiene que estar entre []
        keys = pygame.key.get_pressed()
        self.inputs()

        # aca preguntamos si es es cierto que se esta presionando K_UP si es cierto entonces se ejecuta la funcion vector self.direction que al ser vector tiene dos variables x e y
        if keys[pygame.K_UP]:
            self.direction.y = 1               
        elif keys[pygame.K_DOWN]:
            self.direction.y = -1
        else:
            self.direction.y = 0
            
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0
        
    def update(self):
        self.inputs()
        
        