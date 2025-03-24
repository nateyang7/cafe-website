import tkinter as tk
import random as rd
from prototype.element import Food, Snake
from prototype.grid import Grid

class MyApp(tk.Tk):  # Prototype de PlanetTk et SnakeGame
    MAP_WIDTH = 17
    MAP_HEIGHT = 15
    
    def __init__(self, cell_size = 50, gutter_size = 0, margin_size = 0):
        #  --- Paramètre de la fenêtre principale ---
        tk.Tk.__init__(self)
        self.cell_size = cell_size
        self.gutter_size = gutter_size
        self.margin_size = margin_size
        self.speed = 100  # Vitesse du jeu en ms
        self.grid = Grid([[None] * self.MAP_WIDTH for _ in range(self.MAP_HEIGHT)])
        self.title("Snake Game")
        self.canvas_width = (cell_size * self.grid.get_columns_count() + 2 * margin_size +
                       (self.grid.get_columns_count() - 1) * gutter_size)
        self.canvas_height = (cell_size * self.grid.get_lines_count() + 2 * margin_size +
                        (self.grid.get_lines_count() - 1) * gutter_size)
        self.canvas = tk.Canvas(
            self, width=self.canvas_width, height=self.canvas_height,
            bg="#252525"
        )
        self.canvas.pack(side="top")
        self.draw_grid()
        self.buttons_frame = tk.Frame(self)
        self.buttons_frame.pack(side="bottom")
        self.setup_buttons()
        self.center_window()
        self.resizable(False, False)  # Sécurise la taille de la fenêtre

        # --- Elements du jeu ---
        self.snake = Snake()
        self.food = Food()
        self.mainloop()

    # === Méthodes pour la fenêtre ===

    # Grille du canvas
    def draw_grid(self) -> None:
        """
        Dessine la grille sur le canvas
        (OK)
        """
        for cell_number in range(
                self.grid.get_lines_count() * self.grid.get_columns_count()):
            i, j = self.grid.get_coordinates_from_cell_number(cell_number)
            x = j * (self.cell_size + self.gutter_size) + self.margin_size
            y = i * (self.cell_size + self.gutter_size) + self.margin_size
            self.canvas.create_rectangle(
                x, y, x + self.cell_size, y + self.cell_size,
                tags=(f"c_{i}_{j}", f"c_{cell_number}")
            )
            self.canvas.create_text(
                x + self.cell_size // 2, y + self.cell_size // 2,
                font=("Arial", self.cell_size // 5, "bold"),
                tags=(f"t_{i}_{j}", f"t_{cell_number}")
            )

    def set_cell_text(self, cell_number: int, text: str) -> None:
        """
        Modifie le contenu textuel d'une case par son numéro
        Args:
            cell_number (int): Numéro de la case à modifier
            text (str): Texte à placer dans le contenu de la case
        """
        self.canvas.itemconfig(f"t_{cell_number}", text=text)

    # Fenêtre principale
    def center_window(self) -> None:
        """
        Centre la fenêtre principale en fonction de l'écran de l'utilisateur
        (OK)
        """
        self.update()
        window_width: int = self.winfo_width()
        window_height: int = self.winfo_height()
        screen_width: int = self.winfo_screenwidth()
        screen_height: int = self.winfo_screenheight()
        x: int = int((1 / 2) * (screen_width - window_width))
        y: int = int((1 / 2) * (screen_height - window_height))
        self.geometry(f"{window_width}x{window_height}+{x}+{y}")

    def setup_buttons(self):
        """
        Mets en place les éléments de la frame des boutons
        (OK)
        """
        quit_button = tk.Button(self.buttons_frame, text="Quit", command=self.quit)
        play_button = tk.Button(self.buttons_frame, text="Play", command=lambda : self.spawn_food)
        restart_button = tk.Button(self.buttons_frame, text="Restart", command=lambda : print("Restart"))
        for button in (quit_button, play_button, restart_button):
            button.pack(side="right")
        self.update()

    def init_keybindings(self) -> None:
        """ Initialise les touches pour contrôler le serpent """
        self.bind("<Left>", lambda event: self.change_direction("left"))
        self.bind("<Right>", lambda event: self.change_direction("right"))
        self.bind("<Up>", lambda event: self.change_direction("up"))
        self.bind("<Down>", lambda event: self.change_direction("down"))

    # === Méthodes pour le jeu ===

    def init_food_coordinates(self) -> None:
        """
        Initialise la position de la nourriture
        """
        self.food.x = (rd.randint(0, self.canvas_width // self.cell_size - 1)
                  * self.cell_size )
        self.food.y = (rd.randint(0, self.canvas_height // self.cell_size  - 1)
                  * self.cell_size )
        self.grid.set_cell()

    def spawn_food(self) -> None:
        """ Dessine la nourriture sur le canvas """
        self.init_food_coordinates()
        self.canvas.create_oval(
            self.food.x, self.food.y, self.food.x + self.cell_size,
        self.food.y + self.cell_size, fill=self.food, tag="food"
        )
        print(f"Nourriture placé à la case de coordonnées ({self.food.x}, {self.food.y})")

    '''
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
    '''

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

if __name__ == "__main__":
    app = MyApp()