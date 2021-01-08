import pygame
import os
import sys

bed_x = (200, 300)
bed_y = (150, 250)


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Hero(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image('calm.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = 400
        self.rect.bottom = 500
        self.speedx = 0
        self.speedy = 0

    def update(self):
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -4
        if keystate[pygame.K_RIGHT]:
            self.speedx = 4
        if keystate[pygame.K_DOWN]:
            self.speedy = 4
        if keystate[pygame.K_UP]:
            self.speedy = -4
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.right > 700:
            self.rect.right = 700
        if self.rect.left < 0:
            self.rect.left = 0


def main_play():
    FPS = 60
    size = width, height = 800, 650
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Тамагочи')
    bg = load_image("cub.jpg")
    all_sprites = pygame.sprite.Group()
    player = Hero()
    all_sprites.add(player)

    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pass
        all_sprites.update()
        all_sprites.draw(screen)
        pygame.display.flip()
        screen.blit(bg, (0, 0))


if __name__ == '__main__':
    pygame.init()
    main_play()
    pygame.quit()
