#import pygame
import sys

#pygame.init() # запуск движка
#pygame.mixer.init()
#length=640
#width=480
#screen=pygame.display.set_mode((width,length))
#clock=pygame.time.Clock()
#while 1:
#    for event in pygame.event.get():
#        if event.type ==pygame.QUIT:
#            break
#pygame.quit()
import pygame
import random
import time
import math
class Player(pygame.sprite.Sprite):#
    def __init__(self, image, y_lim = 220):#создание и определение его свойств
        self.y_lim = y_lim
        pygame.sprite.Sprite.__init__(self)#создание спрайта
        self.image = image #pygame.Surface((50, 50))#создать поверхность
        self.image.set_colorkey((0, 0, 0))
        #self.image.fill((255, 20, 50))#создать цвет
        self.rect = self.image.get_rect()#создать рамку для движения
        self.rect.center = (240, 288)#где появиться

    def update(self, image, x_dir, y_dir):#def=метод функция для движения
        self.rect.x = self.rect.x + 1*x_dir#двигаться вправо
        if self.rect.x > width + 10:#если вышел за пределы вернуться
            self.rect.x = -9
        if self.rect.x < 0 - 10:#если вышел за пределы вернуться
            self.rect.x = width
        self.rect.y = self.rect.y + 1*y_dir#двигаться вниз
        if self.rect.y > self.y_lim:#если вышел за пределы вернуться
            self.rect.y = self.y_lim
        if self.rect.y < 0:#если вышел за пределы вернуться
            self.rect.y = length
        self.image = image
        self.image.set_colorkey((0, 0, 0))
        #print(self.rect.x, self.rect.y)

pygame.init() # запуск
lol = 0
pygame.mixer.init()
length=576
width=480
sound2 =pygame.mixer.Sound("mr-beast-scream.mp3")
sound3 =pygame.mixer.Sound("trim_trim_online-audio-converter.mp3")
screen = pygame.display.set_mode((length, width))
clock=pygame.time.Clock()
minigun = 0
tube = 2
lbad = 1
rbad = 1
mushroom_img = pygame.image.load("555.png").convert()
player_img = pygame.image.load("01.png").convert()# текстура персонажа
bullet_img = pygame.image.load("bullet.png").convert()
super_bullet_img = pygame.image.load("super bullet.png").convert()
background=pygame.image.load("definitely not the background.jpg")# фон
bg_x = background.get_width()
screen_height = background.get_height()
screen_width = background.get_width()
shooting = 0
mushroomdead = 0
bullet_x = 0#координата х пули
super_bullet_x = 0#координата х пули
length=screen_height
width=screen_width
screen=pygame.display.set_mode((background.get_width(),background.get_height()))#
player=Player(player_img)#создать спрайта игрока
bullet=Player(bullet_img, 600)
super_bullet=Player(super_bullet_img, 600)
mushroom = Player(mushroom_img, 600)
sprites=pygame.sprite.Group()#создать группу спрайтов
sprites.add(player, bullet, super_bullet, mushroom)#добавить его в группу
bullet.image = bullet_img
xdir = 0
ydir = 0
distance = 0
super_distance = 0
dead = 0
bullet.rect.y = 500#где спавн?
bullet.rect.x = 5000
super_bullet.rect.y = 500
super_bullet.rect.x = 5000
mushroom.rect.x = 500
moving = 0
jumping = 0
direction = 'l'
randy = 0
counter = 0
randside = random.randint(1, 2)
if randside == 1:
    mushroom_x = 1 + counter/10
else:
    mushroom_x = -1 - counter/10
background = pygame.image.load("start.png")
screen = pygame.display.set_mode((800, 600))
cond = 0
font = pygame.font.Font('freesansbold.ttf', 32)
text = "Score: "
while 1:
    clock.tick(72)
    if cond == 0:
        screen.blit(background, (0, 0))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break
            elif event.type == pygame.KEYDOWN:  # если нажата клавиша
                if event.key == pygame.K_q:
                    sys.exit()
                if event.key == pygame.K_RETURN:
                    screen = pygame.display.set_mode((576, 375))
                    background = pygame.image.load("definitely not the background.jpg")
                    cond = 1
    elif cond == 1:
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                break
            elif event.type == pygame.KEYDOWN:#если нажата клавиша
                if event.key == pygame.K_q:
                    sys.exit()
                if event.key == pygame.K_LEFT:
                    xdir = -1 * tube
                    #sound2.play()
                    moving = 1
                    direction = 'l'
                if event.key == pygame.K_RIGHT:
                    xdir = 1 * tube
                    #xdir = 1
                    moving = 1
                    direction = 'r'
                if event.key == pygame.K_UP:
                    ydir = 0
                    if jumping == 0:
                        start = time.time()
                    jumping = 2  # jumping
                if event.key == pygame.K_o:
                    xdir = 0
                    ydir = 0
                    moving = 0
                    minigun = 1
                    tube = 1
                if event.key == pygame.K_p:
                    minigun = 0
                    shooting = 0
                    tube = 2
                if event.key == pygame.K_x and shooting == 1:
                    randy = 5 - random.randrange(0, 10)#задать 5-чо то чо то=от 0 до 10
                    if direction == "r" and rbad == 1:
                        rbad = 0
                        bullet.rect.y = player.rect.y + 50 + randy
                        bullet.rect.x = player.rect.x + 50
                        bullet_x = 5
                    elif direction == "l" and lbad == 1:
                        lbad = 0
                        super_bullet.rect.y = player.rect.y + 50 + randy
                        super_bullet.rect.x = player.rect.x + 10
                        super_bullet_x = -5
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    xdir = 0
                    moving = 0
                if event.key == pygame.K_RIGHT:
                    xdir = 0
                    moving = 0
                if event.key == pygame.K_DOWN:
                    ydir = 0

        if bullet.rect.x > width:#если пуля вышла за пределы исчезнуть
            bullet.rect.y = 500
            bullet_x = 0
            rbad = 1
        if super_bullet.rect.x < 0:
            super_bullet.rect.y = 500
            super_bullet_x = 0
            lbad = 1
        if mushroom_x < 0:
            if (lol // 18) % 2 == 0:
                mushroom_img = pygame.image.load("555.png").convert()
            else:
                mushroom_img = pygame.image.load("mushrooom.png").convert()
        elif mushroom_x > 0:
            if (lol // 18) % 2 == 0:
                mushroom_img = pygame.image.load("ovosh.png").convert()
            else:
                mushroom_img = pygame.image.load("drysh.png").convert()

        if moving == 1 and direction == 'l':
            if (lol//18)%2== 0:
                player_img = pygame.image.load("01.png").convert()
                bullet.image = bullet_img
            else:
                player_img = pygame.image.load("03.png").convert()
                bullet.image = bullet_img
        elif moving == 0 and direction == 'l':
            player_img = pygame.image.load("01.png").convert()
        elif moving == 1 and direction == 'r':
            if (lol//18)%2== 0:
                player_img = pygame.image.load("02.png").convert()
            else:
                player_img = pygame.image.load("04.png").convert()
        elif moving == 0 and direction == 'r':
            player_img = pygame.image.load("02.png").convert()
        if jumping == 2:
            if direction == "l":
                player_img = pygame.image.load("05.png").convert()
                bullet.image = bullet_img
            else:
                player_img = pygame.image.load("00.png").convert()
                bullet.image = bullet_img
            pos = int(280*(time.time() - start)**2 - 280*(time.time()-start) + 220)
            player.rect.y = pos
            if pos > 220:
                jumping = 0
        if minigun == 1 and direction == 'l' and moving == 1:
            if (lol//15)%2== 0:#лол это чтука для анимации если лол четное до включаем какую то картинка если нет то другую
                player_img = pygame.image.load("moving_Anton.png").convert()
                shooting = 1
            else:
                player_img = pygame.image.load("Anton.png").convert()
                shooting = 1
        elif minigun == 1 and direction == 'r' and moving == 1:
            if (lol//15)%2== 0:
                player_img = pygame.image.load("moving_Petya.png").convert()
                shooting = 1
            else:
                player_img = pygame.image.load("Vasya.png").convert()
                shooting = 1
        elif minigun == 1 and direction == 'l' and moving == 0:
            if (lol // 4) % 2 == 0:
                player_img = pygame.image.load("Anton.png").convert()
                shooting = 1
            else:
                player_img = pygame.image.load("Sasha.png").convert()
                shooting = 1
        elif minigun == 1 and direction == 'r' and moving == 0:
            if (lol // 4) % 2 == 0:
                player_img = pygame.image.load("Petya.png").convert()
                shooting = 1
            else:
                player_img = pygame.image.load("Vasya.png").convert()
                shooting = 1
        distance = math.sqrt((bullet.rect.x-mushroom.rect.x)**2+(bullet.rect.y-mushroom.rect.y-30)**2)
        super_distance = math.sqrt((super_bullet.rect.x - mushroom.rect.x) ** 2 + (super_bullet.rect.y - mushroom.rect.y-30) ** 2)
        dead = math.sqrt((player.rect.x - mushroom.rect.x) ** 2 + (player.rect.y - mushroom.rect.y) ** 2)
        if mushroom_x != 0:
            mushroom.rect.y = 225
        if distance <= 20 or super_distance <= 30:
            mushroom_x = 0
            sound3.play()
            mushroom.rect.y = 500
            mushroomdead = 1
            counter = counter + 1
            start = time.time()
        if mushroomdead == 1 and time.time() - start > 1:
            randside = random.randint(1, 2)
            if randside == 2:
                mushroom_x = 1 + counter / 10
            elif randside == 1:
                mushroom_x = -1 - counter / 10
            mushroomdead = 0
        if dead <= 35:
            background = pygame.image.load("lost.png")
            screen = pygame.display.set_mode((800, 600))
            cond = 2
        mushroom.update(mushroom_img, mushroom_x, 0)
        player.update(player_img, xdir, ydir)
        bullet.update(bullet_img, bullet_x, 0)
        super_bullet.update(super_bullet_img, super_bullet_x, 0)
        bg_x -= 1
        if bg_x == 0:#дест = destination чтобы фон двигался
            bg_x = screen_width
        screen.blit(background,(bg_x - screen_width, 0))#screen.fill((0, 255, 0))
        if bg_x > 0:
            screen.blit(background, (bg_x, 0))
        text_screen = font.render(text + str(counter), True, (0, 0, 0))
        screen.blit(text_screen, (0, 0))
        sprites.draw(screen)
        pygame.display.flip()
        lol = lol +1
    elif cond == 2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break
            elif event.type == pygame.KEYDOWN:  # если нажата клавиша
                if event.key == pygame.K_q:
                    sys.exit()
        screen.blit(background, (0, 0))
        pygame.display.flip()
sys.exit()