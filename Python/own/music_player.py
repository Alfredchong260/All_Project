#!/usr/bin/python3
import time
import pygame

file = r'/home/cms/Song/Music/KOMOREBIMTAKU.mp3'
pygame.mixer.init()
print('正在播放', file)
track = pygame.mixer.music.load(file)
pygame.mixer.music.play()
time.sleep(130)
pygame.mixer.music.stop()
