import pygame
from math import pi

#게임 엔진 초기화
pygame.init()

#RGB포맷으로 색 정의
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE  = (  0,   0, 255)
GREEN = (  0, 255,   0)
RED   = (255,   0,   0)

#화면의 크기, 제목을 설정
size = [400, 300]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("타원 일부 그리기")

#닫기 버튼을 누를 때까지 반복
done = False

clock = pygame.time.Clock()

while not done:

    clock.tick(10)

    #메인 이벤트 루프
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(WHITE)

    #pygame.draw.arc(Surface, Color, Rect, Start_angle, Stop_angle, Width=1)
    #Surface : pygame을 실행할 때 전체적으로 화면을 선언한 변수 값
    #Color : 타원의 색깔을 (R, G, B)의 형태로 전달
    #Rect : 타원을 [x축, y축, 오른쪽, 아래]의 형태로 전달
    #Start_angle : 타원을 그릴 시작 위치
    #Stop_angle : 타원을 그릴 끝 위치
    #Width : 타원의 선 크기

    pygame.draw.arc(screen, BLACK, [210, 75, 150, 125], 0, pi/2, 2)
    pygame.draw.arc(screen, GREEN, [210, 75, 150, 125], pi/2, pi, 2)
    pygame.draw.arc(screen, BLUE,  [210, 75, 150, 125], pi, 3*pi/2, 2)
    pygame.draw.arc(screen, RED,   [210, 75, 150, 125], 3*pi/2, 2*pi, 2)
    



    #그린 것을 화면에 업데이트
    #이는 모든 draw 명령의 뒤에 위치해야한다
    pygame.display.flip()

#IDLE로 돌아온다
pygame.quit()
