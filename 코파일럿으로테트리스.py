#cmd
#pip install pygame

import pygame
import random

# 게임 설정
WIDTH, HEIGHT = 300, 600
BLOCK_SIZE = 30
COLUMNS = WIDTH // BLOCK_SIZE
ROWS = HEIGHT // BLOCK_SIZE

# 색상 정의 (더 화려하게 변경)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
COLORS = [
    (0, 255, 255),    # I - 시안
    (0, 0, 255),      # J - 파랑
    (255, 165, 0),    # L - 오렌지
    (255, 255, 0),    # O - 노랑
    (0, 255, 0),      # S - 초록
    (255, 0, 0),      # Z - 빨강
    (128, 0, 128),    # T - 보라
    (255, 0, 255),    # 추가: 핑크
    (0, 255, 128),    # 추가: 민트
    (255, 128, 0),    # 추가: 금색
    (0, 128, 255),    # 추가: 하늘
    (255, 255, 255),  # 추가: 흰색
]

# 테트리스 블록 모양
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 0, 0], [1, 1, 1]],  # J
    [[0, 0, 1], [1, 1, 1]],  # L
    [[1, 1], [1, 1]],        # O
    [[0, 1, 1], [1, 1, 0]],  # S
    [[1, 1, 0], [0, 1, 1]],  # Z
    [[0, 1, 0], [1, 1, 1]]   # T
]

class Tetromino:
    def __init__(self, x, y, shape, color):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = color

    def rotate(self):
        # 블록 모양은 유지하고 색상만 바꿔서 "회전 효과"를 줌
        # 실제 모양은 바뀌지 않음, 색상만 랜덤하게 변경
        self.color = random.choice(COLORS)

def create_grid(locked_positions={}):
    grid = [[BLACK for _ in range(COLUMNS)] for _ in range(ROWS)]
    for y in range(ROWS):
        for x in range(COLUMNS):
            if (x, y) in locked_positions:
                grid[y][x] = locked_positions[(x, y)]
    return grid

def convert_shape_format(shape):
    positions = []
    for i, line in enumerate(shape.shape):
        for j, column in enumerate(line):
            if column:
                positions.append((shape.x + j, shape.y + i))
    return positions

def valid_space(shape, grid):
    accepted_positions = [[(j, i) for j in range(COLUMNS) if grid[i][j] == BLACK] for i in range(ROWS)]
    accepted_positions = [j for sub in accepted_positions for j in sub]
    formatted = convert_shape_format(shape)
    for pos in formatted:
        if pos not in accepted_positions:
            if pos[1] > -1:
                return False
    return True

def check_lost(positions):
    for pos in positions:
        x, y = pos
        if y < 1:
            return True
    return False

def get_shape():
    idx = random.randint(0, len(SHAPES) - 1)
    color_idx = random.randint(0, len(COLORS) - 1)
    shape = SHAPES[idx]
    color = COLORS[color_idx]
    return Tetromino(COLUMNS // 2 - len(shape[0]) // 2, 0, shape, color)

def draw_grid(surface, grid):
    for y in range(ROWS):
        for x in range(COLUMNS):
            pygame.draw.rect(surface, grid[y][x], (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 0)
            # 블럭 테두리 효과 추가
            if grid[y][x] != BLACK:
                pygame.draw.rect(surface, (255,255,255), (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 2)
    for y in range(ROWS):
        pygame.draw.line(surface, GRAY, (0, y * BLOCK_SIZE), (WIDTH, y * BLOCK_SIZE))
    for x in range(COLUMNS):
        pygame.draw.line(surface, GRAY, (x * BLOCK_SIZE, 0), (x * BLOCK_SIZE, HEIGHT))

def clear_rows(grid, locked):
    inc = 0
    for i in range(ROWS-1, -1, -1):
        if BLACK not in grid[i]:
            inc += 1
            ind = i
            for j in range(COLUMNS):
                try:
                    del locked[(j, i)]
                except:
                    continue
    if inc > 0:
        for key in sorted(list(locked), key=lambda x: x[1])[::-1]:
            x, y = key
            if y < ind:
                newKey = (x, y + inc)
                locked[newKey] = locked.pop(key)
    return inc

def main():
    pygame.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('테트리스')
    clock = pygame.time.Clock()
    grid = create_grid()
    change_piece = False
    run = True
    current_piece = get_shape()
    next_piece = get_shape()
    locked_positions = {}
    fall_time = 0
    fall_speed = 0.5
    score = 0

    while run:
        grid = create_grid(locked_positions)
        fall_time += clock.get_rawtime()
        clock.tick()

        if fall_time / 1000 > fall_speed:
            fall_time = 0
            current_piece.y += 1
            if not valid_space(current_piece, grid) and current_piece.y > 0:
                current_piece.y -= 1
                change_piece = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_piece.x -= 1
                    if not valid_space(current_piece, grid):
                        current_piece.x += 1
                elif event.key == pygame.K_RIGHT:
                    current_piece.x += 1
                    if not valid_space(current_piece, grid):
                        current_piece.x -= 1
                elif event.key == pygame.K_DOWN:
                    current_piece.y += 1
                    if not valid_space(current_piece, grid):
                        current_piece.y -= 1
                elif event.key == pygame.K_UP:
                    current_piece.rotate()  # 모양은 유지, 색상만 변경

        shape_pos = convert_shape_format(current_piece)
        for x, y in shape_pos:
            if y > -1:
                grid[y][x] = current_piece.color

        if change_piece:
            for pos in shape_pos:
                locked_positions[(pos[0], pos[1])] = current_piece.color
            current_piece = next_piece
            next_piece = get_shape()
            change_piece = False
            score += clear_rows(grid, locked_positions) * 10

        draw_grid(win, grid)
        pygame.display.update()

        if check_lost(locked_positions):
            run = False

    pygame.quit()
    print(f"게임 오버! 점수: {score}")

if __name__ == "__main__":
    main()