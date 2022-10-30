import os


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

    @staticmethod
    def is_ship_not_where(ship, x, y, *args):
        if args:
            x1, y1 = map(int, args)
        else:
            x1 = x
            y1 = y
        for i in range(ship.get_x - 1, ship.get_x1 + 2):
            for k in range(ship.get_y - 1, ship.get_y1 + 2):
                if i in range(7) and k in range(7) and (i == x and k == y or i == x1 and k == y1):
                    return False
        return True

    def player_ships_inp(self):
        count = 0
        while True:
            if count == 0:
                x, y, x1, y1 = map(int, input("Введите координаты для корабля на 3 клетки (x,y)(x,y): ").split())
                if x + y - x1 - y1 == -2 or x + y - x1 - y1 == 2:
                    self.players_ships.append(Ship(x - 1, y - 1, x1 - 1, y1 - 1))
                    os.system("cls")
                    self.ship_place()
                    self.game_field()
                    count += 1
                else:
                    print("Введены координаты больше или меньше 3 клеток")
            if 0 < count < 3:
                x, y, x1, y1 = map(int, input("Введите координаты для корабля на 2 клетки (x,y)(x,y): ").split())
                if (x + y - x1 - y1 == -1 or x + y - x1 - y1 == 1) \
                        and all([self.is_ship_not_where(i, x - 1, y - 1, x1 - 1, y1 - 1) for i in self.players_ships]):
                    self.players_ships.append(Ship(x - 1, y - 1, x1 - 1, y1 - 1))
                    os.system("cls")
                    self.ship_place()
                    self.game_field()
                    count += 1
                else:
                    print("Введены координаты больше или меньше 2 клеток")
            if 2 < count < 7:
                x, y = map(int, input("Введите координаты для корабля на 1 клетку (x,y): ").split())
                if all([self.is_ship_not_where(i, x - 1, y - 1) for i in self.players_ships]):
                    self.players_ships.append(Ship(x - 1, y - 1))
                    os.system("cls")
                    self.ship_place()
                    self.game_field()
                    count += 1
                else:
                    print("Введены координаты рядом с другим короблем")
            if count == 7:
                break

    def ship_place(self):
        for ship in self.players_ships:
            if ship.get_x == ship.get_x1:
                for i in range(ship.get_y, ship.get_y1 + 1):
                    self.player_field[ship.get_x][i] = "| -"
            elif ship.get_y == ship.get_y1:
                for i in range(ship.get_x, ship.get_x1 + 1):
                    self.player_field[i][ship.get_y] = "| -"
            if ship.get_x1 is None or ship.get_y1 is None:
                self.player_field[ship.get_x][ship.get_y] = "| -"

    def game_field(self):
        print("  | 1 | 2 | 3 | 4 | 5 | 6        | 1 | 2 | 3 | 4 | 5 | 6 ")
        for i, j in enumerate(self.player_field):
            print(i + 1, *j, "   ", i + 1, *self.computer_field[i])

    def start_game(self):
        self.player_ships_inp()
        print("         --> You                           Computer")
        self.game_field()
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
    def __init__(self, x, y, *args):
        self.x = x
        self.y = y
        if args:
            self.x1, self.y1 = map(int, args)
        else:
            self.x1 = x
            self.y1 = y

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
