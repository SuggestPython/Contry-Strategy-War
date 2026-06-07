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

player_img = pygame.image.load("Non_Country.png")
player_img = pygame.transform.scale(player_img, (400, 140))

player_bg = pygame.surface.Surface((1200, 500))
player_bg.fill(Green)
class Player:
    def __init__(self, x, y):
        self.image = player_img
        self.rect = pygame.Rect(x, y, 200, 200)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def lrud(self):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.rect.x -= 10
            if event.key == pygame.K_RIGHT:
                self.rect.x += 10
            if event.key == pygame.K_UP:
                self.rect.y -= 5
            if event.key == pygame.K_DOWN:
                self.rect.y += 5
player = Player(500, 150)
running = True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.lrud()

    screen.blit(player_bg, (0, 0))
    player.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
