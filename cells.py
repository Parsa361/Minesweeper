import sys
from tkinter import Button, Label, messagebox
import random

import settings


def get_cell_by_axis(x, y):
    for cell in Cell.all:
        if cell.x == x and cell.y == y:
            return cell


class Cell:
    all = []
    cell_count_label_object = None
    cell_count = settings.CELLS_COUNT

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.is_mine = False
        self.is_mine_candidate = False
        self.is_opened = False
        self.cell_btn_object = None

        Cell.all.append(self)

    def create_button_object(self, location):
        btn = Button(
            location,
            bg='green',
            width=12,
            height=4,
        )
        btn.bind('<Button-1>', self.left_click_action)
        btn.bind('<Button-3>', self.right_click_action)
        self.cell_btn_object = btn

    @staticmethod
    def create_cell_count_label(location):
        lbl = Label(
            location,
            bg='black',
            fg='white',
            text=f"Cells Left: {Cell.cell_count}",
            font=("", 30)
        )
        Cell.cell_count_label_object = lbl

    def left_click_action(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounded_cells_length == 0:
                for cell_obj in self.surrounded_cells:
                    cell_obj.show_cell()
            self.show_cell()

            if Cell.cell_count == settings.MINES:
                messagebox.showinfo("Congratulations!", "You won the game!!")
        #     Cancel left and right click events if cell is already opened
        self.cell_btn_object.unbind('<Button-1>')
        self.cell_btn_object.unbind('<Button-3>')

    def show_mine(self):
        self.cell_btn_object.configure(bg='red')
        messagebox.showinfo("You clicked on a mine", "Game Over")
        sys.exit()

    @property
    def surrounded_cells_length(self):
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter += 1
        return counter

    @property
    def surrounded_cells(self):
        cells = [
            get_cell_by_axis(self.x - 1, self.y - 1),
            get_cell_by_axis(self.x - 1, self.y),
            get_cell_by_axis(self.x - 1, self.y + 1),
            get_cell_by_axis(self.x, self.y - 1),
            get_cell_by_axis(self.x, self.y + 1),
            get_cell_by_axis(self.x + 1, self.y - 1),
            get_cell_by_axis(self.x + 1, self.y),
            get_cell_by_axis(self.x + 1, self.y + 1),
        ]
        cells = [cell for cell in cells if cell is not None]
        return cells

    def show_cell(self):
        if not self.is_opened:
            Cell.cell_count -= 1
            self.cell_btn_object.configure(text=self.surrounded_cells_length)
            #     Replace the text of cell count label with the newer count
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(text=f"Cells Left: {Cell.cell_count}")
            #     if this was a mine candidate for safety we should configure the background color to blue
            self.cell_btn_object.configure(bg='green')
        self.is_opened = True

    def right_click_action(self, event):
        if not self.is_mine_candidate:
            self.cell_btn_object.configure(bg='orange')
            self.is_mine_candidate = True
        else:
            self.cell_btn_object.configure(bg='green')

    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(
            Cell.all, settings.MINES
        )
        for picked_cell in picked_cells:
            picked_cell.is_mine = True

    def __repr__(self):
        return f"Cell({self.x},{self.y})"
