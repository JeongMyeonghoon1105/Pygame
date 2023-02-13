import pygame
import random
import time

# pygame 시작 함수 실행
pygame.init()
start = time.time()
# 실행창 설정
background = pygame.display.set_mode((600, 600))
# background = pygame.image.load()
# 게임 실행창 제목 설정
pygame.display.set_caption("Avoid")
# 스프라이트 불러오기
sprite = pygame.image.load('./assets/doodugi.png')
sprite = pygame.transform.scale(sprite, (100, 150))
# 장애물 불러오기
e1 = pygame.image.load('./assets/ddong.png')
e1 = pygame.transform.scale(e1, (100, 100)) 
e2 = pygame.image.load('./assets/ddong.png')
e2 = pygame.transform.scale(e2, (100, 100)) 
e3 = pygame.image.load('./assets/ddong.png')
e3 = pygame.transform.scale(e3, (100, 100)) 
e4 = pygame.image.load('./assets/ddong.png')
e4 = pygame.transform.scale(e4, (100, 100)) 
# 장애물 위치 설정
e1_y = random.randint(-400, 0)
e1_x = random.randint(0, 600)
e2_y = random.randint(-400, 0)
e2_x = random.randint(0, 600)
e3_y = random.randint(-400, 0)
e3_x = random.randint(0, 600)
e4_y = random.randint(-400, 0) 
e4_x = random.randint(0, 600)

fps = pygame.time.Clock()
x = 300
y = 400
score = 5
collide = False
finish = False

# 무한 반복을 통해 게임 실행
play = True
while play:
  end = time.time()
  # 1초에 60회만 실행하도록 함
  deltaTime = fps.tick(60)
  # pygame 이벤트 가져오기
  for event in pygame.event.get():
    # 가져온 이벤트의 타입이 QUIT이면 반복문 종료
    if event.type == pygame.QUIT:
      play = False
  if score <= 0:
    screen = pygame.image.load('./assets/gameover.png')
    screen = pygame.transform.scale(screen, (800, 600))
    background.blit(screen, (-100, 0))
    if not finish:
      print('경과 시간 : ' + str(int(end - start)) + '초')
      finish = True
    time.sleep(2)
    play = False
  elif end - start > 20:
    screen = pygame.image.load('./assets/complete.jpg')
    screen = pygame.transform.scale(screen, (800, 600))
    background.blit(screen, (-100, 0))
    if not finish:
      print('경과 시간 : ' + str(int(end - start)) + '초')
      finish = True
    time.sleep(2)
    play = False
  else:
    # 키보드 입력 체크 
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
      x -= 5
      if x < 50:
        x = 50
    elif key[pygame.K_RIGHT]:
      x += 5
      if x > 550:
        x = 550
    
    e1_y += 5
    e2_y += 5
    e3_y += 5
    e4_y += 5
    if e1_y > 600:
      e1_x = random.randint(0, 600)
      e1_y = random.randint(-400, 0)
    if e2_y > 600:
      e2_x = random.randint(0, 600)
      e2_y = random.randint(-400, 0)
    if e3_y > 600:
      e3_x = random.randint(0, 600)
      e3_y = random.randint(-400, 0)
    if e4_y > 600:
      e4_x = random.randint(0, 600)
      e4_y = random.randint(-400, 0)
    
    rect1 = sprite.get_rect(center=(x,y))
    rect2 = e1.get_rect(center=(e1_x,e1_y))
    rect3 = e1.get_rect(center=(e2_x,e2_y))
    rect4 = e1.get_rect(center=(e3_x,e3_y))
    rect5 = e1.get_rect(center=(e4_x,e4_y))

    if rect1.colliderect(rect2):
      if not collide:
        score -= 1
        print('점수 : ' + str(score))
      collide = True
    elif rect1.colliderect(rect3):
      if not collide:
        score -= 1
        print('점수 : ' + str(score))
      collide = True
    elif rect1.colliderect(rect4):
      if not collide:
        score -= 1
        print('점수 : ' + str(score))
      collide = True
    elif rect1.colliderect(rect5):
      if not collide:
        score -= 1
        print('점수 : ' + str(score))
      collide = True
    else:
      collide = False

    # 배경을 흰색으로 설정
    background.fill((255, 255, 255))
    # 스프라이트 복사
    background.blit(sprite, (x, y))
    background.blit(e1, (e1_x, e1_y)) 
    background.blit(e2, (e2_x, e2_y))
    background.blit(e3, (e3_x, e3_y))
    background.blit(e4, (e4_x, e4_y))
  # 디스플레이 업데이트
  pygame.display.update()
# 게임 종료
pygame.quit()