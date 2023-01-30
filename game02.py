import pygame

# pygame 시작 함수 실행
pygame.init()
# 배경 설정
background = pygame.display.set_mode((600, 480))
# 게임 실행창 제목 설정
pygame.display.set_caption("Game 02")

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
        print('UP')
      elif event.key == 115:
        print('DOWN')
      elif event.key == 100:
        print('RIGHT')
      elif event.key == 97:
        print('LEFT')
    if event.type == pygame.MOUSEBUTTONUP:
      print('CLICK')

# 게임 종료
pygame.quit()