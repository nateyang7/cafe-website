import random as rd
from typing import Any

class Grid:
    """
    Classe représentant une grille

    Attributes:
        __grid (list[list[Any]]): Une grille 2D d'éléments de type varié
        __lines_count (int): Nombre de lignes de la grille
        __columns_count (int): Nombre de colonnes de la grille
    """

    def __init__(self, grid_init: list[list[Any]]):
        """
        Initialise une grille

        Args:
            grid_init (list[list[Any]]): Grille 2D d'éléments de type varié
        """
        self.__grid = grid_init
        self.__lines_count = len(grid_init)
        self.__columns_count = len(grid_init[0]) if len(grid_init) else 0

    def get_grid(self) -> list[list[Any]]:
        """ Getter de l'attribut __grid de la grille """
        return self.__grid

    def get_lines_count(self) -> int:
        """ Getter de l'attribut __lines_count de la grille """
        return self.__lines_count

    def get_columns_count(self):
        """ Getter de l'attribut __columns_count de la grille """
        return self.__columns_count

    def fill(self, value: Any) -> None:
        """ Rempli la grille avec une valeur """
        self.__grid = [[value] * self.__columns_count for _ in range(self.__lines_count)]

    def fill_random(self, values: list[Any]) -> None:
        """
        Rempli la grille de valeurs aléatoires d'une liste

        Args:
            values (list[Any]): Une liste d'éléments de type varié
        """
        self.__grid = [[rd.choice(values) for _ in range(self.__columns_count)]
                       for _ in range(self.__lines_count)]

    def get_line(self, line_number: int) -> list[Any]:
        """
        Extrait une ligne selon son numéro dans la grille

        Args:
            line_number (int): Numéro de la ligne à extraire
        Returns:
            list[Any]: Ligne numéro line_number de la grille
        """
        return self.__grid[line_number]

    def get_column(self, column_number: int) -> list[Any]:
        """
        Extrait la colonne selon numéro dans la grille

        Args:
            column_number (int): Numéro de la colonne à extraire
        Returns:
            list[Any]: Colonne numéro column_number de la grille
        """
        return [line[column_number] for line in self.__grid]

    def get_diagonal(self) -> list[Any]:
        """ Extrait la diagonale de la grille """
        diagonal_size = min(self.__lines_count, self.__columns_count)
        return [self.__grid[line_number][line_number] for line_number in range(diagonal_size)]

    def get_anti_diagonal(self) -> list[Any]:
        """ Extrait l'antidiagonale de la grille """
        diagonal_size = min(self.__lines_count, self.__columns_count)
        return [self.__grid[line_number][self.__columns_count - line_number - 1]
                for line_number in range(diagonal_size)]

    def get_line_str(self, line_number: int, separator: str='\t') -> str:
        """
        Récupère une ligne sous la forme d'une chaîne de caractères selon son
        numéro dans la grille

        Args:
            line_number (int): Numéro de la ligne à extraire
            separator (str): Caractère qui sépare chaque caractère de la ligne
        Returns:
            str: Concaténation des valeurs de la ligne numéro line_number de
            la grille dont chaque caractère est séparé par separator
        """
        return separator.join(str(value) for value in self.__grid[line_number])

    def get_grid_str(self, separator: str='\t') -> str:
        """
        Retourne la chaine de caractère représentant la grille

        Args:
            separator (str): Caractère qui sépare les caractères de chaque ligne
            de la grille
        Returns:
            str: Chaîne dee caractère représentant la grille dont chaque
            caractère des lignes est séparé par separator avec un caractère
            de retour à la ligne à la fin de chaque ligne
        """
        return '\n'.join(self.get_line_str(line_number, separator) for line_number in range(self.__lines_count))

    def has_equal_values(self, value: Any) -> bool:
        """ Teste si toutes les valeurs de la grille sont égales à 'value' """
        return all([all([value == grid_value for grid_value in line]) for line in self.__grid])

    def is_square(self) -> bool:
        """ Teste si la grille a le même nombre de lignes et de colonnes """
        return self.__lines_count == self.__columns_count

    def get_count(self, value: Any) -> int:
        """ Compte le nombre d'occurrences de 'value' dans la grille """
        return sum(line.count(value) for line in self.__grid)

    def get_sum(self) -> int:
        """ Fait la somme de tous les éléments de la grille """
        return sum(sum(line) for line in self.__grid)

    def get_coordinates_from_cell_number(self, cell_number: int) -> tuple[int, int]:
        """
        Converti un numéro de case 'cell_number' de la grille vers les
        coordonnées (ligne, colonne) correspondants.
        """
        return cell_number // self.__columns_count, cell_number % self.__columns_count

    def get_cell_number_from_coordinates(self, line_number: int, column_number: int) -> int:
        """
        Converti les coordonnées ('line_number', 'column_number') de la grille
        vers le numéro de case correspondant.
        """
        return line_number * self.__columns_count + column_number

    def get_cells_list(self) -> list[int]:
        """ Renvoie une liste des numéros de cases de la grille """
        return [cell_number for cell_number in range(self.__lines_count * self.__columns_count)]

    def get_coordinates_list(self) -> list[tuple[int, int]]:
        """ Renvoie une liste des coordonnées des cases de la grille """
        return [self.get_coordinates_from_cell_number(cell_number) for cell_number in self.get_cells_list()]

    def get_cell(self, cell_number: int) -> Any:
        """ Extrait la valeur de la grille en position 'cell_number' """
        line_number, column_number = self.get_coordinates_from_cell_number(cell_number)
        return self.__grid[line_number][column_number]

    def set_cell(self, cell_number: int, value: Any) -> None:
        """ Positionne la valeur 'value' dans la case 'cell_number' de la grille """
        line_number, column_number = self.get_coordinates_from_cell_number(cell_number)
        self.__grid[line_number][column_number] = value

    def get_same_value_cell_numbers(self, value: Any) -> list[int]:
        """ Fourni la liste des numéros des cases à valeur égale à 'value' dans la grille """
        return [cell_number for cell_number in range(self.__lines_count * self.__columns_count)
                if self.get_cell(cell_number) == value]

    def get_neighbour(self, line_number: int, column_number: int, delta: tuple[int, int], is_tore: bool=True) -> Any | None:
        """
        Retourne le voisin de la cellule ('line_number', 'column_number') de la grille. La définition de voisin
        correspond à la distance positionnelle indiquée par le 2-uplet 'delta' = (delta_ligne, delta_colonne). La case
        voisine est alors (ligne + delta_ligne, colonne + delta_colonne).
        Si 'is_tore' est à 'True' le voisin existe toujours en considérant la grille comme un tore.
        Si 'is_tore' est à 'False' retourne 'None' lorsque le voisin est hors de la grille.
        """
        new_line_number, new_column_number = line_number + delta[0], column_number + delta[1]
        if is_tore or 0 <= new_line_number < self.__lines_count and 0 <= new_column_number < self.__columns_count:
            return self.__grid[new_line_number % self.__lines_count][new_column_number % self.__columns_count]
        return None

    def get_neighborhood(self, line_number: int, column_number: int, deltas: list[tuple[int, int]], is_tore: bool=True) -> list[int]:
        """
        Retourne la liste des N voisins de la position ('lins_number', 'column_number') dans la grille correspondant
        aux N 2-uplet (delta_ligne, delta_colonne) fournis par la liste 'deltas'.
        Si 'is_tore' est à 'True' le voisin existe toujours en considérant la grille comme un tore.
        Si 'is_tore' est à 'False' un voisin hors de la grille n'est pas considéré.
        """
        return [self.get_neighbour(line_number, column_number, delta, is_tore)
                for delta in deltas]

    def get_cell_neighbour_number(self, cell_number: int, delta: tuple[int, int], is_tore: bool=True) -> int | None:
        """
        Retourne le numéro de cellule voisine de la cellule 'cell_number' de la grille.
        La définition de voisin correspond à la distance positionnelle indiquée par le
        2-uplet 'delta' = (delta_ligne, delta_colonne).
        La case voisine est alors (ligne + delta_ligne, colonne + delta_colonne).
        Si 'is_tore' est à 'True' le voisin existe toujours en considérant la grille comme un tore.
        Si 'is_tore' est à 'False' retourne 'None' lorsque le voisin est hors de la grille.
        """
        line_number, column_number = self.get_coordinates_from_cell_number(cell_number)
        line_number, column_number = line_number + delta[0], column_number + delta[1]
        if is_tore or 0 <= line_number < self.__lines_count and 0 <= column_number < self.__columns_count:
            line_number %= self.__lines_count
            column_number %= self.__columns_count
            return self.get_cell_number_from_coordinates(line_number, column_number)
        return None

    def get_cell_neighborhood_numbers(self, cell_number: int, deltas: list[tuple[int, int]], is_tore: bool=True) -> list[int]:
        """
        Retourne la liste des N cellules voisines de la position 'cell_number'
        dans la grille correspondant aux N 2-uplet (delta_ligne, delta_colonne) fournis par la liste 'deltas'.
        Si 'is_tore' est à 'True' le voisin existe toujours en considérant la grille comme un tore.
        Si 'is_tore' est à 'False' un voisin hors de la grille n'est pas considéré.
        """
        res = []
        for delta in deltas:
            neighbour = self.get_cell_neighbour_number(cell_number, delta, is_tore)
            if neighbour is not None:
                res.append(neighbour)
        return sorted(res)

    '''
    def get_euclidian_distance_from_coordinates(self, x1: int, y1: int, x2: int,
                                                y2: int) -> float:
        """
        Calcule la distance euclidienne entre deux cases selon leurs coordonnées

        :param x1: Numéro de ligne de la première case
        :type x1: int
        :param y1: Numéro de colonne de la première case
        :type y1: int
        :param x2: Numéro de ligne de la seconde case
        :type x2: int
        :param y2: Numéro de colonne de la seconde case
        :type y2: int
        :return: Distance euclidienne entre C1 (x1, y1) et C2 (x2, y2)
        :rtype: float

        (WIP)
        """
        return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def get_euclidian_distance_from_cell_number(self, cell_number1: int,
                                                cell_number2: int) -> float:
        """
        Calcule la distance euclidienne entre deux cases selon leurs coordonnées

        :param cell_number1: Numéro de la première case
        :param cell_number2: Numéro de la seconde case
        :return: Distance euclidienne entre 'cell_number1' et 'cell_number2'
        :rtype: float

        (WIP)
        """
        coordinates_cell_number1: tuple[
            int, int] = self.get_coordinates_from_cell_number(cell_number1)
        coordinates_cell_number2: tuple[
            int, int] = self.get_coordinates_from_cell_number(cell_number2)
        return sqrt(
            (coordinates_cell_number2[0] - coordinates_cell_number1[0]) ** 2 + (
                        coordinates_cell_number2[1] + coordinates_cell_number1[
                    1]) ** 2)
    '''

    def get_boundary_cells_count(self) -> int:
        """
        Renvoie le nombre de cases sur les bordures de Grid

        Returns:
            int: Nombre de cases sur les bordures de Grid
        """
        return 2 * (self.__lines_count + self.__columns_count)

    def get_boundary_cells_coordinates(self) -> list[tuple[int, int]]:
        """
        Renvoie les coordonnées des cellules sur les bordures de la grille

        Returns:
            list[tuple[int, int]]: Liste des coordonnées cellules sur les bordures de la grille
        """
        borders_coordinates: list[tuple[int, int]] = []
        for j in range(self.__columns_count):
            borders_coordinates.append((0, j))
            borders_coordinates.append((self.__lines_count - 1, j))
        for i in range(1, self.__lines_count - 1):
            borders_coordinates.append((i, 0))
            borders_coordinates.append((i, self.__columns_count - 1))
        return borders_coordinates

    def get_boundary_cells_numbers(self) -> list[int]:
        """
        Renvoie les numéros des cases sur les bordures de la grille

        Returns:
            list[int]: Liste des numéros des cases des bordures de la grille
        """
        return [self.get_cell_number_from_coordinates(coordinates[0],
                                                      coordinates[1]) for
                coordinates in self.get_boundary_cells_coordinates()]

    def __repr__(self) -> str:
        """ Renvoie une représentation de la grille pour le débogage """
        return self.get_grid_str()


if __name__ == "__main__":
    GRID_TEST = Grid([[0, 0], [0, 0]])
    print(GRID_TEST)
    print(GRID_TEST.get_cells_list())
    assert GRID_TEST.get_cells_list() == [0, 1, 2, 3]
    print(GRID_TEST.get_coordinates_list())
    assert GRID_TEST.get_coordinates_list() == [(0, 0), (0, 1), (1, 0), (1, 1)]
    print("All tests passed")