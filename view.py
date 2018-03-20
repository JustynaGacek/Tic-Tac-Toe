from abc import ABC
from abc import abstractmethod


class ViewInterface(ABC):
    @abstractmethod
    def print_board(self):
        pass


class View(ViewInterface):
    user_symbol = [' ', 'X', 'O']

    @staticmethod
    def clear_screen():
        pass


    def print_board(self, board):
        data = board.get_board()
        View.clear_screen()
        for a in data:
            print("| {} | {} | {} |\n".format(self.user_symbol[a[0]],
                                              self.user_symbol[a[1]],
                                              self.user_symbol[a[2]]))
