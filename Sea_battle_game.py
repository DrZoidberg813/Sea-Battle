class Game:
    def __init__(self):
        self.players_ships = []
        self.computer_ships = []
        self.player_field = [["| O", "| O", "| O", "| O", "| O", "| O "],
                             ["| O", "| O", "| O", "| O", "| O", "| O "],
                             ["| O", "| O", "| O", "| O", "| O", "| O "],
                             ["| O", "| O", "| O", "| O", "| O", "| O "],
                             ["| O", "| O", "| O", "| O", "| O", "| O "],
                             ["| O", "| O", "| O", "| O", "| O", "| O "]]
        self.computer_field = [["| O", "| O", "| O", "| O", "| O", "| O "],
                               ["| O", "| O", "| O", "| O", "| O", "| O "],
                               ["| O", "| O", "| O", "| O", "| O", "| O "],
                               ["| O", "| O", "| O", "| O", "| O", "| O "],
                               ["| O", "| O", "| O", "| O", "| O", "| O "],
                               ["| O", "| O", "| O", "| O", "| O", "| O "]]

    def is_ship_where(self, x, y , x1, y1):
        for i in self.players_ships:
            if -2 < i.get_x - x < 2 and -2 < i.get_y - y < 2 or -2 < i.get_x1 - x1 < 2 and -2 < i.get_y1 - y1 < 2:
                pass
        return False

    def player_ships_inp(self):
        while True:
            x, y, x1, y1 = map(int, input("Введите координаты для корабля на 3 клетки (x,y)(x,y): ").split())
            if x+y-x1-y1 == -2 or x+y-x1-y1 == 2:
                self.players_ships.append(Ship(x-1, y-1, x1-1, y1-1))
                break
            else:
                print("Введены координаты больше или меньше 3 клеток")
            for i in range(2):
                x, y, x1, y1 = map(int, input("Введите координаты для корабля на 2 клетки (x,y)(x,y): ").split())
                if x + y - x1 - y1 == -1 or x + y - x1 - y1 == 1 and not self.is_ship_where(x - 1, y - 1, x1 - 1, y1 - 1):
                    self.players_ships.append(Ship(x - 1, y - 1, x1 - 1, y1 - 1))
                    break
                else:
                    print("Введены координаты больше или меньше 2 клеток")
            for i in range(4):
                x, y = map(int, input("Введите координаты для корабля на 1 клетку (x,y): ").split())
                if x - y == 0:
                    self.players_ships.append(Ship(x - 1, y - 1))
                    break
                else:
                    print("Введены координаты больше или меньше 3 клеток")

    def game_field(self):
        print("  | 1 | 2 | 3 | 4 | 5 | 6        | 1 | 2 | 3 | 4 | 5 | 6 ")
        for i, j in enumerate(self.player_field):
            print(i + 1, *j, "   ", i + 1, *self.computer_field[i])

    def start_game(self):
        self.player_ships_inp()
        print("         --> You                           Computer")
        self.game_field()
        count = 1
        """while True:
            if count % 2 == 0:
                print("         --> You                           Computer")
            else:
                print("             You                        -->Computer")
            self.game_field()
            count += 1
            if count == 3:
                break"""


class Ship:
    def __init__(self, x, y, x1=None, y1=None):
        self.x = x
        self.y = y
        self.x1 = x1
        self.y1 = y1

    @property
    def get_x(self):
        return self.x

    @property
    def get_y(self):
        return self.y

    @property
    def get_x1(self):
        return self.x1

    @property
    def get_y1(self):
        return self.y1


def main():
    test = Game()
    test.start_game()


if __name__ == '__main__':
    main()
