import sys
import pygame
import pipeiaro_sprites as ps
import pipeiaro_field as pf
import pipeiaro_button as btn

pygame.init()

field = pf.Field()
screen = field.screen
field.init_cells()

bg_color = 200, 200, 200
pygame.display.set_caption("Lakiaro Editor")
sel = ps.get_selection_sprites()
selection_blue = sel["blue"]
selection_green = sel["green"]

btn_height = 60
menu_buttons = {
    "new": btn.Button(field=field,
                      id=1,
                      button_image="sprites/menu/editor/button.png",
                      text_image="sprites/menu/editor/new_text.png",
                      pos_x=0,
                      pos_y=0,
                      width=150,
                      height=btn_height,
                      acton="new")


}

screen.fill(bg_color)

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

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                root_drag = False
                if len(field.sel_seq) > 1:
                    field.generate_root_by_drag()
                else:
                    field.change_cell_fill(pygame.mouse.get_pos())
                field.clear_sel_seq()

        if event.type == pygame.MOUSEMOTION:
            if root_drag:
                selected_cell = field.get_cell_by_coord(pos=pygame.mouse.get_pos())
                field.add_cell_to_seq(selected_cell)
                field.draw_seq(selection_green)
                field.backlight(selection_green, pygame.mouse.get_pos())
            else:
                field.backlight(selection_blue, pygame.mouse.get_pos())

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                field.change_cell_rotate(pygame.mouse.get_pos())
            if event.key == pygame.K_f:
                field.change_cell_fat(pygame.mouse.get_pos())
            if event.key == pygame.K_d:
                field.change_cell_type(pygame.mouse.get_pos())
            if event.key == pygame.K_g:
                field.change_cell_inversion(pygame.mouse.get_pos())
            if event.key == pygame.K_SPACE:
                field.change_cell_fill(pygame.mouse.get_pos(), 0)

            if event.key == pygame.K_F1:
                click_cell = field.get_cell_by_coord(pos=pygame.mouse.get_pos())
                print(click_cell)
            if event.key == pygame.K_F2:
                pass
            if event.key == pygame.K_F5:
                field.draw()
            if event.key == pygame.K_F9:
                field.save_field()
            if event.key == pygame.K_F10:
                field.load_field()
