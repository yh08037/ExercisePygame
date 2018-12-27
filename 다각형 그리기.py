import pygame

#게임 엔진 초기화
pygame.init()

#RGB포맷으로 색 정의
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE  = (  0,   0, 255)
GREEN = (  0, 255,   0)
RED   = (255,   0,   0)

#화면의 크기과 폰트, 제목을 설정
size = [500, 300]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Draw Poligon")

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

    #pygame.draw.rect(Surface, color, PointLilst, Width=0)
    #Surface : pygame을 실행할 때 전체적으로 화면을 선언한 변수 값
    #color : 다각형의 색깔을 (R, G, B)의 형태로 전달
    #PointList : 다각형을 점을 [[x1, y1], [x2, y2],..., [xn, yn]]의 형태로 전달
    #Width : 다각형의 선 크기이며, 기본값은 0:색 채움

    pygame.draw.polygon(screen, BLACK, [[50, 50], [0, 100], [100, 100]], 2)

    pygame.draw.polygon(screen, BLACK, [[200, 50], [150, 100], [250, 100]])

    pygame.draw.polygon(screen, GREEN, [[0, 200], [200, 200], [100, 250], [100, 150]], 4)
    
    pygame.draw.polygon(screen, GREEN, [[250, 200], [450, 200], [350, 250], [350, 150]])

    #그린 것을 화면에 업데이트
    #이는 모든 draw 명령의 뒤에 위치해야한다
    pygame.display.flip()

#IDLE로 돌아온다
pygame.quit()
