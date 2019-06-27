'''
@author Mateus R. Moreira
@date 26/06/2019

Faça um programa que leia e reproduza um arquivo 
mp3
''' 
import pygame
pygame.init()
pygame.mixer.music.load('desafio21.mp3')
pygame.mixer.music.play()
pygame.event.wait()
'''
Info: Estes exercícios são tirados do 
curso em video de python. 
'''