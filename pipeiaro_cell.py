import pygame
import pipeiaro_sprites as ps


class Cell:
    """Info about cell contain"""

    def __init__(self, screen, coord_x, coord_y, cell_size = 48, fill=0, root_type=0, fat=0, rotate=0, in_align=0, out_align=0, inverted=False):
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.cell_size = 48
        self.fill = fill  # 0 - Dirt 1 - Root, 2 - Stone, 3 - Lakiaro
        self.root_type = root_type  # 0 - Straight, 1 - Corner, 2 - Tail
        self.fat = fat  # 0 - Thick, 1 - Neck, 2 - Thin
        self.rotate = rotate  # clockwise rotate 1 - 90 degrees, 2 - 180, 3 - 270
        self.in_align = in_align  # align at in position 1 - left, 2 - middle, 3 - right
        self.out_align = out_align  # align at out position 1 - left, 2 - middle, 3 - right
        self.inverted = inverted  # inverted draw direction
        self.sprite = ""
        self.image = ""
        self.screen = screen
        self.refresh_sprite()

    def __repr__(self):
        return str(f'Coordinates X:{self.coord_x}; Y:{self.coord_y}\n'
                   f'Fill={self.fill}, Type={self.root_type}, Fat={self.fat}\n' 
                   f'In allign={self.in_align}, Out allign={self.out_align}\n'
                   f'Rotate={self.rotate} Inverted={self.inverted}')

    def refresh_sprite(self, redraw=True):
        """Update sprite of cell by cell parameters and redraw it"""
        self.image = ps.get_sprite(self.fill, self.root_type, self.fat)
        self.image = pygame.image.load(self.image).convert()
        if self.fill == 1:  # Root transform
            self.sprite = pygame.transform.rotate(self.image, 90 * self.rotate)
            if self.root_type == 1 and self.inverted:
                self.sprite = pygame.transform.flip(self.sprite, False, True)
                self.sprite = pygame.transform.rotate(self.sprite, 90)
        else:
            self.sprite = self.image
        if redraw:
            sprite_rect = pygame.Rect(self.coord_x, self.coord_y,
                                      self.coord_x + self.cell_size, self.coord_y + self.cell_size)
            self.screen.blit(self.sprite, (self.coord_x, self.coord_y))
            pygame.display.update(sprite_rect)

    def draw(self):
        """Draws cell at screen, and redraw it sprite at exact location"""
        self.screen.blit(self.sprite, (self.coord_x, self.coord_y))
        sprite_rect = pygame.Rect(self.coord_x, self.coord_y,
                                  self.coord_x + self.cell_size, self.coord_y + self.cell_size)
        pygame.display.update(sprite_rect)

    def change_fill(self, ch_type):
        """Switch fill type of cell and refresh it sprite"""
        if ch_type == -1:
            if self.fill < 3:
                self.fill += 1
            else:
                self.fill = 0
        else:
            self.fill = ch_type
        self.refresh_sprite()

    def change_type(self, ch_type):
        """Switch root type of cell and refresh it sprite"""
        if ch_type == -1:
            if self.root_type < 2:
                self.root_type += 1
            else:
                self.root_type = 0
        else:
            self.root_type = ch_type
        self.refresh_sprite()

    def change_fat(self, ch_type):
        """Switch root fat type of cell and refresh it sprite"""
        if ch_type == -1:
            if self.fat < 2:
                self.fat += 1
            else:
                self.fat = 0
        else:
            self.fat = ch_type
        self.refresh_sprite()

    def change_rotate(self):
        """Switch rotate statement of cell and refresh it sprite"""
        if self.rotate < 3:
            self.rotate += 1
        else:
            self.rotate = 0
        self.refresh_sprite()

    def change_inverted(self):
        self.inverted = not self.inverted
        self.refresh_sprite()

    def update_display(self, screen):
        self.screen = screen
