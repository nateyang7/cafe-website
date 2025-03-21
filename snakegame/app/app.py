import random as rd
import tkinter as tk
from snakegame.element import Food, Snake

class App(tk.Tk):
    """
    Classe permettant de représenter le jeu snake
    """
    GAME_WIDTH: int = 700
    GAME_HEIGHT: int = 700
    SPEED: int = 100 # Default: 50
    SPACE_SIZE: int = 50
    BACKGROUND_COLOR = "#000000"

    def __init__(self) -> None:
        super().__init__()
        self.title("Snake Game")
        self.resizable(False, False)
        self.score: int = 0
        self.direction: str = "down"
        self.food: Food = Food()
        self.snake: Snake = Snake()
        self.score_label: tk.Label = tk.Label(
            self, text=f"Score: {self.score}", font=("consolas", 40)
        )
        self.score_label.pack()
        self.canvas: tk.Canvas = tk.Canvas(
            self, bg=self.BACKGROUND_COLOR, height=self.GAME_HEIGHT,
            width=self.GAME_WIDTH
        )
        self.canvas.pack()
        self.center_window()
        self.init_keybindings()
        self.init_snake_coordinates_and_squares()
        self.init_food_coordinates()
        self.spawn_food(self.food)
        self.next_turn()
        self.mainloop()

    def center_window(self) -> None:
        """
        Centre la fenêtre principale en fonction de l'écran de l'utilisateur
        """
        self.update()
        window_width: int = self.winfo_width()
        window_height: int = self.winfo_height()
        screen_width: int = self.winfo_screenwidth()
        screen_height: int = self.winfo_screenheight()
        x: int = int((1 / 2) * (screen_width - window_width))
        y: int = int((1 / 2) * (screen_height - window_height))
        self.geometry(f"{window_width}x{window_height}+{x}+{y}")

    def init_keybindings(self) -> None:
        """ Initialise les touches pour contrôler le serpent """
        self.bind("<Left>", lambda event: self.change_direction("left"))
        self.bind("<Right>", lambda event: self.change_direction("right"))
        self.bind("<Up>", lambda event: self.change_direction("up"))
        self.bind("<Down>", lambda event: self.change_direction("down"))



    def init_food_coordinates(self) -> None:
        """
        Initialise la position de la nourriture
        """
        self.food.x = (rd.randint(0, self.GAME_WIDTH // self.SPACE_SIZE - 1)
                  * App.SPACE_SIZE)
        self.food.y = (rd.randint(0, self.GAME_HEIGHT // self.SPACE_SIZE - 1)
                  * App.SPACE_SIZE)

    def init_snake_coordinates_and_squares(self) -> None:
        """
        Initialise les coordonnées et les cases du serpent
        """
        for body_part in range(0, self.snake.body_parts):
            self.snake.coordinates.append((0, 0))
        for x, y in self.snake.coordinates:
            square = self.canvas.create_rectangle(
                x, y, x + self.SPACE_SIZE, y + self.SPACE_SIZE,
                fill=self.snake, tag="snake"
            )
            self.snake.squares.append(square)


    def spawn_food(self, food: Food) -> None:
        """ Dessine la nourriture sur le canvas """
        self.canvas.create_oval(
            self.food.x, self.food.y, self.food.x + self.SPACE_SIZE,
        self.food.y + self.SPACE_SIZE, fill=self.food, tag="food")

    # Game states
    def next_turn(self) -> None:
        x, y = self.snake.coordinates[0]

        if self.direction == "up":
            y -= self.SPACE_SIZE
        elif self.direction == "down":
            y += self.SPACE_SIZE
        elif self.direction == "left":
            x -= self.SPACE_SIZE
        elif self.direction == "right":
            x += self.SPACE_SIZE

        self.snake.coordinates.insert(0, (x, y))

        # Mets à jour les mouvements du serpent
        square = self.canvas.create_rectangle(
            x, y, x + self.SPACE_SIZE, y + self.SPACE_SIZE, fill=self.snake)
        self.snake.squares.insert(0, square)
        del self.snake.coordinates[-1]
        self.canvas.delete(self.snake.squares[-1])
        del self.snake.squares[-1]

        # Prochain tour
        self.after(self.SPEED, self.next_turn)

    def change_direction(self, new_direction: str) -> None:
        """
        Change la direction du serpent en fonction de la touche appuyée

        Args:
            new_direction (str): La nouvelle direction
        """
        if new_direction == "left":
            if self.direction != "right":
                self.direction = new_direction
        elif new_direction == "right":
            if self.direction != "left":
                self.direction = new_direction
        elif new_direction == "up":
            if self.direction != "down":
                self.direction = new_direction
        elif new_direction == "down":
            if self.direction != "up":
                self.direction = new_direction

    def check_collisions(self) -> None:
        """

        Returns:

        """
        pass



if __name__ == "__main__":
    APP_TEST = App()
