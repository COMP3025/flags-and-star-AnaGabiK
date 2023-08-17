import sys
import math
import pygame
from pygame.locals import QUIT

pygame.init()

width, height = 400, 300
DISPLAYSURF = pygame.display.set_mode((width, height))

green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)

def draw_star(screen, position, size, angle):
  center_x, center_y = position

  raio = size
  raio_dentro = round(raio / 2)
  pontos_dentro = []
  pontos_fora = []
  for i in range(5):
    angulo = math.radians(angle + i * 72)  # Convertendo para radianos
    x = center_x + raio * math.cos(angulo)
    y = center_y - raio * math.sin(angulo)
    pontos_fora.append((int(x), int(y)))
  for i in range(5):
    angulo = math.radians(angle + 36 + (i * 72))  # Convertendo para radianos
    x = center_x + raio_dentro * math.cos(angulo)
    y = center_y - raio_dentro * math.sin(angulo)
    pontos_dentro.append((int(x), int(y)))

  pontos = []
  for i in range(5):
    pontos.append(pontos_fora[i])
    pontos.append(pontos_dentro[i])

  #print(pontos)
  for _ in range(5):
    pygame.draw.polygon(screen, white, pontos, 0)


while True:
  pygame.draw.rect(DISPLAYSURF, white, (30, 30, 250, 80))
  pygame.draw.rect(DISPLAYSURF, red, (30, 110, 250, 80))
  pygame.draw.rect(DISPLAYSURF, blue, (30, 30, 80, 80))

  draw_star(DISPLAYSURF, (70, 70), 20, 90)

  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
  pygame.display.update()
