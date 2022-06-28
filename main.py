import pygame, sys
from debug import debug
from settings import *
from level import Level
from debug import debug

class Game:
    # funcion inicializar la ventana o pantalla
    def __init__(self):
        pygame.init()
        # general setup
        self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
        # llamamos un o creamos un objeto que luego nos permitira seguir el paso del tiempo Framerate
        self.clock = pygame.time.Clock()
        self.name = pygame.display.set_caption("Pepito")
        # creamos una instancia u objeto de nuestro clase Level
        self.level = Level()
    
    # funcion que nos dira cuando corre o no corre el juego
    def run(self):
        # mientras sea verdadero es como decirle que entre en un loop que nunca salga
        while True:
            # creamos una variable evento que revise cada evento del programa
            for event in pygame.event.get():
                # si uno de esos eventos es pygame.QUIT cerramos pygame y paramos de correr el codigo
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()      
            # actualizar el screen
            pygame.display.update()
            # que color queremos que tenga la pantalla al iniciar
            self.screen.fill('black')
            # le decimos que corra las instancias
            self.level.run()
            # llamamos al objeto creado en la linea 11 y le decimos que la velocidad sea la de la variable FPS creada en settings
            self.clock.tick(FPS)



# le decimos que mientras que el programa se abra desde aca, que la clase Game() se llame game y que ejecute el game.run()
if __name__=="__main__":
    game = Game()
    game.run()
