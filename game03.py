import pygame

# pygame 시작 함수 실행
pygame.init()
# 실행창 설정
background = pygame.display.set_mode((600, 480))
# 게임 실행창 제목 설정
pygame.display.set_caption("Game 03")

# x_pos = background.get_size()[0] // 2
# y_pos = background.get_size()[1] // 2
x_pos = 300
y_pos = 240

# 무한 반복을 통해 게임 실행
play = True
while play:
  # pygame 이벤트 가져오기
  for event in pygame.event.get():
    # 가져온 이벤트의 타입이 QUIT이면 반복문 종료
    if event.type == pygame.QUIT:
      play = False
    # 만약 키보드를 눌렀다면
    if event.type == pygame.KEYDOWN:
      if event.key == 119:
        y_pos -= 10
      elif event.key == 115:
        y_pos += 10
      elif event.key == 100:
        x_pos += 10
      elif event.key == 97:
        x_pos -= 10
    if event.type == pygame.MOUSEBUTTONUP:
      print('CLICK')

    # 배경을 흰색으로 설정
    background.fill((255, 255, 255))
    # 원 그리기(원을 생성할 실행창, 원 색깔, 좌표, 지름)
    pygame.draw.circle(background, (0, 0, 255), (x_pos, y_pos), 5)
    # 디스플레이 업데이트
    pygame.display.update()

# 게임 종료
pygame.quit()