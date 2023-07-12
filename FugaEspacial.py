"""
Jogo: Fuga Espacial
Descrição: Um grupo de diplomatas escapam de uma fortaleza estrelar a bordo de uma nave danificada.
    A nave precisa se desviar das ameaças e sobreviver até atingir a zona de segurança diplomática.
"""

import pygame

class Game:
    screen = None
    screen_size = None
    width = 800
    height = 600
    run = True
    background = None

    def __init__(self, size, fullscreen):...

"""
Função que inicializa o pygame, define a resolução da tela,
caption e desabilita o mouse.
"""
pygame.init() #inicia o pygame

self.screen = pygame.display.set_mode((self.width, self.height)) #tamanho da tela
self.screen_size = self.screen.get_size() #define tamanho da tela do jogo

pygame.mouse.set_visible(0) #desabilita mouse
pygame.display.set_caption('Fuga Espacial')



def handle_events(self):
    """
    Trata o evento e toma a ação necessária.
    """
    for event in pygame.event.get():
          if event.type == pygame.QUIT:
                self.run = False #trata a saída do jogo
#handle_events()

def elements_update(self, dt):
        self.background.update(dt) #Atualiza elementos
#elements_update()

    def elements_draw(self):
        self.background.draw(self,screen) #define elementos
    #elements_draw()

    def loop(self):...
    #loop()
#Game