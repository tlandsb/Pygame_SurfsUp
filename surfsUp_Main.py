import pygame

pygame.init()

win = pygame.display.set_mode((800, 900))

pygame.display.set_caption("Surfs Up!")

walkRight = [pygame.image.load('surfer.png'), pygame.image.load('surfer.png'), pygame.image.load('surfer.png'),
             pygame.image.load('surfer.png'), pygame.image.load('surfer.png'), pygame.image.load('surfer.png'),
             pygame.image.load('surfer.png'), pygame.image.load('surfer.png'), pygame.image.load('surfer.png')]
walkLeft = [pygame.image.load('surfer.png'), pygame.image.load('surfer.png'), pygame.image.load('surfer.png'),
            pygame.image.load('surfer.png'), pygame.image.load('surfer.png'), pygame.image.load('surfer.png'),
            pygame.image.load('surfer.png'), pygame.image.load('surfer.png'), pygame.image.load('surfer.png')]
bg = pygame.image.load('ocean3.png')
char = pygame.image.load('surfer.png')

clock = pygame.time.Clock()

##bulletSound = pygame.mixer.Sound('bullet.wav')
##hitSound = pygame.mixer.Sound('hit.wav')

# music = pygame.mixer.music.load('mightyreal.mp3')
# pygame.mixer.music.play(-1)

score = 0


class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.health = 10
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.standing = True
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not (self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))
        ##self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
        pygame.draw.rect(win, (0, 128, 0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
        self.hitbox = (self.x, self.y, 100, 120)
        pygame.draw.rect(win, (255,0,0), self.hitbox,2)

    def hit(self):
        self.isJump = False
        self.jumpCount = 10
        # self.x = 100
        # self.y = 410
        self.walkCount = 0
        font1 = pygame.font.SysFont('comicsans', 50)
        text = font1.render('BOMB WAVE!!', 1, (0,100,0))
        win.blit(text, (250 - (text.get_width() / 2), 200))
        pygame.display.update()
        i = 0
        while i < 200:
            ##pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 201
                    pygame.quit()

    def hit_bad(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False
        print('hit')

class projectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


class wave(object):
    walkRight = [pygame.image.load('wave.jpg'), pygame.image.load('wave.jpg'), pygame.image.load('wave.jpg'),
                 pygame.image.load('wave.jpg'), pygame.image.load('wave.jpg'), pygame.image.load('wave.jpg'),
                 pygame.image.load('wave.jpg'), pygame.image.load('wave.jpg'), pygame.image.load('wave.jpg'),
                 pygame.image.load('wave.jpg'), pygame.image.load('wave.jpg')]
    walkLeft = [pygame.image.load('wave.jpg'), pygame.image.load('wave.jpg'), pygame.image.load('wave.jpg'),
                pygame.image.load('wave.jpg'), pygame.image.load('wave.jpg'), pygame.image.load('wave.jpg'),
                pygame.image.load('wave.jpg'), pygame.image.load('wave.jpg'), pygame.image.load('wave.jpg'),
                pygame.image.load('wave.jpg'), pygame.image.load('wave.jpg')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.health = 10
        self.visible = True

    def draw(self, win):
        ##self.move()
        if self.visible:
            if self.walkCount + 1 >= 33:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1

            ##pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            ##pygame.draw.rect(win, (0, 128, 0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
            #self.hitbox = (self.x + 17, self.y + 2, 31, 57)
            self.hitbox = (self.x, self.y, 164, 64)
            ##pygame.draw.rect(win, (255,0,0), self.hitbox,2)
            # goblin = enemy(141, 520, 64, 64, 450)

    def move(self, vel):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

    # def hit(self):
    #     if self.health > 0:
    #         self.health -= 1
    #     else:
    #         self.visible = False
    #     print('hit')

    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False
        print('hit')

class enemy_water(object):

    def __init__(self, image, x, y, width, height, end):
        self.image=image
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.y, self.end]
        self.walkCount = 0
        self.vel = 6
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.health = 10
        self.visible = True

    def draw(self, win):
        self.move()
        if self.visible:
            win.blit(self.image, (self.x, self.y))

            ##pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            ##pygame.draw.rect(win, (0, 128, 0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
            #self.hitbox = (self.x + 17, self.y + 2, 31, 57)
            self.hitbox = (self.x, self.y, 22, 22)
            ##pygame.draw.rect(win, (255,0,0), self.hitbox,2)
            # goblin = enemy(141, 520, 64, 64, 450)

    ##clam = enemy_water(10, 10, 5, 5, 1000)
    def move(self):
        if self.y > 0:
            if self.y + self.vel < self.path[1]:
                self.y -= self.vel
        else:
            self.y=820

        print("x ",self.x, "Y ",self.y)
        print("vel", self.vel)


    # def hit(self):
    #     if self.health > 0:
    #         self.health -= 1
    #     else:
    #         self.visible = False
    #     print('hit')

    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False
        print('hit')

def redrawGameWindow():
    win.blit(bg, (0, 0))
    text = font.render('Score: ' + str(score), 1, (0, 0, 0))
    win.blit(text, (350, 10))
    man.draw(win)
    wave1.draw(win)
    waterEnemy1.draw(win)
    waterEnemy2.draw(win)
    waterEnemy3.draw(win)
    waterEnemy4.draw(win)
    waterEnemy5.draw(win)
    waterEnemy6.draw(win)
    for bullet in bullets:
        bullet.draw(win)

    pygame.display.update()


# mainloop -- LEVEL 1
font = pygame.font.SysFont('comicsans', 30, True)
man = player(200, 410, 64, 64)
wave1 = wave(141, 520, 64, 64, 450)
waterEnemy1= enemy_water(pygame.image.load('clam.png'), 37, 820, 5, 5, 1000)
waterEnemy2= enemy_water(pygame.image.load('clam.png'),87, 820, 5, 5, 1000)
waterEnemy3= enemy_water(pygame.image.load('clam.png'),500, 820, 5, 5, 1000)
waterEnemy4= enemy_water(pygame.image.load('clam.png'),600, 820, 5, 5, 1000)
waterEnemy5= enemy_water(pygame.image.load('clam.png'),200, 820, 5, 5, 1000)
waterEnemy6= enemy_water(pygame.image.load('clam.png'),500, 820, 5, 5, 1000)

shootLoop = 0
bullets = []
run = True
while run:
    clock.tick(27)

    if man.health<2:
        print("GAME OVER")
        break

    # if score > 1000:
    #     win = pygame.display.set_mode((950, 900))
    #     pygame.display.set_caption("Surfs Up!")
    #     bg=pygame.image.load('van.jpg')
    #     win.blit(bg, (0, 0))
    #     text = font.render('NEXT LEVEL, LETS GO!', 1, (46,139,87))
    #     win.blit(text, (80, 100))
    #     pygame.display.update()
    #     pygame.time.delay(4000)
    #     print("Level 2")
        # break

    if wave1.visible == True:
        if man.hitbox[1] < wave1.hitbox[1] + wave1.hitbox[3] and man.hitbox[1] + man.hitbox[3] > wave1.hitbox[1]:
            if man.hitbox[0] + man.hitbox[2] > wave1.hitbox[0] and man.hitbox[0] < wave1.hitbox[0] + wave1.hitbox[2]:
                man.hit()
                score += 5

    if man.hitbox[1] < waterEnemy1.hitbox[1] + waterEnemy1.hitbox[3] and man.hitbox[1] + man.hitbox[3] > waterEnemy1.hitbox[1]:
        if man.hitbox[0] + man.hitbox[2] > waterEnemy1.hitbox[0] and man.hitbox[0] < waterEnemy1.hitbox[0] + waterEnemy1.hitbox[2]:
            man.hit_bad()

    if man.hitbox[1] < waterEnemy2.hitbox[1] + waterEnemy2.hitbox[3] and man.hitbox[1] + man.hitbox[3] > waterEnemy2.hitbox[1]:
        if man.hitbox[0] + man.hitbox[2] > waterEnemy2.hitbox[0] and man.hitbox[0] < waterEnemy2.hitbox[0] + waterEnemy2.hitbox[2]:
            man.hit_bad()

    if man.hitbox[1] < waterEnemy3.hitbox[1] + waterEnemy3.hitbox[3] and man.hitbox[1] + man.hitbox[3] > waterEnemy3.hitbox[1]:
        if man.hitbox[0] + man.hitbox[2] > waterEnemy3.hitbox[0] and man.hitbox[0] < waterEnemy3.hitbox[0] + waterEnemy3.hitbox[2]:
            man.hit_bad()

    if man.hitbox[1] < waterEnemy4.hitbox[1] + waterEnemy4.hitbox[3] and man.hitbox[1] + man.hitbox[3] > waterEnemy4.hitbox[1]:
        if man.hitbox[0] + man.hitbox[2] > waterEnemy4.hitbox[0] and man.hitbox[0] < waterEnemy4.hitbox[0] + waterEnemy4.hitbox[2]:
            man.hit_bad()

    if man.hitbox[1] < waterEnemy5.hitbox[1] + waterEnemy5.hitbox[3] and man.hitbox[1] + man.hitbox[3] > waterEnemy5.hitbox[1]:
        if man.hitbox[0] + man.hitbox[2] > waterEnemy5.hitbox[0] and man.hitbox[0] < waterEnemy5.hitbox[0] + waterEnemy5.hitbox[2]:
            man.hit_bad()

    if man.hitbox[1] < waterEnemy6.hitbox[1] + waterEnemy6.hitbox[3] and man.hitbox[1] + man.hitbox[3] > waterEnemy6.hitbox[1]:
        if man.hitbox[0] + man.hitbox[2] > waterEnemy6.hitbox[0] and man.hitbox[0] < waterEnemy6.hitbox[0] + waterEnemy6.hitbox[2]:
            man.hit_bad()



    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 3:
        shootLoop = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[
            1]:
            if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + \
                    goblin.hitbox[2]:
                ##hitSound.play()
                goblin.hit()
                score += 1
                bullets.pop(bullets.index(bullet))

        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and shootLoop == 0:
        ##bulletSound.play()
        if man.left:
            facing = -1
        else:
            facing = 1

        if len(bullets) < 5:
            bullets.append(
                projectile(round(man.x + man.width // 2), round(man.y + man.height // 2), 6, (0, 0, 0), facing))

        shootLoop = 1

    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False
    elif keys[pygame.K_RIGHT] and man.x < 2000 - man.width - man.vel:
        man.x += man.vel
        man.right = True
        man.left = False
        man.standing = False
    else:
        man.standing = True
        man.walkCount = 0

    if not (man.isJump):
        if keys[pygame.K_UP]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.5 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10

    print(event)
    redrawGameWindow()

# # mainloop - LEVEL 2
# bg = pygame.image.load('ocean3.png')
# score=0
# font = pygame.font.SysFont('comicsans', 30, True)
# man = player(200, 410, 64, 64)
# goblin = wave(141, 520, 64, 64, 450)
#
# waterEnemy1= enemy_water(pygame.image.load('jellyfish-n.png'), 37, 820, 5, 5, 1000)
# waterEnemy2= enemy_water(pygame.image.load('jellyfish-n.png'),87, 820, 5, 5, 1000)
# waterEnemy3= enemy_water(pygame.image.load('jellyfish-n.png'),500, 820, 5, 5, 1000)
# waterEnemy4= enemy_water(pygame.image.load('jellyfish-n.png'),600, 820, 5, 5, 1000)
# waterEnemy5= enemy_water(pygame.image.load('jellyfish-n.png'),200, 820, 5, 5, 1000)
# waterEnemy6= enemy_water(pygame.image.load('jellyfish-n.png'),500, 820, 5, 5, 1000)
#
#
# shootLoop = 0
# bullets = []
# run = True
# while run:
#     clock.tick(27)
#
#     if man.health<2:
#         print("GAME OVER")
#         break
#
#     if score > 1000:
#         print("GAME OVER")
#         break
#
#     if goblin.visible == True:
#         if man.hitbox[1] < goblin.hitbox[1] + goblin.hitbox[3] and man.hitbox[1] + man.hitbox[3] > goblin.hitbox[1]:
#             if man.hitbox[0] + man.hitbox[2] > goblin.hitbox[0] and man.hitbox[0] < goblin.hitbox[0] + goblin.hitbox[2]:
#                 man.hit()
#                 score += 5
#
#     if man.hitbox[1] < waterEnemy1.hitbox[1] + waterEnemy1.hitbox[3] and man.hitbox[1] + man.hitbox[3] > waterEnemy1.hitbox[1]:
#         if man.hitbox[0] + man.hitbox[2] > waterEnemy1.hitbox[0] and man.hitbox[0] < waterEnemy1.hitbox[0] + waterEnemy1.hitbox[2]:
#             man.hit_bad()
#
#     if shootLoop > 0:
#         shootLoop += 1
#     if shootLoop > 3:
#         shootLoop = 0
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
#
#     for bullet in bullets:
#         if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[
#             1]:
#             if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + \
#                     goblin.hitbox[2]:
#                 ##hitSound.play()
#                 goblin.hit()
#                 score += 1
#                 bullets.pop(bullets.index(bullet))
#
#         if bullet.x < 500 and bullet.x > 0:
#             bullet.x += bullet.vel
#         else:
#             bullets.pop(bullets.index(bullet))
#
#     keys = pygame.key.get_pressed()
#
#     if keys[pygame.K_SPACE] and shootLoop == 0:
#         ##bulletSound.play()
#         if man.left:
#             facing = -1
#         else:
#             facing = 1
#
#         if len(bullets) < 5:
#             bullets.append(
#                 projectile(round(man.x + man.width // 2), round(man.y + man.height // 2), 6, (0, 0, 0), facing))
#
#         shootLoop = 1
#
#     if keys[pygame.K_LEFT] and man.x > man.vel:
#         man.x -= man.vel
#         man.left = True
#         man.right = False
#         man.standing = False
#     elif keys[pygame.K_RIGHT] and man.x < 1000 - man.width - man.vel:
#         man.x += man.vel
#         man.right = True
#         man.left = False
#         man.standing = False
#     else:
#         man.standing = True
#         man.walkCount = 0
#
#     if not (man.isJump):
#         if keys[pygame.K_UP]:
#             man.isJump = True
#             man.right = False
#             man.left = False
#             man.walkCount = 0
#     else:
#         if man.jumpCount >= -10:
#             neg = 1
#             if man.jumpCount < 0:
#                 neg = -1
#             man.y -= (man.jumpCount ** 2) * 0.5 * neg
#             man.jumpCount -= 1
#         else:
#             man.isJump = False
#             man.jumpCount = 10
#
#     print(event)
#     redrawGameWindow()

pygame.quit()
