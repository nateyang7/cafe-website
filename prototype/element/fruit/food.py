from ..element import Element

class Food(Element):
    FOOD_COLOR = "#FF0000"

    def __init__(self) -> None:
        super().__init__(self.FOOD_COLOR)
        self.x: int = 0
        self.y: int = 0
        self.coordinates: list[int] = [self.x, self.y]