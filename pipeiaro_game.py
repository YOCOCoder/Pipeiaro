import sys
import pygame
import time

pygame.init()


class Field:

    def __init__(self, size=12):
        self.size = size
        cells = {}
        self.cell_width = 48
        self.cell_height = 48

        i = 1
        for row in range(0, size, 1):
            for col in range(0, size, 1):
                cells[str(i)] = (col * self.cell_width, row * self.cell_height)
                i += 1
        self.cells = cells

    def open_cell(self, click_coord):
        x_coord = click_coord[0]
        y_coord = click_coord[1]
        click_cell = ((x_coord // self.cell_width) + 1) + ((y_coord // self.cell_height) * self.size)
        click_cell_coord = field.cells[str(click_cell)]
        screen.blit(dirt, (click_cell_coord[0], click_cell_coord[1]))
        pygame.display.flip()


field = Field()

print(field.cells["18"])
size = width, height = field.size * field.cell_width, field.size * field.cell_height
black = 0, 0, 0

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Lakiaro")
grass = pygame.image.load("sprites/grass.png")
dirt = pygame.image.load("sprites/dirt.png")

clock = pygame.time.Clock()
dt = clock.tick(60)

screen.fill(black)

for cell in field.cells.values():
    screen.blit(grass, (cell[0], cell[1]))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            field.open_cell(pygame.mouse.get_pos())

