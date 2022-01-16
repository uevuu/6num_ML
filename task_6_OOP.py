import pygame
from copy import deepcopy
from random import randint


class GameLife:

    def __init__(self, width, height, size, fps=1):
        self.width = width
        self.height = height
        self.size = size
        self.count_cell_width = width // size
        self.count_cell_height = height // size
        self.fps = fps
        self.current_field = [[randint(0, 1) for i in range(self.count_cell_width)] for j in
                              range(self.count_cell_height)]
        self.next_field = [[0 for i in range(self.count_cell_width)] for j in range(self.count_cell_height)]

    # Рисуем игровое поле
    def draw_grid(self):
        pygame.init()
        screen = pygame.display.set_mode((self.width, self.height))
        [pygame.draw.line(screen, pygame.Color('white'), (x, 0), (x, self.height)) for x in
         range(0, self.width, self.size)]
        [pygame.draw.line(screen, pygame.Color('white'), (0, y), (self.width, y)) for y in
         range(0, self.height, self.size)]

    # запуск игры
    def view(self):
        pygame.init()
        screen = pygame.display.set_mode((self.width, self.height))
        clock = pygame.time.Clock()
        screen.fill(pygame.Color('black'))
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            self.draw_grid()
            # Живые клетки
            for x in range(1, self.count_cell_width - 1):
                for y in range(1, self.count_cell_height - 1):
                    if self.current_field[y][x]:
                        pygame.draw.rect(screen, pygame.Color('red'),
                                         (x * self.size - 1, y * self.size - 1, self.size - 1, self.size - 1))
                    self.next_field[y][x] = Ceil.check_ceil(self.current_field, x, y)
            self.current_field = deepcopy(self.next_field)
            pygame.display.flip()
            clock.tick(self.fps)


class Ceil:
    @staticmethod
    # Проверяем клетку на соседей
    def check_ceil(current_field, x, y):
        count = 0
        for i in range(y - 1, y + 2):
            for j in range(x - 1, x + 2):
                if current_field[i][j]:
                    count += 1

        if current_field[y][x]:
            count -= 1
            if count == 2 or count == 3:
                return 1
            return 0
        else:
            if count == 3:
                return 1
            return 0


game = GameLife(800, 800, 20, 5)
game.view()
