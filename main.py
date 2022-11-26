# Pygame template
import pygame
import random

WIDTH = 360
HEIGHT = 480
FPS = 60

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0,)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

# Inicia o Pygame e cria uma janela
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Projeto Topásio")
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    # Travar o FPS
    clock.tick(FPS)
    # Eventos (commandos dados pelo player)
    for event in pygame.event.get():
        # Verificar se é necessário fechar a janela
        if event.type == pygame.QUIT:
            running = False

    # Update

    # Render
    screen.fill(PRETO)
    # Depois de rederizar tudo, "virar"/mostrar as cartas (os objetos)
    pygame.display.flip()

pygame.quit()
