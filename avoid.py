import pygame

# pygame 시작 함수 실행
pygame.init()
# 실행창 설정
background = pygame.display.set_mode((600, 600))
# background = pygame.image.load()
# 게임 실행창 제목 설정
pygame.display.set_caption("Avoid")
# 스프라이트 불러오기
sprite = pygame.image.load('./assets/doodugi.png')
sprite = pygame.transform.scale(sprite, (100, 150)) 

fps = pygame.time.Clock()
x = 300
y = 400

# 무한 반복을 통해 게임 실행
play = True
while play:
  # 1초에 60회만 실행하도록 함
  deltaTime = fps.tick(60)
  # pygame 이벤트 가져오기
  for event in pygame.event.get():
    # 가져온 이벤트의 타입이 QUIT이면 반복문 종료
    if event.type == pygame.QUIT:
      play = False
  # 키보드 입력 체크 
  key = pygame.key.get_pressed()
  if key[pygame.K_LEFT]:
    x -= 5
    if x < 100:
      x = 100
  elif key[pygame.K_RIGHT]:
    x += 5
    if x > 500:
      x = 500

  # 배경을 흰색으로 설정
  background.fill((255, 255, 255))
  # 스프라이트 복사
  background.blit(sprite, (x, y))
  # 디스플레이 업데이트
  pygame.display.update()

# 게임 종료
pygame.quit()