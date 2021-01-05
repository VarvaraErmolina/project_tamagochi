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


def hero_move(key, x, y):
    if key == pygame.K_LEFT:
        x -= 10
    elif key == pygame.K_RIGHT:
        x += 10
    elif key == pygame.K_UP:
        y -= 10
    elif key == pygame.K_DOWN:
        y += 10
    return x, y


def main_play():
    FPS = 60
    size = width, height = 800, 650
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Тамагочи')
    bg = load_image("cub.jpg")
    #hero = load_image('calm.png')
    all_sprites = pygame.sprite.Group()
    player = Hero()
    all_sprites.add(player)
    x = 400
    y = 450
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                a = event.key
                x, y = hero_move(a, x, y)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pass
        # screen.blit(hero, (x, y))
        all_sprites.update()
        all_sprites.draw(screen)
        pygame.display.flip()
        screen.blit(bg, (0, 0))


if __name__ == '__main__':
    pygame.init()
    main_play()
    pygame.quit()
