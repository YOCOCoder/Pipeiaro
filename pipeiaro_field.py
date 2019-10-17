import pygame
import pickle
import pipeiaro_cell as cl
import tkinter
# from tkinter import messagebox
from tkinter import filedialog
import os
import pygame as pg
import pipeiaro_field


class Field:
    menu_width = 150

    def __init__(self, size=12):
        self.cells = {}
        self.size = size
        self.cell_width = 48
        self.cell_height = 48
        size = self.size * self.cell_width + Field.menu_width, self.size * self.cell_height
        self.screen = pygame.display.set_mode(size)
        self.selection = None
        self.sel_seq = []
        self.save_path = ""

    def init_cells(self):  # To flip sprites, display need to be initialized first
        """assign dictionary of empty cells (dirt) to field"""
        cells = {}
        i = 1
        for row in range(0, self.size, 1):
            for col in range(0, self.size, 1):
                cells[str(i)] = cl.Cell(self.screen, col * self.cell_width, row * self.cell_height)
                i += 1
        self.cells = cells
        self.generate_middle()

    def generate_middle(self, pos_x=5, pos_y=5, width=4, height=4):
        cell_nums = []
        start_pos = pos_y * self.size - (self.size - pos_x)
        for row in range(0, height):
            for col in range(0, width):
                cell_nums.append(str(start_pos + row * self.size + col))
        for cell_num in cell_nums:
            self.cells[cell_num].change_fill(3)

    # Changing cell parameters
    # We can't place it in cell class, cause it's button-specific behaviors
    def change_cell_fill(self, click_coord, ch_type=-1):
        click_cell = self.get_cell_by_coord(pos=click_coord)
        if click_cell is not None:
            click_cell.change_fill(ch_type)

    def change_cell_type(self, click_coord, ch_type=-1):
        click_cell = self.get_cell_by_coord(pos=click_coord)
        if click_cell is not None:
            click_cell.change_type(ch_type)

    def change_cell_fat(self, click_coord, ch_type=-1):
        click_cell = self.get_cell_by_coord(pos=click_coord)
        if click_cell is not None:
            click_cell.change_fat(ch_type)

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

    def backlight(self, sprite, mouse_coord):
        """
        Draws backlight contour at cell
        """
        hover_cell = self.get_cell_by_coord(pos=mouse_coord)
        if hover_cell is not None:
            if self.selection != hover_cell:
                self.screen.blit(sprite, (hover_cell.coord_x, hover_cell.coord_y))  # Draw marker
                if self.selection is not None:
                    self.selection.draw()
                self.selection = hover_cell
                pygame.display.flip()

    def draw(self, refresh=False):
        """redraws sprite of every cell
        if refresh is True - also regenerates
        sprites for cells """
        if refresh:
            for cell in self.cells.values():
                cell.refresh_sprite()
        for cell in self.cells.values():
            self.screen.blit(cell.sprite, (cell.coord_x, cell.coord_y))

    # Drag selection sequence
    def add_cell_to_seq(self, cell):
        """adds cell to selection sequence"""
        if cell not in self.sel_seq:
            self.sel_seq.append(cell)

    def draw_seq(self, sel_sprite):
        """draws marker at selection sequence"""
        for cell in self.sel_seq:
            self.screen.blit(cell.sprite, (cell.coord_x, cell.coord_y))
            self.screen.blit(sel_sprite, (cell.coord_x, cell.coord_y))
        pygame.display.flip()

    def clear_sel_seq(self):
        """clear selection sequence, and removes selection marker"""
        for cell in self.sel_seq:
            self.screen.blit(cell.sprite, (cell.coord_x, cell.coord_y))
        pygame.display.flip()
        self.sel_seq = []

    def generate_root_by_drag(self):
        """generates root at selection sequence"""
        length = len(self.sel_seq)

        if length < 6:
            return

        new_fill = 1
        for i, cell in enumerate(self.sel_seq):
            inverted = False
            new_rotate = 0

            # Root fat # 0 - Thick, 1 - Neck, 2 - Thin
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
            elif i == length - 1:
                new_type = 2
                prev_cell = self.sel_seq[i - 1]
                if cell.coord_x != prev_cell.coord_x:
                    if cell.coord_x > prev_cell.coord_x:  # OLD >>> NEW
                        new_rotate = 1
                    else:
                        new_rotate = 3
                elif cell.coord_y > prev_cell.coord_y:  # OLD vvv NEW (cause "y" axis from top to bottom)
                    new_rotate = 0
                else:
                    new_rotate = 2

            # Middle roots
            else:
                prev_cell = self.sel_seq[i - 1]
                next_cell = self.sel_seq[i + 1]
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
                    # Counterclockwise
                    if prev_cell.coord_y < cell.coord_y and next_cell.coord_x > cell.coord_x:  # UP TO RIGHT
                        new_rotate = 0
                    elif prev_cell.coord_x > cell.coord_x and next_cell.coord_y > cell.coord_y:  # RIGHT TO DOWN
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
                            new_rotate = 3
                        elif prev_cell.coord_x < cell.coord_x and next_cell.coord_y > cell.coord_y:  # LEFT TO DOWN
                            new_rotate = 2
                        elif prev_cell.coord_y > cell.coord_y and next_cell.coord_x > cell.coord_x:  # DOWN TO RIGHT
                            new_rotate = 1

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

                    elif prev_cell.coord_x > cell.coord_x and next_cell.coord_y < cell.coord_y:  # RIGHT TO UP
                        new_rotate = 0
                    elif prev_cell.coord_y < cell.coord_y and next_cell.coord_x < cell.coord_x:  # UP TO LEFT
                        new_rotate = 1
                    elif prev_cell.coord_x < cell.coord_x and next_cell.coord_y > cell.coord_y:  # LEFT TO DOWN
                        new_rotate = 2
                    elif prev_cell.coord_y > cell.coord_y and next_cell.coord_x > cell.coord_x:  # DOWN TO RIGHT
                        new_rotate = 3

            cell.fill = new_fill
            cell.type = new_type
            cell.fat = new_fat
            cell.rotate = new_rotate
            cell.inverted = inverted
            cell.refresh_sprite()

    # Field save and load
    def save_field(self, force = False):
        """saves field in specified file"""
        if len(self.save_path) > 0 and not force:
            self.save_sequence()
        else:
            tkinter.Tk().withdraw()
            curr_dir = os.getcwd()
            file_path = filedialog.asksaveasfilename(initialdir=curr_dir, title="Select file", filetypes=(
                ("Lakiaro grid file (.lkg)", "*.lkg"), ("all files", "*.*"))) + ".lkg"
            if len(file_path) > 0:
                self.save_path = file_path
                self.save_sequence()

    def save_sequence(self):
        # Cleaning object of dynamic generated stuff, that cannot be pickled
        self.screen = None
        self.sel_seq = []
        self.selection = None
        for copy_cell in self.cells.values():
            copy_cell.sprite = None
            copy_cell.image = None
            copy_cell.screen = None

        output = open(self.save_path, "wb")
        pickle.dump(self, output)
        output.close()
        print("Field saved!")
        self.reassign_data()

    def load_field(self, load_path="savegame.lkg"):
        """loads field from specified file"""

        curr_dir = os.getcwd()
        tkinter.Tk().withdraw() # use to hide tkinter window
        file_path = filedialog.askopenfilename(initialdir=curr_dir,
                                               title="Select file",
                                               filetypes=(("Lakiaro grid file (.lkg)", "*.lkg"),
                                                         ("all files", "*.*")))

        if len(file_path) > 0:
            input_file = open(file_path, "rb")
            loaded = pickle.load(input_file)
            input_file.close()
            print("Field loaded!")

            self.cells = loaded.cells
            self.size = loaded.size
            self.cell_width = loaded.cell_width
            self.cell_height = loaded.cell_height
            self.cells = loaded.cells

            self.reassign_data()

    def reassign_data(self):
        """assign dynamic generated data to Field, when save/loading"""
        size = self.size * self.cell_width, self.size * self.cell_height
        screen = pygame.display.set_mode(size)
        self.screen = screen
        for cell in self.cells.values():
            cell.screen = screen
            cell.refresh_sprite()
        pygame.display.flip()
