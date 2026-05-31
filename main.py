import pygame
from random import randint

White = (255, 255, 255)
Blue = (0, 0, 255)
Red = (255, 0, 0)
Green = (0, 255, 0)
Yellow = (255, 255, 0)
FPS = 60
pygame.init()
screen = pygame.display.set_mode((1200, 500))
clock = pygame.time.Clock()

player_img = pygame.image.load("Ukraine.png")
player_img = pygame.transform.scale(player_img, (100, 100))

player_bg = pygame.surface.Surface((1200, 500))
player_bg.fill(White)
class Player:
    def __init__(self):
        self.image = player_img

        self.rect = pygame.Rect(0, 0, 100, 100)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
player = Player()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.blit(player_bg, (0, 0))
    player.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
