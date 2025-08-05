import pygame
import sys

# 초기화
pygame.init()
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("블럭깨기 게임")

# 색상
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 102, 204)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# 패들
paddle = pygame.Rect(WIDTH // 2 - 150, HEIGHT - 30, 300, 10)  # 폭을 3배로 변경
paddle_speed = 7

# 공
ball = pygame.Rect(WIDTH // 2 - 10, HEIGHT // 2 - 10, 20, 20)
ball_speed = [5, -5]

# 블럭
blocks = []
block_colors = [
    (255, 0, 0),      # 빨강
    (255, 165, 0),    # 주황
    (255, 255, 0),    # 노랑
    (0, 255, 0),      # 초록
    (0, 255, 255),    # 청록
    (0, 0, 255),      # 파랑
    (128, 0, 128),    # 보라
    (255, 192, 203),  # 핑크
]
block_rows, block_cols = 5, 8
block_width, block_height = 60, 20
for row in range(block_rows):
    for col in range(block_cols):
        block = pygame.Rect(10 + col * (block_width + 10), 40 + row * (block_height + 10), block_width, block_height)
        color = block_colors[col % len(block_colors)]
        blocks.append((block, color))

clock = pygame.time.Clock()
running = True

while running:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 패들 이동
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.x += paddle_speed

    # 공 이동
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    # 벽 충돌
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_speed[0] = -ball_speed[0]
    if ball.top <= 0:
        ball_speed[1] = -ball_speed[1]
    if ball.bottom >= HEIGHT:
        print("게임 오버!")
        running = False

    # 패들 충돌
    if ball.colliderect(paddle):
        ball_speed[1] = -ball_speed[1]

    # 블럭 충돌
    hit_index = -1
    for i, (block, color) in enumerate(blocks):
        if ball.colliderect(block):
            hit_index = i
            break
    if hit_index != -1:
        blocks.pop(hit_index)
        ball_speed[1] = -ball_speed[1]

    # 그리기
    pygame.draw.rect(screen, BLUE, paddle)
    pygame.draw.ellipse(screen, RED, ball)
    for block, color in blocks:
        pygame.draw.rect(screen, color, block)

    # 승리 조건
    if not blocks:
        print("클리어!")
        running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()