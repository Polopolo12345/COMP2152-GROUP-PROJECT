import random

class TreasureMap:
    def __init__(self, rows=5, cols=5):
        self.rows = rows
        self.cols = cols
        self.map = [[" " for _ in range(cols)] for _ in range(rows)]
        self.player_pos = (2, 2)  # 시작 위치
        self.score = 0
        self.health = 10

        # 보물 배치
        self.treasure_types = ["healing", "trap", "bonus"]
        self.treasures = {}
        self._place_treasures()

    def _place_treasures(self):
        for _ in range(4):
            r, c = random.randint(0, self.rows - 1), random.randint(0, self.cols - 1)
            if (r, c) != self.player_pos and (r, c) not in self.treasures:
                self.map[r][c] = "X"
                self.treasures[(r, c)] = random.choice(self.treasure_types)

    def move_player(self, direction):
        r, c = self.player_pos
        if direction == "up" and r > 0:
            r -= 1
        elif direction == "down" and r < self.rows - 1:
            r += 1
        elif direction == "left" and c > 0:
            c -= 1
        elif direction == "right" and c < self.cols - 1:
            c += 1
        else:
            print("Invalid move.")
            return

        self.player_pos = (r, c)
        print(f"You moved to ({r}, {c})")

        # 중첩 조건문: 해당 위치가 보물인지 확인
        if (r, c) in self.treasures:
            item = self.treasures[(r, c)]
            if item == "healing":
                self.health += 5
                print("You found a healing item! +5 health.")
            elif item == "trap":
                self.health -= 3
                print("It's a trap! -3 health.")
            elif item == "bonus":
                self.score += 10
                print("Bonus points! +10 score.")
            del self.treasures[(r, c)]
            self.map[r][c] = " "

        print(f"Health: {self.health}, Score: {self.score}")

    def show_map(self):
        for i in range(self.rows):
            row = ""
            for j in range(self.cols):
                if (i, j) == self.player_pos:
                    row += "P "
                else:
                    row += self.map[i][j] + " "
            print(row)
