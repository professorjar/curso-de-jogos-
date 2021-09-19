#Autor: João Tinti
#Fork : José Alberto Rodrigues 19/09/2021
import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura = 640
altura = 480

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Curso de Python3 Plataforma BVS')

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update()