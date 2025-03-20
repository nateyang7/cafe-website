import tkinter as tk
import random as rd

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 50
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BG_COLOR = "#000000"


class Snake:

    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares: list[int] = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append((0, 0))

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y,
                                             x + SPACE_SIZE, y + SPACE_SIZE,
                                             fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)


class Food:

    def __init__(self):
        x = rd.randint(0, GAME_WIDTH // SPACE_SIZE - 1) * SPACE_SIZE
        y = rd.randint(0, GAME_HEIGHT // SPACE_SIZE - 1) * SPACE_SIZE

        self.coordinates = (x, y)

        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE,
                           fill=FOOD_COLOR, tag="food")


def next_turn():
    pass


def change_direction(new_direction):
    pass


def check_collisions():
    pass


def game_over():
    pass


app = tk.Tk()
app.title("Snake game")
app.resizable(False, False)

score = 0
direction = "down"

label = tk.Label(app, text=f"Score: {score}", font=("consolas", 40))
label.pack()

canvas = tk.Canvas(app, bg=BG_COLOR, height=GAME_HEIGHT,
                   width=GAME_WIDTH)
canvas.pack()

app.update()

app_width = app.winfo_width()
app_height = app.winfo_height()
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()

x = int((screen_width / 2) - (app_width / 2))
y = int((screen_height / 2) - (app_height / 2))

app.geometry(f"{app_width}x{app_height}+{x}+{y}")

snake = Snake()
food = Food()


app.mainloop()
