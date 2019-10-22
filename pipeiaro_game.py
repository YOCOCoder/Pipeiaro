import sys
import pygame
import time
import pipeiaro_field as pf
import pipeiaro_sprites as ps

pygame.init()


field = pf.Field()
playfield = pf.Playfield(field)
screen = field.screen
field.init_cells(0)
playfield.init_cells(3)

bg_color = 200, 200, 200
pygame.display.set_caption("Lakiaro Game")
sel = ps.get_selection_sprites()
selection_blue = sel["blue"]
selection_green = sel["green"]

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


playfield.draw()

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                playfield.open_cell(pygame.mouse.get_pos())
            if event.button == 2:
                playfield.change_cell_type(pygame.mouse.get_pos())

        # if event.type == pygame.MOUSEBUTTONUP:
        #     if event.button == 1:
        #         root_drag = False
        #         if len(field.sel_seq) > 1:
        #             field.generate_root_by_drag()
        #         else:
        #             field.change_cell_fill(pygame.mouse.get_pos())
        #         field.clear_sel_seq()

        if event.type == pygame.MOUSEMOTION:
            # if root_drag:
            #     selected_cell = field.get_cell_by_coord(pos=pygame.mouse.get_pos())
            #     field.add_cell_to_seq(selected_cell)
            #     field.draw_seq(selection_green)
            #     field.backlight(selection_green, pygame.mouse.get_pos())
            # else:
                playfield.backlight(selection_blue, pygame.mouse.get_pos())

        if event.type == pygame.KEYDOWN:
            # if event.key == pygame.K_r:
            #     field.change_cell_rotate(pygame.mouse.get_pos())
            # if event.key == pygame.K_f:
            #     field.change_cell_fat(pygame.mouse.get_pos())
            # if event.key == pygame.K_d:
            #     field.change_cell_type(pygame.mouse.get_pos())
            # if event.key == pygame.K_g:
            #     field.change_cell_inversion(pygame.mouse.get_pos())
            # if event.key == pygame.K_SPACE:
            #     field.change_cell_fill(pygame.mouse.get_pos(), 0)

            if event.key == pygame.K_F1:
                click_cell = playfield.get_cell_by_coord(pos=pygame.mouse.get_pos())
                print(click_cell)
            if event.key == pygame.K_F2:
                pass
            if event.key == pygame.K_F5:
                playfield.draw()
            if event.key == pygame.K_F9:
                playfield.save_field()
            if event.key == pygame.K_F10:
                playfield.load_field()
