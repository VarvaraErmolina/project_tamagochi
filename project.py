import pygame
import os
import sys

FPS = 50


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


def exit():
    pygame.quit()
    sys.exit()


def start_menu():
    menu_text = ['«Главное меню»', 'Играть', 'Правила']
    menu_bg = pygame.transform.scale(load_image('fon_menu.jpg'), (800, 650))
    screen.blit(menu_bg, (0, 0))
    running = True
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 100)
    text_coord = 110
    for line in menu_text:
        string_rendered = font.render(line, True, (0, 0, 0))
        intro_rect = string_rendered.get_rect()
        text_coord += 50
        intro_rect.top = text_coord
        intro_rect.x = 50
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                coor_in_menu = event.pos
                if 270 < coor_in_menu[1] < 350:
                    return 'Игра'
                elif 400 < coor_in_menu[1] < 470:
                    return 'Правила'
        pygame.display.flip()
        clock.tick(FPS)


def rules():
    rul = ['Правила']
    menu_bg = pygame.transform.scale(load_image('fon_menu.jpg'), (800, 650))
    screen.blit(menu_bg, (0, 0))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 100)
    text_coord = 110
    running = True
    for line in rul:
        string_rendered = font.render(line, True, (0, 0, 0))
        intro_rect = string_rendered.get_rect()
        text_coord += 50
        intro_rect.top = text_coord
        intro_rect.x = 50
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                main_screen()
        pygame.display.flip()
        clock.tick(FPS)


def main_screen():
    bg = load_image("cub.jpg")
    running = True
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONUP:
                pass
        pygame.display.flip()
        screen.blit(bg, (0, 0))


if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 650
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Тамагочи')
    var = start_menu()
    if var == 'Игра':
        main_screen()
    elif var == 'Правила':
        rules()
