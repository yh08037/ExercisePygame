import pygame

#게임 엔진 초기화
pygame.init()

#RGB 포맷으로 색 정의
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

size = [400, 300]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("타원 그리기")


done = False
clock = pygame.time.Clock()

while not done:

    clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(WHITE)

    pygame.draw.ellipse(screen, RED, [50, 50, 50, 20], 2)
    pygame.draw.ellipse(screen, RED, [150, 50, 20, 50])

    pygame.display.flip()


pygame.quit()
