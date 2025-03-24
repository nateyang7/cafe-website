class Element():
    """
    Classe représentant un élément par un caractère
    """

    def __init__(self, char_repr: str) -> None:
        """
        Initialise un élément

        Args:
            char_repr (str): Caractère qui représente l'élément
        """
        self.__char_repr: str = char_repr

    def __repr__(self) -> str:
        """ Renvoie une représentation de l'élément pour le débogage """
        return self.__char_repr

    def __eq__(self, other: object) -> bool:
        """
        Teste si l'instance et un objet possèdent le même caractère

        Args:
            other (object): Un objet à comparer avec l'instance
        Returns:
            bool: True si l'instance et other ont le même caractère sinon False
        """
        return self.__char_repr == other.__char_repr if isinstance(other, Element) else False
