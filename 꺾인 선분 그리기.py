import pygame

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

pygame.display.set_caption("선분 그리기")


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

    #pygame.draw.lines(Surface, Color, Closed, PointList, Width=1)
    #Surface : pygame을 실행할 때 전체적으로 화면을 선언한 변수 값
    #Color : 선분의 색깔을 (R, G, B)의 형태로 전달
    #Closed : 시작점과 끝점을 연결할지 안할지를 결정
    #PointList : 꺾인 선의 꼭짓점의 위치들의 리스
    #Width : 선분의 선 크기

    pygame.draw.lines(screen, GREEN, False, [[50, 50], [100, 100], [50, 200]], 5)
    pygame.draw.lines(screen, BLUE, True, [[150, 50], [200, 100], [150, 200]], 5)


    #그린 것을 화면에 업데이트
    #이는 모든 draw 명령의 뒤에 위치해야한다
    pygame.display.update()

#IDLE로 돌아온다
pygame.quit()
