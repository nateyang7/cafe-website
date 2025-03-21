from typing import Any

class Element:
    """
    Classe représentant un élément par un caractère unicode

    Attributes:
        __char_repr (str): Caractère unicode qui représente l'élément
    """

    def __init__(self, char_repr: str) -> None:
        """
        Initialise un élément

        Args:
            char_repr (str): Caractère unicode
        """
        self.__char_repr: str = char_repr

    def __repr__(self) -> str:
        """ Renvoie une représentation de l'élément pour le débogage """
        return self.__char_repr

    def __eq__(self, other: Any) -> bool:
        """
        Comparer deux instances d'Element pour une égalité

        Args:
            other (Any): Instance à comparer avec l'élément
        Returns:
            bool: True si les deux instances ont le même caractère unicode et
            classe sinon False
        """
        return self.__char_repr == other.__char_repr if isinstance(other,
                                                                   Element) else False

