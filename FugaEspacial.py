import pygame
import time  #função membro time.sleep(...
import random  #biblioteca utilizada para gerar numeros aleatorios
import os  #função membro OS.path.isfile(...) em play_soundtrack
import sys

class Background:
    """Define plano de fundo do jogo"""
    image = None  #atributo
    margin_left = None
    margin_right = None

    def __init__(self):
        background_fig = pygame.image.load("Images/background.png")
        background_fig.convert()  #adapta a imagem no formato do nosso display
        background_fig = pygame.transform.scale(background_fig, (800, 602))
        self.image = background_fig  #atribui a imagem para o background

        # mergea a imagem na esquerda
        margin_left_fig = pygame.image.load("Images/margin_1.png")  #cria a variável e carrega a imagens do diretorio
        margin_left_fig.convert()  #formato aceitavel
        margin_left_fig = pygame.transform.scale(margin_left_fig, (60, 602))  #ajusta no tamanho da imagem
        self.margin_left = margin_left_fig  #jogamos a imagem manipulada para o atributo referenciando através do SELF.

        #insere imagem na direita
        margin_right_fig = pygame.image.load("Images/margin_2.png")
        margin_right_fig.convert()
        margin_right_fig = pygame.transform.scale(margin_right_fig, (60, 602))
        self.margin_right = margin_right_fig

    def update(self, dt):
        pass  #ainda não faz nada

    def draw(self, screen):
        screen.blit(self.image, (0, 0))  #copiar de uma imagem para outra. / Copia a imagem que eu quero para a posição desejada
        screen.blit(self.margin_left, (0, 0))  #60 depois da primeira margem
        screen.blit(self.margin_right, (740, 0))  #60 depois da primeira margem

    def move(self, screen, scr_height, movL_x, movL_y, movR_x, movR_y):
        for i in range(0, 2):
            screen.blit(self.image, (movL_x, movL_y - i * scr_height))
            screen.blit(self.margin_left, (movL_x, movL_y - i * scr_height))
            screen.blit(self.margin_right, (movR_x, movR_y - i * scr_height))

class Player:  #classe que define o jogador
    image = None  #inicializa os atributos
    x = None
    y = None

    def __init__(self, x, y):
        player_fig = pygame.image.load("Images/player.png")
        player_fig.convert()
        player_fig = pygame.transform.scale(player_fig, (90, 90))
        self.image = player_fig
        self.x = x
        self.y = y

    def draw(self, screen, x, y): #metodo que desenha o player
        screen.blit(self.image, (x, y))

#gera/gerir os obstculos/ameaças ao jogador
class Hazard:
    image = None
    x = None
    y = None

    def __init__(self, img, x, y):
        hazard_fig = pygame.image.load(img)
        hazard_fig.convert()
        hazard_fig = pygame.transform.scale(hazard_fig, (130, 130))
        self.image = hazard_fig
        self.x = x
        self.y = y
    # __init__()

    def draw(self, screen, x, y):
        screen.blit(self.image, (x, y))
    # draw()
# Hazard:

class Game:
    screen = None
    screen_size = None
    width = 800
    height = 600
    run = True
    background = None
    player = None  #atributo player
    hazard = []  #atributo da ameaça ao player
    render_text_bateulateral = None
    render_text_perdeu = None
    #soundtrack = None


    #movimento do Player
    #DIREITA = pygame.K_RIGHT
    #ESQUERDA = pygame.K_LEFT
    mudar_x = 0.0

    def __init__(self, size, fullsceen):
        """Função que inicializa o pygame, define a resolução da tela, caption e desabilita o mouse"""
        pygame.init()

        self.screen = pygame.display.set_mode((self.width, self.height))  #Define o tamanho da tela
        self.screen_size = self.screen.get_size()  #define o tamanho da tela do jogo

        pygame.mouse.set_visible(0)  #desabilita mouse
        pygame.display.set_caption('Fulga Espacial')  #define a caption da janela do jogo

        my_font = pygame.font.Font("Fonts/Fonte4.ttf", 100)  #define a fonte

        self.render_text_bateulateral = my_font.render("VACILOU!!", 0, (255, 255, 255)) #@texto não está centralizado
        self.render_text_perdeu = my_font.render("VIROU POEIRA!)", 0, (255, 0, 0))  #texto opaco/translucido informando fim dojogo
    #init()

    def handle_events(self):  #trata a saída do jogo
        """Trava o evento e toma a ação necessária"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False

            if event.type == pygame.KEYDOWN:  #se clicar em qlq tecla, entra no if
                if event.key == pygame.K_LEFT:  #na seta da esquerda, anda 3 espaços no eixo X.
                    self.mudar_x = -3
                if event.key == pygame.K_RIGHT:  #na seta da direita, anda 3 espaços no eixo X.
                    self.mudar_x = 3

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    self.mudar_x = 0
    #  handle_events()

    def elements_update(self, dt):  #atualiza os elementos
        self.background.update(dt)

    def elememnts_draw(self):  #desenha os elementos
        self.background.draw(self.screen)
#######################################################################
    def score_card(self, screen, h_passou, score):
        font = pygame.font.SysFont(None, 35)  #define e renderiza os textos
        passou = font.render("Passou: " + str(h_passou), True, (255, 255, 128))
        score = font.render("Score: " + str(score), True, (253, 231, 32))
        screen.blit(passou, (0, 50))  #sobrepõe os textos na tela
        screen.blit(score, (0, 100))  #sobrepõe os textos na tela
    #  score_card()

    def play_soundtrack(self):
        if os.path.isfile('Sounds/song.wav'):  #inclui trilha sonora. Confere se o arquivo existe
            pygame.mixer.music.load('Sounds/song.wav')  #carrega o arquivo
            pygame.mixer.music.set_volume(0.5)  #ajusta o volume do som
            pygame.mixer.music.play(loops=-1)  #coloca para rodar infinitamente
        else:  #mostra mensagem de erro caso o arquivo não exista
            print('Sounds/song.mp3 not found... ignoring', file=sys.stderr)
    # play_soundtrack()

    def play_sound(self, sound):
        if os.path.isfile(sound):  #inclui trilha sonora. Confere se o arquivo existe
            pygame.mixer.music.load(sound)  #carrega o arquivo
            pygame.mixer.music.set_volume(0.5)  #ajusta o volume do som
            pygame.mixer.music.play()  #coloca para rodar infinitamente
        else:  #mostra mensagem de erro caso o arquivo não exista
            print('Sounds/song.mp3 not found... ignoring', file=sys.stderr)
    # play_sound()

    def draw_explosion(self, screen, x, y):
        explosion_fig = pygame.image.load("Images/explosion.png")
        explosion_fig.convert()
        explosion_fig = pygame.transform.scale(explosion_fig, (150, 150))
        screen.blit(explosion_fig, (x, y))
    # draw_exploosion()

######################################################################
    def loop(self):
        """Função do Laço principal"""
        velocidade_background = 10  #variavel para movimento do plano de fundo
        #movimento da margem esquerda
        movL_x = 0
        movL_y = 0
        
        #movimento da margem direita
        movR_x = 740
        movR_y = 0

        #*Movimentação das ameaças do jogo*
        velocidade_hazard = 10  #variavel para velocidade da atualização das amaeças
        hzrd = 0
        h_x = random.randrange(125, 660)
        h_y = -500
        #Info Hazard, referente as diemenões da imagens do obstaculo
        h_width = 100
        h_height = 110

        #*Inicializa variáveis da pontuação*
        score = 0
        h_passou = 0

        self.background = Background()  #cria o plano de fundo cria o objeto background
        self.play_soundtrack()  #inclui trilha sonora

        x = (self.width - 56) / 2  #posição do player
        y = (self.height - 125)

        self.player = Player(x, y)  #cria player

        # criando o hazard
        self.hazard.append(Hazard("Images/satelite.png", h_x, h_y))
        self.hazard.append(Hazard("Images/nave.png", h_x, h_y))
        self.hazard.append(Hazard("Images/cometaVermelho.png", h_x, h_y))
        self.hazard.append(Hazard("Images/meteoros.png", h_x, h_y))
        self.hazard.append(Hazard("Images/buracoNegro.png", h_x, h_y))

        clock = pygame.time.Clock()  #inicia o relogio e a dt(delta time - ms) que vai limitar o valor de FPS
        dt = 16

        while self.run:  #inicio do loop principal
            clock.tick(1000 / dt)  #controla o n° máximo de FPS
            self.handle_events()  #trava eventos, lida com a entrada de eventos
            self.elements_update(dt)  #atualiza os elementos
            self.elememnts_draw()  #desenha o bacground buffer, desenha elementos

            self.background.move(self.screen, self.height, movL_x, movL_y, movR_x, movR_y)  # @
            movL_y = movL_y + velocidade_background
            movR_y = movR_y + velocidade_background

            # se a imagem ultrapassar a extremidade da tela, mova de volta. Garante que a imagem de fundo esteja sempre em movimento
            if movL_y > 600 and movR_y > 600:
                movL_y -= 600
                movR_y -= 600

            #*Movimentação do Player*
            #muda a coordenada "X" da Nave concordando com as mudanças na função event_handle()
            x = x + self.mudar_x  #muda a posição do Player

            #*Chama a função player.draw() no laço principal da classe Game:*
            self.player.draw(self.screen, x, y)  #desenha o player pelo metodo Draw()
            self.score_card(self.screen, h_passou, score)  #mostra a pontuação. chama a função score_card


            #*Retrições do movimento do Player*
            if x > 760 - 92 or x < 40 + 5:  #se o Player bate na lateral não é Game Over
                self.play_sound('Sounds/jump2.wav')  # adciona/chama a função do som de colisão na margem
                self.screen.blit(self.render_text_bateulateral, (80, 200))
                pygame.display.update()  #atualizar a tela
                time.sleep(3)
                self.loop()
                self.run = False


            #adiciona movimento ao hazard
            h_y = h_y + velocidade_hazard / 4  #atualiza a posição e velocidade. Mova para baixo
            self.hazard[hzrd].draw(self.screen, h_x, h_y)  #chama o método draw() para desenhar o hazard em nova posição
            h_y = h_y + velocidade_hazard  #garante que continue se movendo em vel constate a cada quadro

            #*Define onde hazard vai aparecer, recomeça a posição do obstaculo e da faixa
            if h_y > self.height:  #verifica se a ameaça passou da altura da tela.
                h_y = 0 - h_height  #redefine a posição vertical do hazard para o topo da tela (0) menos a altura do próprio hazard.
                h_x = random.randrange(125, 650 - h_height)  #add movimento ao objeto Hazazrd. Atualiza sua posição na tela e reinicia sua posição e tipo aleatoriamente quando ele passa da altura da tela.
                hzrd = random.randint(0, 4)
                #determina quantos hazard passaram e a pontuação
                h_passou = h_passou + 1  #faz o acescimo dos valores
                score = h_passou * 10

            ####################
            player_rect = self.player.image.get_rect()  #colisão e Game Over
            player_rect.topleft = (x, y)
            hazard_rect = self.hazard[hzrd].image.get_rect()
            hazard_rect.topleft = (h_x, h_y)

            if hazard_rect.colliderect(player_rect):  #condiçao para a colisão
                self.play_sound('Sounds/crash.wav')  #chamando o som de colisão
                # exibe a imagem de explosão
                self.draw_explosion(self.screen, x - (self.player.image.get_width() / 2), y - (self.player.image.get_height()))
                self.screen.blit(self.render_text_perdeu, (80, 200))  #exibe a mensagem de Game Over
                pygame.display.update()
                time.sleep(3)
                self.run = False
            ####################

            pygame.display.update()  #atualiza a tela, com argumento de 2000 quadros por segundos
            clock.tick(2000)  #evita q ñ seja atualizado numa velocidade muito alta. Assim, limita o uso excessivo dos recursos do sistema/hardware


        # Wile self.run

    # loop()


#*Inicia o jogo: Cria o objeto game e chama o loop básico*
game = Game("resolution", "fullscreen")
game.loop()