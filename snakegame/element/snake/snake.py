from snakegame.element import Element

class Snake(Element):
    """
    Classe représentant un serpent
    """
    SNAKE_COLOR: str = "#00FF00"
    BODY_PARTS: int = 3

    def __init__(self) -> None:
        """
        Initialise un serpent
        """
        super().__init__(self.SNAKE_COLOR)
        self.body_parts: int = self.BODY_PARTS
        self.coordinates: list[tuple[int, int]] = []
        self.squares: list[int] = []


if __name__ == "__main__":
    SNAKE_TEST = Snake()
    print(SNAKE_TEST)
    print("All tests passed")