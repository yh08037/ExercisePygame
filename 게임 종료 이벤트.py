import pygame

#게임 엔진 최기화
pygame.init()

#RGB 포맷으로 색 정의
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE  = (  0,   0, 255)
GREEN = (  0, 255,   0)
RED   = (255,   0,   0)

#화면의 크기를 설정
size = [400, 300]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("게임 종료 이벤트")


done = False
flag = False
FPS = 10
clock = pygame.time.Clock()

x = 0
y = 0
count = 0

while not done:

    clock.tick(FPS)

    #메인 이벤트 루프
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            if count >=15:
                done = True
            flag = True


    screen.fill(WHITE)

    if flag == True:
        x += 10
        y += 10
        count += 1
        flag = False

    #그린 것을 화면에 업데이트
    #이는 모든 draw 명령의 뒤에 위치해야한다
    pygame.draw.line(screen, BLACK, [0, 0], [x, y], 5)

    pygame.display.update()

#IDLE로 돌아온다
pygame.quit()

    
