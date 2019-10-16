import sys
import pygame
import time
import pickle
import pipeiaro_sprites as ps


class Cell:
    """Info about cell contain"""

    def __init__(self, num, coord_x, coord_y, fill=0, type=0, fat=0, rotate=0, in_align=0, out_align=0, inverted=False):
        self.num = num
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
        self.image = ""
        self.refresh_sprite()

    def __repr__(self):
        return str(f'Coordinates X:{self.coord_x}; Y:{self.coord_y}\n'
                   f'Fill={self.fill}, Type={self.type}, Fat={self.fat}\n' 
                   f'In allign={self.in_align}, Out allign={self.out_align}\n'
                   f'Rotate={self.rotate} Inverted={self.inverted}')

    def refresh_sprite(self, redraw=True):
        self.image = ps.get_sprite(self.fill, self.type, self.fat)
        self.image = pygame.image.load(self.image).convert()
        if self.fill == 1:  # Root transform
            self.sprite = pygame.transform.rotate(self.image, 90 * self.rotate)
            if self.type == 1 and self.inverted:
                self.sprite = pygame.transform.flip(self.sprite, False, True)
                self.sprite = pygame.transform.rotate(self.sprite, 90)
        else:
            self.sprite = self.image
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
        self.selection = None
        self.sel_seq = []

    def init_cells(self):  # To flip sprites, display need to be initialized first
        cells = {}
        i = 1
        for row in range(0, self.size, 1):
            for col in range(0, self.size, 1):
                cells[str(i)] = Cell(i, col * self.cell_width, row * self.cell_height)
                i += 1
        self.cells = cells

    # Changing cell parameters
    # We can't place it in cell class, because it's button-specific behaviors
    def change_cell_fill(self, click_coord):
        click_cell = self.get_cell_by_coord(pos=click_coord)
        if click_cell is not None:
            click_cell.change_fill()

    def change_cell_type(self, click_coord):
        click_cell = self.get_cell_by_coord(pos=click_coord)
        if click_cell is not None:
            click_cell.change_type()

    def change_cell_fat(self, click_coord):
        click_cell = self.get_cell_by_coord(pos=click_coord)
        if click_cell is not None:
            click_cell.change_fat()

    def change_cell_rotate(self, click_coord):
        click_cell = self.get_cell_by_coord(pos=click_coord)
        if click_cell is not None:
            click_cell.change_rotate()

    def change_cell_inversion(self, click_coord):
        click_cell = self.get_cell_by_coord(pos=click_coord)
        if click_cell is not None:
            click_cell.change_inverted()

    def get_cell_by_coord(self, **coords):
        """
        Returns object of cell by provided coordinates,
        if here is no cell in coordinates, returns None
        """
        if "x_coord" in coords and "y_coord" in coords:
            x_coord = coords["x_coord"]
            y_coord = coords["y_coord"]
        elif "pos" in coords:
            x_coord = coords["pos"][0]
            y_coord = coords["pos"][1]
        else:
            return None

        if x_coord < self.cell_width * self.size and y_coord < self.cell_height * self.size:
            cell_number = ((x_coord // self.cell_width) + 1) + ((y_coord // self.cell_height) * self.size)
            cell_object = self.cells[str(cell_number)]
            return cell_object
        return None

    def backlight(self,sprite, mouse_coord):
        """
        Draws backlight contour at cell
        """
        hover_cell = self.get_cell_by_coord(pos=mouse_coord)

        if hover_cell is not None:
            if self.selection != hover_cell:
                screen.blit(sprite, (hover_cell.coord_x, hover_cell.coord_y)) # Draw marker
                if self.selection is not None:
                    self.selection.draw()
                self.selection = hover_cell
                pygame.display.flip()
        pass

    def draw(self):
        for cell in self.cells.values():
            screen.blit(cell.sprite, (cell.coord_x, cell.coord_y))

    def add_cell_to_seq(self, cell):
        if cell not in self.sel_seq:
            self.sel_seq.append(cell)

    def draw_seq(self):
        for cell in self.sel_seq:
            screen.blit(cell.sprite, (cell.coord_x, cell.coord_y))
            screen.blit(selection_green, (cell.coord_x, cell.coord_y))
        pygame.display.flip()

    def redraw_seq(self):
        for cell in self.sel_seq:
            print(cell.num)

    def clear_sel_seq(self):
        for cell in self.sel_seq:
            screen.blit(cell.sprite, (cell.coord_x, cell.coord_y))
        pygame.display.flip()
        self.sel_seq = []

    def save_field(self, save_path="savegame"):
        with open(save_path, "wb") as f:
            pickle.dump(self, f)
        print("Game saved!")

    def generate_root_by_drag(self):
        length = len(self.sel_seq)
        if length < 6:
            return

        new_fill = 1
        for i, cell in enumerate(self.sel_seq):
            inverted = False

            # Determine root fat # 0 - Thick, 1 - Neck, 2 - Thin
            if i < 4:
                new_fat = 0
            elif i == 4:
                new_fat = 1
            else:
                new_fat = 2

            # Determine root type # 0 - Straight, 1 - Corner, 2 - Tail

            # First is always straight
            if i == 0:
                new_type = 0
                next_cell = self.sel_seq[i + 1]
                if cell.coord_x != next_cell.coord_x:
                    new_rotate = 1
                else:
                    new_rotate = 0

            # Last is always tail
            elif i == length-1:
                new_type = 2
                prev_cell = self.sel_seq[i-1]
                if cell.coord_x != prev_cell.coord_x:
                    if cell.coord_x > prev_cell.coord_x:    # OLD >>> NEW
                        new_rotate = 1
                    else:
                        new_rotate = 3
                elif cell.coord_y > prev_cell.coord_y:  # OLD vvv NEW (cause "y" axis from top to bottom)
                    new_rotate = 0
                else:
                    new_rotate = 2

            # Middle roots
            else:
                prev_cell = self.sel_seq[i-1]
                next_cell = self.sel_seq[i+1]
                if next_cell.coord_x == prev_cell.coord_x or next_cell.coord_y == prev_cell.coord_y:
                    # Straight
                    new_type = 0
                    if cell.coord_x < next_cell.coord_x:
                        new_rotate = 1
                    elif cell.coord_x > next_cell.coord_x:
                        new_rotate = 3
                    elif cell.coord_y < next_cell.coord_y:
                        new_rotate = 0
                    else:
                        new_rotate = 2

                elif new_fat == 1:
                    # Corner neck
                    new_type = 1
                    if prev_cell.coord_y < cell.coord_y and next_cell.coord_x > cell.coord_x: # UP TO RIGHT
                        new_rotate = 0
                    elif prev_cell.coord_x > cell.coord_x and next_cell.coord_y > cell.coord_y: # RIGHT TO DOWN
                        new_rotate = 3
                    elif prev_cell.coord_y > cell.coord_y and next_cell.coord_x < cell.coord_x:  # DOWN TO LEFT
                        new_rotate = 2
                    elif prev_cell.coord_x < cell.coord_x and next_cell.coord_y < cell.coord_y:  # LEFT TO UP
                        new_rotate = 1
                    else:
                        inverted = True
                        # Inverted rotation is counterclockwise !!!
                        if prev_cell.coord_x > cell.coord_x and next_cell.coord_y < cell.coord_y:  # RIGHT TO UP
                            new_rotate = 0
                        elif prev_cell.coord_y < cell.coord_y and next_cell.coord_x < cell.coord_x:  # UP TO LEFT
                            new_rotate = 1
                        elif prev_cell.coord_x < cell.coord_x and next_cell.coord_y > cell.coord_y:  # LEFT TO DOWN
                            new_rotate = 2
                        elif prev_cell.coord_y > cell.coord_y and next_cell.coord_x > cell.coord_x:  # DOWN TO RIGHT
                            new_rotate = 3

                else:
                    # Corner middle
                    new_type = 1
                    if prev_cell.coord_y < cell.coord_y and next_cell.coord_x > cell.coord_x:  # UP TO RIGHT
                        new_rotate = 0
                    elif prev_cell.coord_x > cell.coord_x and next_cell.coord_y > cell.coord_y:  # RIGHT TO DOWN
                        new_rotate = 3
                    elif prev_cell.coord_y > cell.coord_y and next_cell.coord_x < cell.coord_x:  # DOWN TO LEFT
                        new_rotate = 2
                    elif prev_cell.coord_x < cell.coord_x and next_cell.coord_y < cell.coord_y:  # LEFT TO UP
                        new_rotate = 1

            cell.fill = new_fill
            cell.type = new_type
            cell.fat = new_fat
            cell.rotate = new_rotate
            cell.inverted = inverted
            cell.refresh_sprite()


pygame.init()

field = Field()
size = width, height = field.size * field.cell_width + 200, field.size * field.cell_height
screen = pygame.display.set_mode(size)
field.init_cells()

black = 0, 0, 0
pygame.display.set_caption("Lakiaro Editor")
selection = ps.get_selection_sprites()
selection_blue = selection["blue"]
selection_green = selection["green"]

screen.fill(black)

field.draw()

pygame.display.flip()

root_drag = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                root_drag = True
                selected_cell = field.get_cell_by_coord(pos=pygame.mouse.get_pos())
                field.add_cell_to_seq(selected_cell)
            if event.button == 2:
                field.change_cell_type(pygame.mouse.get_pos())
            if event.button == 3:
                field.change_cell_fat(pygame.mouse.get_pos())
            if event.button == 4:
                field.change_cell_rotate(pygame.mouse.get_pos())
            if event.button == 5:
                field.change_cell_inversion(pygame.mouse.get_pos())

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                root_drag = False
                if len(field.sel_seq) > 1:
                    field.generate_root_by_drag()
                    field.redraw_seq()
                else:
                    field.change_cell_fill(pygame.mouse.get_pos())
                field.clear_sel_seq()

        if event.type == pygame.MOUSEMOTION:
            if root_drag:
                selected_cell = field.get_cell_by_coord(pos=pygame.mouse.get_pos())
                field.add_cell_to_seq(selected_cell)
                field.draw_seq()
                field.backlight(selection_green, pygame.mouse.get_pos())
            else:
                field.backlight(selection_blue, pygame.mouse.get_pos())

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F1:
                click_cell = field.get_cell_by_coord(pos=pygame.mouse.get_pos())
                print(click_cell)
            if event.key == pygame.K_F2:
                for cell in field.cells.values():
                    print(cell)
            if event.key == pygame.K_F5:
                field.draw()
            if event.key == pygame.K_F9:
                field.save_field()
