import sys
import pygame
import time
import pickle
import pipeiaro_sprites as sp


class Cell:
    """Info about cell contain"""

    def __init__(self, coord_x, coord_y, fill=0, type=0, fat=0, rotate=0, in_align=0, out_align=0, inverted=False):
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.fill = fill  # 0 - Dirt 1 - Root, 2 - Stone, 3 - Lakiaro
        self.type = type  # 0 - Straight, 1 - Corner, 2 - Tail
        self.fat = fat  # 0 - Thick, 1 - Neck, 2 - Thin
        self.rotate = rotate  # clockwise rotate 1 - 90 degrees, 2 - 180, 3 - 270
        self.in_align = in_align  # align at in position 1 - left, 2 - middle, 3 - right
        self.out_align = out_align  # align at out position 1 - left, 2 - middle, 3 - right
        self.inverted = inverted  # inverted draw direction
        self.sprite = ""
        self.refresh_sprite()

    def __repr__(self):
        return str(f'Coordinates X:{self.coord_x}; Y:{self.coord_y}\n'
                   f'Fill={self.fill}, Type={self.type}, Fat={self.fat}\n' 
                   f'In allign={self.in_align}, Out allign={self.out_align}\n'
                   f'Rotate={self.rotate} Inverted={self.inverted}')

    def refresh_sprite(self, redraw=True):
        self.sprite = sp.get_sprite(self.fill, self.type, self.fat)
        surface = pygame.image.load(self.sprite).convert()
        pygame.transform.rotate(surface, 90 * self.rotate)
        if self.inverted:
            pygame.transform.flip(surface, False, True)
            pygame.transform.rotate(surface, 180)
        self.sprite = surface
        if redraw:
            self.draw()

    def draw(self):
        screen.blit(self.sprite, (self.coord_x, self.coord_y))
        pygame.display.flip()

    def change_fill(self):
        if self.fill < 3:
            self.fill += 1
        else:
            self.fill = 0
        self.refresh_sprite()

    def change_type(self):
        if self.type < 2:
            self.type += 1
        else:
            self.type = 0
        self.refresh_sprite()

    def change_fat(self):
        if self.fat < 2:
            self.fat += 1
        else:
            self.fat = 0
        self.refresh_sprite()

    def change_rotate(self):
        if self.rotate < 3:
            self.rotate += 1
        else:
            self.rotate = 0
        self.refresh_sprite()

    def change_inverted(self):
        self.inverted = not self.inverted
        self.refresh_sprite()

    def get_cell_sprite(self):
        pass


class Field:

    def __init__(self, size=12):
        self.cells = {}
        self.size = size
        self.cell_width = 48
        self.cell_height = 48
        self.selection = (0, 0)

    def init_cells(self):  # To flip sprites, display need to be initialized first
        cells = {}
        i = 1
        for row in range(0, self.size, 1):
            for col in range(0, self.size, 1):
                cells[str(i)] = Cell(col * self.cell_width, row * self.cell_height)
                i += 1
        self.cells = cells

    def change_cell_fill(self, click_coord):
        click_cell = self.get_cell_by_coord(x_coord=click_coord[0], y_coord=click_coord[1])
        if click_cell is not None:
            cell = self.cells[str(click_cell)]
            cell.change_fill()

    def change_cell_type(self, click_coord):
        click_cell = self.get_cell_by_coord(x_coord=click_coord[0], y_coord=click_coord[1])
        if click_cell is not None:
            cell = self.cells[str(click_cell)]
            cell.change_type()

    def change_cell_fat(self, click_coord):
        click_cell = self.get_cell_by_coord(x_coord=click_coord[0], y_coord=click_coord[1])
        if click_cell is not None:
            cell = self.cells[str(click_cell)]
            cell.change_fat()

    def change_cell_rotate(self, click_coord):
        click_cell = self.get_cell_by_coord(x_coord=click_coord[0], y_coord=click_coord[1])
        if click_cell is not None:
            cell = self.cells[str(click_cell)]
            cell.change_rotate()

    def change_cell_inversion(self, click_coord):
        click_cell = self.get_cell_by_coord(x_coord=click_coord[0], y_coord=click_coord[1])
        if click_cell is not None:
            cell = self.cells[str(click_cell)]
            cell.change_inverted()

    def open_cell(self, click_coord):
        click_cell = self.get_cell_by_coord(x_coord=click_coord[0], y_coord=click_coord[1])
        if click_cell is not None:
            current_cell = self.cells[str(click_cell)]
            screen.blit(dirt, (current_cell.coord_x, current_cell.coord_y))
            pygame.display.flip()

    def get_cell_by_coord(self, x_coord, y_coord):
        """
        Returns number of cell by provided coordinates,
        if here is no cell in coordinates, returns None
        :param x coordinates:
        :param y coordinates:
        :return: int cell number
        """
        if x_coord < self.cell_width * self.size and y_coord < self.cell_height * self.size:
            return ((x_coord // self.cell_width) + 1) + ((y_coord // self.cell_height) * self.size)
        return None

    def backlight(self, mouse_coord):
        # hover_cell = self.get_cell_by_coord(x_coord=mouse_coord[0], y_coord=mouse_coord[1])
        #
        # if hover_cell is not None:
        #     hover_cell_coord = self.cells[str(hover_cell)]
        #
        #     if hover_cell_coord != self.selection:
        #         screen.blit(selection, (hover_cell_coord.coord_x, hover_cell_coord.coord_y))
        #         pygame.display.flip()
        #
        #         if self.selection != hover_cell_coord:
        #             screen.blit(grass, (self.selection[0], self.selection[1]))
        #             self.selection = hover_cell_coord
        #             pygame.display.flip()
        pass

    def draw(self):
        for cell in self.cells.values():
            screen.blit(cell.sprite, (cell.coord_x, cell.coord_y))

    def save_field(self, save_path="savegame"):
        with open(save_path, "wb") as f:
            pickle.dump(self, f)
        print("Game saved!")


pygame.init()

field = Field()
size = width, height = field.size * field.cell_width + 200, field.size * field.cell_height
screen = pygame.display.set_mode(size)
field.init_cells()

black = 0, 0, 0
pygame.display.set_caption("Lakiaro Editor")
selection = pygame.image.load("sprites/selection.png")

clock = pygame.time.Clock()
dt = clock.tick(60)

screen.fill(black)

field.draw()

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                field.change_cell_fill(pygame.mouse.get_pos())
            if event.button == 2:
                field.change_cell_type(pygame.mouse.get_pos())
            if event.button == 3:
                field.change_cell_fat(pygame.mouse.get_pos())
            if event.button == 4:
                field.change_cell_rotate(pygame.mouse.get_pos())
            if event.button == 5:
                field.change_cell_inversion(pygame.mouse.get_pos())
        if event.type == pygame.MOUSEMOTION:
            # field.backlight(pygame.mouse.get_pos())
            pass
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F1:
                coord = pygame.mouse.get_pos()
                click_cell = field.get_cell_by_coord(coord[0],coord[1])
                print(field.cells[str(click_cell)])
            if event.key == pygame.K_F2:
                for cell in field.cells.values():
                    print(cell)
            if event.key == pygame.K_F5:
                field.draw()
            if event.key == pygame.K_F9:
                field.save_field()
