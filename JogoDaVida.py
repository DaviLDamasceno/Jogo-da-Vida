import pygame
import random as rnd
import time

# Dimensões da grade
WIDTH = 800
HEIGHT = 800
CELL_SIZE = 40
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE

# Cores
BLUE = (50, 200, 240)
WHITE = (255, 255, 255)


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

def draw_grid(grid):
    screen.fill(BLUE)
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            if grid[y][x] == 1:
                pygame.draw.rect(screen, WHITE, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # linhas verticais
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(screen, BLUE, (x, 0), (x, HEIGHT))

    #linhas horizontais
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, BLUE, (0, y), (WIDTH, y))

def game_of_life(grid):
    new_grid = [[0] * GRID_WIDTH for _ in range(GRID_HEIGHT)]
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            c = count_neighbors(grid, x, y)
            if grid[y][x] == 0:
                if c == 3:
                    new_grid[y][x] = 1
            else:
                if c < 2 or c > 3:
                    new_grid[y][x] = 0
                else:
                    new_grid[y][x] = 1
    return new_grid

def count_neighbors(grid, x, y):
    count = 0
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            if dy == 0 and dx == 0:
                continue
            nx = x + dx
            ny = y + dy
            if 0 <= nx < GRID_WIDTH and 0 <= ny < GRID_HEIGHT and grid[ny][nx] == 1:
                count += 1
    return count


grid = [[rnd.randint(0, 1) for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_grid(grid)
    pygame.display.flip()

    grid = game_of_life(grid)

    time.sleep(0.9)  # Intervalo da animaçoes
    clock.tick(60)

pygame.quit()

