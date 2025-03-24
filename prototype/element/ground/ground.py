from ..element import Element

class Ground(Element):
    """
    Classe représentant un sol par un élément
    """

    def __init__(self) -> None:
        """
        Initialise un sol
        """
        super().__init__("\u2B1C")