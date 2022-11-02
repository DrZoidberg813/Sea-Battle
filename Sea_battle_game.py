import os
import random


class Game:
    def __init__(self):
        self.players_ships = []
        self.computer_ships = []
        self.player_field = [["| O", "| O", "| O", "| O", "| O", "| O"],
                             ["| O", "| O", "| O", "| O", "| O", "| O"],
                             ["| O", "| O", "| O", "| O", "| O", "| O"],
                             ["| O", "| O", "| O", "| O", "| O", "| O"],
                             ["| O", "| O", "| O", "| O", "| O", "| O"],
                             ["| O", "| O", "| O", "| O", "| O", "| O"]]
        self.computer_field = [["| O", "| O", "| O", "| O", "| O", "| O"],
                               ["| O", "| O", "| O", "| O", "| O", "| O"],
                               ["| O", "| O", "| O", "| O", "| O", "| O"],
                               ["| O", "| O", "| O", "| O", "| O", "| O"],
                               ["| O", "| O", "| O", "| O", "| O", "| O"],
                               ["| O", "| O", "| O", "| O", "| O", "| O"]]

    @staticmethod
    def IS_WIN(ships, field):
        count = 0
        count_hit = 0
        for ship in ships:
            for n in range(ship.get_x, ship.get_x1 + 1):
                for k in range(ship.get_y, ship.get_y1 + 1):
                    if field[n][k] == "| \033[31mX\033[0m":
                        count_hit += 1
                    count += 1
        if count == count_hit:
            return True
        return False

    @staticmethod
    def IS_SHIP_NOT_WHERE(ship, x, y, x1, y1):
        for i in range(ship.get_x - 1, ship.get_x1 + 2):
            for k in range(ship.get_y - 1, ship.get_y1 + 2):
                if (i == x and k == y) or (i == x1 and k == y1):
                    return False
        return True

    @staticmethod
    def IS_HIT(ships, x, y):
        for ship in ships:
            for n in range(ship.get_x, ship.get_x1 + 1):
                for k in range(ship.get_y, ship.get_y1 + 1):
                    if n == x and k == y:
                        return True
        return False

    @staticmethod
    def SHIP_TERMINATE(ship, field):
        count_hit = 0
        count = 0
        for n in range(ship.get_x, ship.get_x1 + 1):
            for k in range(ship.get_y, ship.get_y1 + 1):
                if field[n][k] == "| \033[31mX\033[0m":
                    count_hit += 1
                count += 1
        if count_hit == count:
            for n in range(ship.get_x - 1, ship.get_x1 + 2):
                for k in range(ship.get_y - 1, ship.get_y1 + 2):
                    if n in range(6) and k in range(6) and field[n][k] != "| \033[31mX\033[0m":
                        field[n][k] = "| \033[35mT\033[0m"

    def ship_input(self, ships, x, y, x1, y1, what_ship):
        if all([
            x in range(1, 7), y in range(1, 7),
            ((abs(x - x1) == what_ship and y == y1) or (abs(y - y1) == what_ship and x == x1)), x <= x1 and y <= y1,
            all([self.IS_SHIP_NOT_WHERE(i, x - 1, y - 1, x1 - 1, y1 - 1) for i in ships])
        ]):
            ships.append(Ship(x - 1, y - 1, x1 - 1, y1 - 1))
            return True
        else:
            return False

    def ships_create(self, name):
        x, y, x1, y1, ship = None, None, None, None, None
        count = 0
        count_while = 0
        while True:
            try:
                if count == 0 and name == "player":
                    x, y, x1, y1 = map(int, input("Введите координаты для корабля на 3 клетки,"
                                                  " из начальной координаты x,y через пробел"
                                                  " и конечной координаты x,y через пробел): ").split())
                    ship = 2
                elif count == 0 and name == "computer":
                    x, y, x1, y1 = [random.randint(1, 6) for i in range(4)]
                    ship = 2
                elif 0 < count < 3 and name == "player":
                    x, y, x1, y1 = map(int, input("Введите координаты для корабля на 2 клетки,"
                                                  " из начальной координаты x,y через пробел"
                                                  " и конечной координаты x,y через пробел): ").split())
                    ship = 1
                elif 0 < count < 3 and name == "computer":
                    x, y, x1, y1 = [random.randint(1, 6) for i in range(4)]
                    ship = 1
                elif 2 < count < 7 and name == "player":
                    x, y = map(int, input("Введите координаты для корабля на 1 клетку,"
                                          " в виде x,y через пробел: ").split())
                    x1, y1 = x, y
                    ship = 0
                elif 2 < count < 7 and name == "computer":
                    x, y = [random.randint(1, 6) for i in range(2)]
                    x1, y1 = x, y
                    ship = 0
                if name == "computer":
                    if self.ship_input(self.computer_ships, x, y, x1, y1, ship):
                        count += 1
                if name == "player":
                    if self.ship_input(self.players_ships, x, y, x1, y1, ship):
                        count += 1
                        os.system("cls")
                        self.ship_place()
                        self.game_field()
                    else:
                        print("Введены неверные координаты.")
                        if input(
                                "Если хотите сбросить набор кораблей введите restart, если нет нажмите Enter: "
                        ) == "restart":
                            self.players_ships.clear()
                            self.player_field = [["| O", "| O", "| O", "| O", "| O", "| O"],
                                                 ["| O", "| O", "| O", "| O", "| O", "| O"],
                                                 ["| O", "| O", "| O", "| O", "| O", "| O"],
                                                 ["| O", "| O", "| O", "| O", "| O", "| O"],
                                                 ["| O", "| O", "| O", "| O", "| O", "| O"],
                                                 ["| O", "| O", "| O", "| O", "| O", "| O"]]
                            os.system("cls")
                            self.game_field()
                            return self.ships_create("player")
            except ValueError:
                print("Введены неверные координаты.")
            finally:
                if count == 7:
                    break
                count_while += 1
                if count_while >= 2000:
                    self.computer_ships.clear()
                    return self.ships_create("computer")

    def ship_place(self):
        for ship in self.players_ships:
            if ship.get_x == ship.get_x1:
                for i in range(ship.get_y, ship.get_y1 + 1):
                    self.player_field[ship.get_x][i] = "|\033[34m ■\033[0m"
            elif ship.get_y == ship.get_y1:
                for i in range(ship.get_x, ship.get_x1 + 1):
                    self.player_field[i][ship.get_y] = "|\033[34m ■\033[0m"

    def game_field(self):
        print("             You                             Computer")
        print("  | 1 | 2 | 3 | 4 | 5 | 6 ", "       | 1 | 2 | 3 | 4 | 5 | 6 ")
        for i, j in enumerate(self.player_field):
            print(i + 1, *j, "     ", i + 1, *self.computer_field[i])

    def is_shoot(self, ships, field, x, y):
        try:
            if not field[x][y] in ["| \033[31mX\033[0m", "| \033[35mT\033[0m"]:
                if self.IS_HIT(ships, x, y):
                    field[x][y] = "| \033[31mX\033[0m"
                    return True
                else:
                    field[x][y] = "| \033[35mT\033[0m"
                    return False
            else:
                return None
        except IndexError:
            print("Введены неверные координаты.")

    def start_game(self):
        os.system("cls")
        self.ships_create("computer")
        self.game_field()
        self.ships_create("player")
        count = 0
        while True:
            try:
                if count % 2 == 0:
                    shoot_x, shoot_y = map(int, input("Введите координаты выстрела x,y через пробел: ").split())
                    shoot = self.is_shoot(self.computer_ships, self.computer_field, shoot_x - 1, shoot_y - 1)
                    if shoot is not None and not shoot:
                        count += 1
                    os.system("cls")
                    if shoot is None:
                        print("В эту точку уже стреляли.")
                else:
                    shoot_x, shoot_y = random.randint(0, 5), random.randint(0, 5)
                    shoot = self.is_shoot(self.players_ships, self.player_field, shoot_x, shoot_y)
                    if shoot is not None and not shoot:
                        count += 1
                    os.system("cls")
            except ValueError or IndexError:
                os.system("cls")
                print("Введены неверные координаты.")
            finally:
                for ship in self.computer_ships:
                    self.SHIP_TERMINATE(ship, self.computer_field)

                for ship in self.players_ships:
                    self.SHIP_TERMINATE(ship, self.player_field)

                self.game_field()

                if self.IS_WIN(self.players_ships, self.player_field):
                    print("Компьютер победил!")
                    break

                if self.IS_WIN(self.computer_ships, self.computer_field):
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
    if input("Начать игру (y/n)? ") == "y":
        test = Game()
        test.start_game()


if __name__ == '__main__':
    main()
