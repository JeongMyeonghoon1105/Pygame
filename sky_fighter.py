from pygame import *
import random

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.player_img = image.load("./assets/pixel_ship_yellow.png")
        
    def update(self, win):
        keys = key.get_pressed()
        if keys[K_LEFT]:
            self.x -= 5   
        if keys[K_RIGHT]:
            self.x += 5   
        if keys[K_UP]:
            self.y -= 5   
        if keys[K_DOWN]:
            self.y += 5   
        win.blit(self.player_img, (self.x, self.y))

class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.enemy_img = image.load("./assets/pixel_ship_red_small.png")
        
    def update(self, win):
        win.blit(self.enemy_img, (self.x, self.y))
        
    def move(self):
        self.y += 5
        if random.randint(0, 5) == 3:
            self.x += random.randint(-10, 10)

class Laser:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.laser_img = img

    def update(self, win):
        win.blit(self.laser_img, (self.x, self.y))
        win.blit(self.laser_img, (self.x+80, self.y))

    def move(self):
        self.y -= 5
       
WIDTH, HEIGHT = 500, 500

init()

window = display.set_mode((WIDTH, HEIGHT))
display.set_caption("Sky Fighter")

shooting_sound = mixer.Sound("pew.wav")
explode_sound = mixer.Sound("explode.wav")

laser_img = image.load("./assets/pixel_laser_green_2.png") 

BG = image.load("./assets/background-black.png")
BG_scaled = transform.scale(BG, (500, 500))

player = Player(100, 100)
plaser = Laser(300, 300, laser_img)

clock = time.Clock()

# 적군 리스트 
enemies = []
# 레이저 리스트 
lasers = [] 

run = True
enemyCool = 0
laserCool = 0
while run:
    dt = clock.tick(60)
    for ev in event.get():
        if ev.type == QUIT:
            run = False
   
    window.blit(BG_scaled, (0,0))
    player.update(window) 
    #plaser.update(window)
    # 적군 복제
    enemyCool += 1
    if enemyCool > 20:
        enemy = Enemy(random.randint(0, 500), 0) 
        enemies.append(enemy)  # [ enemy, enemy....]
        enemyCool = 0
    # 레이저 복제
    laserCool += 1
    if laserCool > 10: 
        keys = key.get_pressed()
        if keys[K_SPACE]:
            # 복제 
            plaser = Laser(player.x, player.y, laser_img)
            lasers.append(plaser)
            shooting_sound.play()
            laserCool = 0
    # 적군 업데이트 
    for ey in enemies:
        ey.update(window)
    for ey in enemies:
        ey.move()
        if ey.y > 500:
            enemies.remove(ey)
    # 레이저 업데이트
    for laser in lasers:
        laser.update(window)
        print(len(lasers))
    for laser in lasers:
        laser.move()
        if laser.y < 0:
            lasers.remove(laser)
    #for laser in lasers:
    #    if laser.y < 0:
    #        lasers.remove(laser)
    # 충돌체크 - Enemy vs Player

    for enemy in enemies:
        enemy_rect = enemy.enemy_img.get_rect(topleft = (enemy.x, enemy.y))
        player_rect = player.player_img.get_rect(topleft = (player.x, player.y))
        result = player_rect.colliderect(enemy_rect)
        if result == True:
            enemies.remove(enemy)
            
    # 충돌체크 레이저 VS 에네미 
    for laser in lasers:
        laser_rect_1 = laser.laser_img.get_rect(topleft = (laser.x, laser.y))
        laser_rect_2 = laser.laser_img.get_rect(topleft = (laser.x+80, laser.y))
        for enemy in enemies:
            enemy_rect = enemy.enemy_img.get_rect(topleft = (enemy.x, enemy.y))
            result1 = laser_rect_1.colliderect(enemy_rect)
            result2 = laser_rect_2.colliderect(enemy_rect)
            if result1 == True or result2 == True: 
                enemies.remove(enemy)
                lasers.remove(laser)
                explode_sound.play()
    
    #plaser.move()
    display.update()   
quit()
