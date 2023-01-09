import pygame

# pygame 시작 함수 실행
pygame.init()
# 실행창 설정
background = pygame.display.set_mode((600, 480))
# 게임 실행창 제목 설정
pygame.display.set_caption("Game 04")

# x_pos = background.get_size()[0] // 2
# y_pos = background.get_size()[1] // 2
x_pos = 300
y_pos = 240

to_x = 0
to_y = 0

fps = pygame.time.Clock()

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
    # 만약 키보드를 눌렀다면
    if event.type == pygame.KEYDOWN:
      if event.key == 119:
        to_y = -1
      elif event.key == 115:
        to_y = 1
      elif event.key == 100:
        to_x = 1
      elif event.key == 97:
        to_x = -1
    if event.type == pygame.KEYUP:
      if event.key == 119:
        to_y = 0
      elif event.key == 115:
        to_y = 0
      elif event.key == 100:
        to_x = 0
      elif event.key == 97:
        to_x = 0
    if event.type == pygame.MOUSEBUTTONUP:
      print('CLICK')
    
    x_pos += to_x
    y_pos += to_y

    # 배경을 흰색으로 설정
    background.fill((255, 255, 255))
    # 원 그리기(원을 생성할 실행창, 원 색깔, 좌표, 지름)
    pygame.draw.circle(background, (0, 0, 255), (x_pos, y_pos), 5)
    # 디스플레이 업데이트
    pygame.display.update()

# 게임 종료
pygame.quit()