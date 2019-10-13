import sys
import pygame
import time
import pickle


class Field:

    def __init__(self, size=12):
        self.size = size
        cells = {}
        self.cell_width = 48
        self.cell_height = 48
        self.selection = (0, 0)

        i = 1
        for row in range(0, size, 1):
            for col in range(0, size, 1):
                cells[str(i)] = {
                                    "coord": (col * self.cell_width, row * self.cell_height),   # Cell draw coordinates
                                    "fill": 0,  # 1 - Root, 2 - Stone, 3 - Lakiaro
                                    "type": 0,  # 1 - Straight, 2 - Corner, 3 - Tail
                                    "fat": 0,   # 1 - Thick, 2 - Neck, 3 - Thin
                                    "rotate": 0,    # clockwise rotate 1 - 90 degrees, 2 - 180, 3 - 270
                                    "in_align":0,   # align at in position 1 - left, 2 - middle, 3 - right
                                    "out_align":0   # align at out position 1 - left, 2 - middle, 3 - right
                                }
                i += 1
        self.cells = cells

    def open_cell(self, click_coord):
        click_cell = self.get_cell_by_coord(x_coord=click_coord[0], y_coord=click_coord[1])
        if click_cell != None:
            click_cell_coord = self.cells[str(click_cell)]["coord"]
            screen.blit(dirt, (click_cell_coord[0], click_cell_coord[1]))
            pygame.display.flip()

    def get_cell_by_coord(self, x_coord, y_coord):
        '''
        Returns number of cell by provided coordinates,
        if here is no cell in coordinates, returns None
        :param x coordinates:
        :param y coordinates:
        :return: int cell number
        '''
        if x_coord < self.cell_width * self.size and y_coord < self.cell_height * self.size:
            return ((x_coord // self.cell_width) + 1) + ((y_coord // self.cell_height) * self.size)
        return None

    def backlight(self,mouse_coord):
        hover_cell = self.get_cell_by_coord(x_coord=mouse_coord[0], y_coord=mouse_coord[1])

        if hover_cell is not None:
            hover_cell_coord = self.cells[str(hover_cell)]["coord"]

            if hover_cell_coord != self.selection:
                screen.blit(selection, (hover_cell_coord[0], hover_cell_coord[1]))
                pygame.display.flip()

                if self.selection != hover_cell_coord:
                    screen.blit(grass, (self.selection[0], self.selection[1]))
                    self.selection = hover_cell_coord
                    pygame.display.flip()

    def redraw_cell(self):
        pass

    def redraw_grid(self):
        pass

    def save_field(self, save_path="savegame"):
        with open(save_path, "wb") as f:
            pickle.dump(self, f)
        print("Game saved!")


pygame.init()

field = Field()

size = width, height = field.size * field.cell_width + 200, field.size * field.cell_height
black = 0, 0, 0

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Lakiaro Editor")
grass = pygame.image.load("sprites/grass.png")
dirt = pygame.image.load("sprites/dirt.png")
selection = pygame.image.load("sprites/selection.png")

clock = pygame.time.Clock()
dt = clock.tick(60)

screen.fill(black)

for cell in field.cells.values():
    screen.blit(grass, (cell["coord"][0], cell["coord"][1]))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            field.open_cell(pygame.mouse.get_pos())
        if event.type == pygame.MOUSEMOTION:
            field.backlight(pygame.mouse.get_pos())
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F1:
                print(field.cells)
            if event.key == pygame.K_F2:
                for cell in field.cells.values():
                    print(cell)
            if event.key == pygame.K_F5:
                field.save_field()

