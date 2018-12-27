import pygame

#게임 엔진 초기화
pygame.init()

#RGB 포맷으로 색을 초기화
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#화면의 크기과 폰트, 제목을 설정
size = [400, 300]
screen = pygame.display.set_mode(size)
font = pygame.font.SysFont("consolas", 20)

pygame.display.set_caption("마우스 모션 이벤트")

#닫기 버튼을 누를 때까지 반복
done = False
flag = None
clock = pygame.time.Clock()

#printText 함수
def printText(msg, color='BLACK', pos=(50,50)):
    textSurface = font.render(msg, True, pygame.Color(color), None)
    textRect = textSurface.get_rect()
    textRect.topleft = pos

    screen.blit(textSurface, textRect)

while not done:

	clock.tick(10)

	#메인 이벤트 루프
	for event in pygame.event.get():
		if event.type == pygame.MOUSEMOTION:
			flag = True
		elif event.type == pygame.QUIT:
			done = True

	screen.fill(WHITE)

	if flag == True:
		printText("Your mouse is now moving!!")
		flag = False

	elif flag == False:
		printText("Your mouse is now stopped!!")
		
        #그린 것을 화면에 업데이트
	#이는 모든 draw 명령의 뒤에 위치해야한다
	pygame.display.flip()

#IDLE로 돌아온다
pygame.quit()
