import pygame
import sys
import random

# 초기화
pygame.init()

# 화면 설정
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("블럭깨기 게임")

# 블럭 설정
block_width, block_height = 80, 20
blocks = []
for row in range(5):
    for col in range(width // block_width):
        block = pygame.Rect(col * block_width, row * block_height, block_width, block_height)
        # 각 블럭마다 무작위로 색상 설정
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        blocks.append((block, color))

# 패들, 공, 텍스트 색상 설정
paddle_color = (255, 255, 255)
ball_color = (0, 0, 255)
text_color = (255, 0, 0)
background_color = (0, 0, 0)

# 패들 설정
paddle_width, paddle_height = 100, 20
paddle_x = (width - paddle_width) // 2
paddle_y = height - 50

# 공 설정
ball_radius = 10
ball_x = width // 2
ball_y = height // 2
ball_speed_x = 5 * random.choice([-1, 1])
ball_speed_y = 5

# 폰트 설정
font = pygame.font.SysFont(None, 55)

# 게임 루프
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    paddle_speed = 10
    paddle_x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * paddle_speed
    paddle_x = max(0, min(width - paddle_width, paddle_x))

    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # 벽과 충돌 검사
    if ball_x - ball_radius < 0 or ball_x + ball_radius > width:
        ball_speed_x *= -1

    if ball_y - ball_radius < 0:
        ball_speed_y *= -1

    # 패들과 충돌 검사
    if (
        paddle_x < ball_x < paddle_x + paddle_width
        and paddle_y < ball_y + ball_radius
    ):
        ball_speed_y *= -1

    # 블럭과 충돌 검사
    for block, color in blocks:
        if block.colliderect(pygame.Rect(ball_x - ball_radius, ball_y - ball_radius, 2 * ball_radius, 2 * ball_radius)):
            ball_speed_y *= -1
            blocks.remove((block, color))

    # 게임 오버 검사
    if ball_y + ball_radius > height:
        screen.fill(background_color)
        text = font.render("게임 오버", True, text_color)
        screen.blit(text, (width // 2 - 150, height // 2 - 30))
        pygame.display.flip()
        pygame.time.wait(3000)
        pygame.quit()
        sys.exit()

    # 승리 검사
    if not blocks:
        screen.fill(background_color)
        text = font.render("승리!", True, text_color)
        screen.blit(text, (width // 2 - 100, height // 2 - 30))
        pygame.display.flip()
        pygame.time.wait(3000)
        pygame.quit()
        sys.exit()

    # 화면 그리기
    screen.fill(background_color)
    pygame.draw.rect(screen, paddle_color, (paddle_x, paddle_y, paddle_width, paddle_height))
    pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)

    for block, color in blocks:
        pygame.draw.rect(screen, color, block)

    pygame.display.flip()

    # 초당 프레임 수 설정
    pygame.time.Clock().tick(60)
