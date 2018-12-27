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
size = [400, 300]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Draw Rectangle")

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

    #pygame.draw.rect(Surface, color, Rect, Width=0)
    #Surface : pygame을 실행할 때 전체적으로 화면을 선언한 변수 값
    #color : 사각형의 색깔을 (R, G, B)의 형태로 전달
    #Rect : 사각형을 [x축, y축, 오른쪽, 아래]의 형태로 전달
    #Width : 사각형의 선 크기이며, 기본값은 0:색 채움

    pygame.draw.rect(screen, BLACK, [75, 10, 50, 20], 2)

    pygame.draw.rect(screen, BLACK, [150, 10, 50, 20])

    #그린 것을 화면에 업데이트
    #이는 모든 draw 명령의 뒤에 위치해야한다
    pygame.display.flip()

#IDLE로 돌아온다
pygame.quit()
