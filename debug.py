from dis import dis
import pygame
pygame.init()

# creamos un objeto font
# entendimiento del formato (modulo general).(modulo font dentro del modulo general).(Objeto)
# los objetos son instancias de una clase las cuales poseen atributos
font = pygame.font.Font(None,30)

# creamos una funcion que tendra 3 variables info, y, x
def debug(info, y = 10, x = 10):
    # esta funcion get_surface nos devolvera una referencia de la superficie de visualizacion actualmente establecida
    display_surface = pygame.display.get_surface()
    # dibuja un texto en una nueva superficie establecida, y le decimos que muetre lo que este en la variable
    # info la cual debe estar en typo string, queremos que tenga antialias(que los pixeles de los bordes del texto esten desenfocados)
    # y por ultimo el color de la letra
    debug_surf = font.render(str(info), True, 'White')
    # ubicacion de la nueva superficie creada con render(), y le damos las variables brindadas al llamar la funcion
    debug_rect = debug_surf.get_rect(topleft = (x,y))
    # pygame.draw es un modulo para crear formas, lo usaremos para crear el cuadro de texto
    pygame.draw.rect(display_surface,'Black', debug_rect)
    display_surface.blit(debug_surf, debug_rect)