from ..element import Element

class Snake(Element):
    """
    Classe représentant un serpent par un élément

    Attributes:
        __body_parts_count (int): Longueur du serpent
        __coordinates (list[tuple[int, int]]): Coordonnées des parties du
        corps du serpent (index 0 = tête du serpent)
        __squares (list[int]): Les cases du corps du serpent sur la grille du jeu
        __alive (bool): Status de vie du serpent (default: True)
    """

    def __init__(self, body_parts_count: int=2) -> None:
        """
        Initialise un serpent

        Args:
            body_parts_count (int): Paramètre qui initialise l'attribut
            body_parts_count (default: 2)
        """
        super().__init__('\U0001F40D')
        self.__body_parts_count: int = body_parts_count
        self.__coordinates: list[tuple[int, int]] = []
        self.__squares: list[int] = []
        self.__alive: bool = True
        #self.__direction: str = "right"

    def get_body_parts_count(self) -> int:
        """ Getter de l'attribut __body_parts_count du serpent """
        return self.__body_parts_count

    def get_coordinates(self) -> list[tuple[int, int]]:
        """ Getter de l'attribut __coordinates du serpent """
        return self.__coordinates

    def get_squares(self) -> list[int]:
        """ Getter de l'attribut __squares du serpent """
        return self.__squares

    def is_alive(self) -> bool:
        """ Teste si le serpent est toujours en vie """
        return self.__alive
