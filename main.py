import tkinter as tk
import random as rd

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 150  # Default: 50
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


def next_turn(snake: Snake, food: Food) -> None:
    x, y = snake.coordinates[0]
    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0, (x, y))
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE,
                                     fill=SNAKE_COLOR)
    snake.squares.insert(0, square)

    # Si la tête du serpent touche la nourriture
    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1
        label.config(text=f"Score: {score}")
        canvas.delete("food")
        food = Food()

    # Sinon le serpent continue de bouger dans la direction choisie
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]
    #app.after(SPEED, next_turn, snake, food)

    # Vérifier les collisions avec le corps
    if check_collisions(snake):  # Si True, la partie est terminée
        game_over()
    else:  # Sinon, le serpent continue de bouger
        app.after(SPEED, next_turn, snake, food)


def change_direction(new_direction):
    global direction
    if new_direction == "left":
        if direction != "right":
            direction = new_direction
    elif new_direction == "right":
        if direction != "left":
            direction = new_direction
    elif new_direction == "up":
        if direction != "down":
            direction = new_direction
    elif new_direction == "down":
        if direction != "up":
            direction = new_direction


def check_collisions(snake) -> bool:
    x, y = snake.coordinates[0]
    if x < 0 or x >= GAME_WIDTH:
        return True
    if y < 0 or y >= GAME_HEIGHT:
        return True

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True
    return False


def game_over():
    canvas.delete(tk.ALL)
    canvas.create_text(canvas.winfo_width() // 2, canvas.winfo_height() // 2,
                       font=("consolas", 70), text="GAME OVER", fill="red",
                       tag="gameover")
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

# KEYBINDS
app.bind('<Left>', lambda event: change_direction('left'))
app.bind('<Right>', lambda event: change_direction("right"))
app.bind("<Up>", lambda event: change_direction("up"))
app.bind("<Down>", lambda event: change_direction("down"))

snake = Snake()
food = Food()

next_turn(snake, food)

app.mainloop()
