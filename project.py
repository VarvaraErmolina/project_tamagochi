import pygame
import os
import sys
import random
import datetime


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
    file = open("data/info.txt", 'w')
    file.write(f'{indicators[0]}\n{indicators[1]}\n{indicators[2]}\n{indicators[3]}\n{indicators[4]}\n{indicators[5]}')
    file.close()
    pygame.quit()
    sys.exit()


def start_play():
    starting_play_bg = pygame.transform.scale(load_image('fon_menu.jpg'), (800, 650))
    screen.blit(starting_play_bg, (0, 0))
    running = True
    start_text = ['Выбери персонажа', "", "", "", '              Ок']
    font = pygame.font.Font(None, 100)
    text_coord = 75
    pet = ''
    for line in start_text:
        string_rendered = font.render(line, True, (0, 0, 0))
        intro_rect = string_rendered.get_rect()
        text_coord += 13
        intro_rect.top = text_coord
        intro_rect.x = 70
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    clock = pygame.time.Clock()
    menu_hero = pygame.sprite.Group()
    one = pygame.sprite.Sprite()
    one.image = load_image("dark_calm.png")
    one.rect = one.image.get_rect()
    one.rect.x = 100
    one.rect.y = 200
    menu_hero.add(one)
    mam = pygame.sprite.Sprite()
    mam.image = load_image("dark_mam_calm.png")
    mam.rect = mam.image.get_rect()
    mam.rect.x = 300
    mam.rect.y = 215
    menu_hero.add(mam)
    meme = pygame.sprite.Sprite()
    meme.image = load_image("dark_meme_calm.png")
    meme.rect = meme.image.get_rect()
    meme.rect.x = 500
    meme.rect.y = 215
    menu_hero.add(meme)
    menu_hero.draw(screen)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                coor_in_start_play = event.pos
                if pet == '':
                    if 100 < coor_in_start_play[0] < 298 and 200 < coor_in_start_play[1] < 415:
                        one.image = load_image('big_calm.png')
                        mam.image = load_image("dark_mam_calm.png")
                        meme.image = load_image("dark_meme_calm.png")
                        pet = 'one'
                    elif 330 < coor_in_start_play[0] < 475 and 215 < coor_in_start_play[1] < 398:
                        mam.image = load_image("big_mam_calm.png")
                        one.image = load_image("dark_calm.png")
                        meme.image = load_image("dark_meme_calm.png")
                        pet = 'mam'
                    elif 510 < coor_in_start_play[0] < 665 and 220 < coor_in_start_play[1] < 400:
                        meme.image = load_image("big_meme_calm.png")
                        mam.image = load_image("dark_mam_calm.png")
                        one.image = load_image("dark_calm.png")
                        pet = 'meme'
                    menu_hero.draw(screen)
                elif pet != '' and 340 < coor_in_start_play[0] < 430 and 431 < coor_in_start_play[1] < 450:
                    return pet
            pygame.display.flip()
            clock.tick(FPS)


def happy_ending(pet):
    text_win = ['Вы отлично ухаживали за питомцем,', 'он вырос здоровым и счастливым!']
    menu_bg = pygame.transform.scale(load_image('fon_menu.jpg'), (800, 650))
    screen.blit(menu_bg, (0, 0))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 50)
    text_coord = 110
    running = True

    if pet == 'one':
        image = load_image('big_calm.png')
        screen.blit(image, (100, 250))
    elif pet == 'mam':
        image = load_image('big_mam_calm.png')
        screen.blit(image, (50, 200))
    elif pet == 'meme':
        image = load_image('big_meme_calm.png')
        screen.blit(image, (0, 150))

    pygame.mixer.music.stop()
    good_sound = pygame.mixer.Sound('good.mp3')
    good_sound.set_volume(0.7)
    good_sound.play()

    for line in text_win:
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
                file = open("data/info.txt", 'w')
                file.write('')
                file.close()
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                file = open("data/info.txt", 'w')
                file.write('')
                file.close()
                pygame.quit()
        pygame.display.flip()
        clock.tick(FPS)


def sad_ending(pet):
    pygame.init()
    text_win = ['К сожалению, вы плохо ухаживали', 'за питомцем, и он ушел.']
    menu_bg = pygame.transform.scale(load_image('fon_menu.jpg'), (800, 650))
    screen.blit(menu_bg, (0, 0))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 50)
    text_coord = 110
    running = True

    if pet == 'one':
        image = load_image('mem_leave.png')
        screen.blit(image, (100, 250))
    elif pet == 'mam':
        image = load_image('meme_leave.png')
        screen.blit(image, (50, 200))
    elif pet == 'meme':
        image = load_image('mam_leave.png')
        screen.blit(image, (0, 150))

    pygame.mixer.music.stop()
    bad_sound = pygame.mixer.Sound('bad.mp3')
    bad_sound.set_volume(0.5)
    bad_sound.play()

    for line in text_win:
        string_rendered = font.render(line, True, (0, 0, 0))
        intro_rect = string_rendered.get_rect()
        text_coord += 50
        intro_rect.top = text_coord
        intro_rect.x = 50
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    pygame.display.flip()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                file = open("data/info.txt", 'w')
                file.write('')
                file.close()
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                file = open("data/info.txt", 'w')
                file.write('')
                file.close()
                pygame.quit()
        clock.tick(FPS)


def open_information():
    file = open('data/info.txt', mode='r')
    text = file.read().split('\n')
    if text == ['']:
        eat = 100
        sleep = 100
        clean = 100
        time = ''.join(str(datetime.datetime.now()))
        first_time = time
        pet = start_play()
    else:
        time = ''.join(str(datetime.datetime.now()))
        old_time = text[4]
        minus = (int(time[8:10]) - int(old_time[8:10])) * 24 + (int(time[11:13]) - int(old_time[11:13]))
        eat = int(text[0]) - minus
        sleep = int(text[1]) - minus
        clean = int(text[2]) - minus
        pet = text[3]
        first_time = text[5]
    if eat > 0 or sleep > 0 or clean > 0:
        if (int(time[8:10]) - int(first_time[8:10])) * 24 + (int(time[11:13]) - int(first_time[11:13])) >= 168:
            happy_ending(pet)
        else:
            return eat, sleep, clean, pet, time, first_time
    elif eat <= 0 or sleep <= 0 or clean <= 0:
        sad_ending(pet)
    return eat, sleep, clean, pet, time, first_time


def start_menu():
    FPS = 60
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
    rul = ['Правила', '1. Ухаживай за питомцем,', 'нажимая на предметы в комнате',
           '2. Перемещай питомца по комнате,', 'используя мышку']
    menu_bg = pygame.transform.scale(load_image('fon_menu.jpg'), (800, 650))
    screen.blit(menu_bg, (0, 0))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 50)
    text_coord = 50
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
                start_menu()
        pygame.display.flip()
        clock.tick(FPS)


class Particle(pygame.sprite.Sprite):

    def __init__(self, pos, dx, dy):
        super().__init__(bub_sprites)
        self.image = random.choice(particles)
        self.rect = self.image.get_rect()
        self.velocity = [dx, dy]
        self.rect.x, self.rect.y = pos
        self.gravity = 2

    def update(self):
        screen_rect = (0, 0, 800, 650)
        self.velocity[1] += self.gravity
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        if not self.rect.colliderect(screen_rect):
            self.kill()


def create_particles(position):
    particle_count = 30
    numbers = range(-10, 10)
    for _ in range(particle_count):
        Particle(position, random.choice(numbers), random.choice(numbers))


class Hero(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        pet = indicators[3]
        if pet == 'one':
            self.image = load_image('calm.png')
            self.image_sleep = load_image('sleep.png')
            self.image_food = load_image('food.png')
        elif pet == 'meme':
            self.image = load_image('meme_calm.png')
            self.image_sleep = load_image('meme_sleep.png')
            self.image_food = load_image('meme_food.png')
        elif pet == 'mam':
            self.image = load_image('mam_calm.png')
            self.image_sleep = load_image('mam_sleep.png')
            self.image_food = load_image('mam_food.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = 400
        self.rect.bottom = 500
        self.speedx = 0
        self.speedy = 0

    def update(self, x1, y1):
        pet = indicators[3]

        shower_sound = pygame.mixer.Sound('shower.mp3')
        sleep_sound = pygame.mixer.Sound('sleep.mp3')
        food_sound = pygame.mixer.Sound('food.mp3')
        shower_sound.set_volume(0.7)
        sleep_sound.set_volume(0.8)
        food_sound.set_volume(0.7)

        if pet == 'one':
            self.image = load_image('calm.png')
        elif pet == 'meme':
            self.image = load_image('meme_calm.png')
        elif pet == 'mam':
            self.image = load_image('mam_calm.png')
        if 110 < x1 < 250 and 250 < y1 < 350:
            self.rect.centerx = x1
            self.rect.centery = y1
        elif 250 < x1 < 350 and 225 < y1 < 275:
            self.rect.centerx = x1
            self.rect.centery = y1
        elif 220 < x1 < 250 and 250 < y1 < 500:
            self.rect.centerx = x1
            self.rect.centery = y1
        elif 250 < x1 < 500 and 450 < y1 < 550:
            self.rect.centerx = x1
            self.rect.centery = y1
        elif 350 < x1 < 450 and 400 < y1 < 450:
            self.rect.centerx = x1
            self.rect.centery = y1
        elif 350 < x1 < 500 and 550 < y1 < 575:
            self.rect.centerx = x1
            self.rect.centery = y1
        elif 500 < x1 < 600 and 500 < y1 < 550:
            self.rect.centerx = x1
            self.rect.centery = y1
        elif 175 < x1 < 300 and 175 < y1 < 250 or \
                225 < x1 < 300 and 150 < y1 < 200:
            sleep_sound.play()
            self.rect.centerx = x1
            self.rect.centery = y1
            self.image = self.image_sleep
        elif 275 < x1 < 350 and 350 < y1 < 450:
            shower_sound.play()
            create_particles((x1, y1))
            self.rect.centerx = 800
            self.rect.centery = 800
        elif 450 < x1 < 575 and 400 < y1 < 475:
            food_sound.play()
            self.rect.centerx = x1
            self.rect.centery = y1
            self.image = self.image_food


def main_play():
    bg = load_image("cub.jpg")
    all_sprites = pygame.sprite.Group()
    player = Hero()
    food_icon = load_image('food_icon.png')
    sleep_icon = load_image('sleep_icon.png')
    soap_icon = load_image('soap_icon.png')
    all_sprites.add(player)

    font = pygame.font.SysFont("jokerman", 40)
    scale_food = font.render("100", True, (255, 255, 255))
    scale_sleep = font.render("100", True, (255, 255, 255))
    scale_soap = font.render("100", True, (255, 255, 255))
    pygame.mouse.set_visible(False)

    cursor_img = load_image('arrow.png')
    hand_cursor_img = load_image('hand.png')
    cursor_img_rect = cursor_img.get_rect()

    running = True
    clock = pygame.time.Clock()
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x1, y1 = pygame.mouse.get_pos()
                all_sprites.update(x1, y1)

        cursor_img_rect.x, cursor_img_rect.y = pygame.mouse.get_pos()
        if 175 < cursor_img_rect.x < 300 and 175 < cursor_img_rect.y < 250 or \
                225 < cursor_img_rect.x < 300 and 150 < cursor_img_rect.y < 200:
            screen.blit(hand_cursor_img, cursor_img_rect)
        elif 275 < cursor_img_rect.x < 350 and 350 < cursor_img_rect.y < 450:
            screen.blit(hand_cursor_img, cursor_img_rect)
        elif 450 < cursor_img_rect.x < 575 and 400 < cursor_img_rect.y < 475:
            screen.blit(hand_cursor_img, cursor_img_rect)
        else:
            screen.blit(cursor_img, cursor_img_rect)

        bub_sprites.update()
        bub_sprites.draw(screen)
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(50)
        screen.blit(bg, (0, 0))

        screen.blit(food_icon, (690, 120))
        screen.blit(sleep_icon, (690, 250))
        screen.blit(soap_icon, (700, 400))

        screen.blit(scale_food, (705, 200))
        screen.blit(scale_sleep, (705, 330))
        screen.blit(scale_soap, (705, 475))


if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 650
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Тамагочи')
    FPS = 60

    pygame.mixer.music.load('copycat.mp3')
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(loops=-1)

    particles = [load_image("bubble.png")]
    for scale in (5, 10, 20):
        particles.append(pygame.transform.scale(particles[0], (scale, scale)))
    bub_sprites = pygame.sprite.Group()

    var = start_menu()
    if var == 'Игра':
        indicators = open_information()
        main_play()
    elif var == 'Правила':
        rules()
    pygame.quit()
