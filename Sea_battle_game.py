import os
import random


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
    def IS_SHIP_NOT_WHERE(ship, x, y, *args):
        if args:
            x1, y1 = map(int, args)
        else:
            x1 = x
            y1 = y
        for i in range(ship.get_x - 1, ship.get_x1 + 2):
            for k in range(ship.get_y - 1, ship.get_y1 + 2):
                if i in range(6) and k in range(6) and ((i == x and k == y) or (i == x1 and k == y1)):
                    return False
        return True

    def computer_ship_inp(self):
        count = 0
        count_while = 0
        while True:
            x, y, x1, y1 = random.randint(0, 5), random.randint(0, 5), random.randint(0, 5), random.randint(0, 5)
            if count == 0:
                if ((abs(x - x1) == 2 and y == y1) or (abs(y - y1) == 2 and x == x1)) and x <= x1 and y <= y1:
                    self.computer_ships.append(Ship(x, y, x1, y1))
                    count += 1
            elif 0 < count < 3:
                if ((abs(x - x1) == 1 and y == y1) or (abs(y - y1) == 1 and x == x1)) and x <= x1 and y <= y1 \
                        and all([self.IS_SHIP_NOT_WHERE(i, x, y, x1, y1) for i in self.computer_ships]):
                    self.computer_ships.append(Ship(x, y, x1, y1))
                    count += 1
            elif 2 < count < 7:
                if all([self.IS_SHIP_NOT_WHERE(i, x, y) for i in self.computer_ships]):
                    self.computer_ships.append(Ship(x, y))
                    count += 1
            elif count == 7:
                break
            count_while += 1
            if count_while >= 1000:
                self.computer_ships.clear()
                return self.computer_ship_inp()

    def player_ships_inp(self):
        count = 0
        while True:
            self.ship_place()
            self.game_field()
            if count == 0:
                x, y, x1, y1 = map(int, input("Введите координаты для корабля на 3 клетки (x,y)(x,y): ").split())
                if ((abs(x - x1) == 2 and y == y1) or (abs(y - y1) == 2 and x == x1)) and x <= x1 and y <= y1:
                    self.players_ships.append(Ship(x - 1, y - 1, x1 - 1, y1 - 1))
                    count += 1
                    os.system("cls")
                else:
                    os.system("cls")
                    print("Введены координаты больше или меньше 3 клеток или рядом с другим короблем")
            elif 0 < count < 3:
                x, y, x1, y1 = map(int, input("Введите координаты для корабля на 2 клетки (x,y)(x,y): ").split())
                if ((abs(x - x1) == 1 and y == y1) or (abs(y - y1) == 1 and x == x1)) and x <= x1 and y <= y1 \
                        and all([self.IS_SHIP_NOT_WHERE(i, x - 1, y - 1, x1 - 1, y1 - 1) for i in self.players_ships]):
                    self.players_ships.append(Ship(x - 1, y - 1, x1 - 1, y1 - 1))
                    count += 1
                    os.system("cls")
                else:
                    os.system("cls")
                    print("Введены координаты больше или меньше 2 клеток или рядом с другим короблем")
            elif 2 < count < 7:
                x, y = map(int, input("Введите координаты для корабля на 1 клетку (x,y): ").split())
                if all([self.IS_SHIP_NOT_WHERE(i, x - 1, y - 1) for i in self.players_ships]):
                    self.players_ships.append(Ship(x - 1, y - 1))
                    count += 1
                    os.system("cls")
                else:
                    os.system("cls")
                    print("Введены координаты рядом с другим короблем")
            elif count == 7:
                break

    def ship_place(self):
        for ship in self.players_ships:
            if ship.get_x == ship.get_x1:
                for i in range(ship.get_y, ship.get_y1 + 1):
                    self.player_field[ship.get_x][i] = "| S"
            elif ship.get_y == ship.get_y1:
                for i in range(ship.get_x, ship.get_x1 + 1):
                    self.player_field[i][ship.get_y] = "| S"

    def game_field(self):
        print("         --> You                           Computer")
        print("  | 1 | 2 | 3 | 4 | 5 | 6        | 1 | 2 | 3 | 4 | 5 | 6 ")
        for i, j in enumerate(self.player_field):
            print(i + 1, *j, "   ", i + 1, *self.computer_field[i])

    @staticmethod
    def IS_HIT(ships, x, y):
        for ship in ships:
            for n in range(ship.get_x, ship.get_x1 + 1):
                for k in range(ship.get_y, ship.get_y1 + 1):
                    if n == x and k == y:
                        return True
        return False

    @staticmethod
    def ship_terminate(ship, field):
        count_hit = 0
        count = 0
        for n in range(ship.get_x, ship.get_x1 + 1):
            for k in range(ship.get_y, ship.get_y1 + 1):
                if field[n][k] == "| X":
                    count_hit += 1
                count += 1
        if count_hit == count:
            for n in range(ship.get_x - 1, ship.get_x1 + 2):
                for k in range(ship.get_y - 1, ship.get_y1 + 2):
                    if n in range(6) and k in range(6):
                        if not field[n][k] == "| X":
                            field[n][k] = "| T"

    def shoot(self, ships, field, x, y):
        if self.IS_HIT(ships, x, y):
            field[x][y] = "| X"
            return True
        else:
            field[x][y] = "| T"
            return False

    def is_shoot(self, name, x, y):
        if name == "player" and (not self.computer_field[x][y] == "| X" or not self.computer_field[x][y] == "| T"):
            if self.shoot(self.computer_ships, self.computer_field, x, y):
                return True
        if name == "computer" and (not self.player_field[x][y] == "| X" or not self.player_field[x][y] == "| T"):
            if self.shoot(self.players_ships, self.player_field, x, y):
                return True
        return False

    def is_win(self, ships, field):
        count = 0
        count_hit = 0
        for ship in ships:
            for n in range(ship.get_x, ship.get_x1 + 1):
                for k in range(ship.get_y, ship.get_y1 + 1):
                    if field[n][k] == "| X":
                        count_hit += 1
                    count += 1
        if count == count_hit:
            return True
        return False

    def start_game(self):
        self.computer_ship_inp()
        self.player_ships_inp()
        count = 0
        while True:
            os.system("cls")
            for ship in self.computer_ships:
                self.ship_terminate(ship, self.computer_field)
            for ship in self.players_ships:
                self.ship_terminate(ship, self.player_field)
            self.game_field()
            if count % 2 == 0:
                shoot_x, shoot_y = map(int, input("Введите координаты выстрела (x,y): ").split())
                if not self.is_shoot("player", shoot_x - 1, shoot_y - 1):
                    count += 1
            else:
                shoot_x, shoot_y = random.randint(0, 5), random.randint(0, 5)
                if not self.is_shoot("computer", shoot_x, shoot_y):
                    count += 1
            if self.is_win(self.players_ships, self.player_field):
                print("Компьютер победил!")
                break
            if self.is_win(self.computer_ships, self.computer_field):
                print("Игрок победил!")
                break


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
