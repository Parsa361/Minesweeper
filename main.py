from tkinter import *
import settings
import utils
from cells import Cell

root = Tk()
root.geometry(f"{settings.WIDTH}x{settings.HEIGHT}")
root.title("Minesweeper Game")
root.configure(bg='black')
root.resizable(False, False)

top_frame = Frame(
    root,
    bg='black',
    width=settings.WIDTH,
    height=utils.height_percentage(25)
)
top_frame.place(x=0, y=0)

game_title = Label(
    top_frame,
    bg='black',
    foreground='white',
    text='Minesweeper Game',
    font=("", 40)
)
game_title.place(
    x=utils.width_percentage(30), y=0
)

left_frame = Frame(
    root,
    bg='black',
    width=utils.width_percentage(25),
    height=utils.height_percentage(75)
)
left_frame.place(x=0, y=utils.height_percentage(25))

center_frame = Frame(
    root,
    bg='black',
    width=utils.width_percentage(75),
    height=utils.height_percentage(75)
)
center_frame.place(x=utils.width_percentage(25), y=utils.height_percentage(25))

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x, y)
        c.create_button_object(center_frame)
        c.cell_btn_object.grid(column=y, row=x)

Cell.randomize_mines()
Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(x=0, y=0)

root.mainloop()
