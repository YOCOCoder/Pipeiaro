import tkinter as tk
from tkinter import messagebox
# from tkinter import filedialog
# import os
# import pygame as pg
# import pipeiaro_field


class Menu:

    def __init__(self):
        self.buttons = []

    def add_button(self, **params):
        self.buttons.append(Button(params))


class Button:

    def __init__(self, **params):
        self.field = params["field"]
        self.button_id = params["id"]
        self.button_image = params["button_image"]
        self.text_image = params["text_image"]
        self.pos_x = params["pos_x"]
        self.pos_y = params["pos_y"]
        self.width = params["width"]
        self.height = params["height"]
        self.clicked = False
        self.btn_action = params["acton"]

    def action(self):
        if self.btn_action == "new":
            msg_box = tk.messagebox.askquestion('New Field', 'Are you sure you want to clear the field?\n'
                                                             'This action cannot be undone',
                                                icon='warning')
            if msg_box == 'yes':
                self.field.init_cells()
                self.field.generate_middle()

        elif self.btn_action == "open":
            self.field.load_field()
        elif self.btn_action == "save":
            self.field.save_field()
        elif self.btn_action == "save_as":
            self.field.save_field(force=True)
