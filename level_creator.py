# from inputimeout import inputimeout, TimeoutOccurred
from rich import print
# from rich.console import Console
# console = Console()
import time
import os

class Level:
    def __init__(self, name, rows):
        self.name = name
        self.grid = []
        self.editor_position = [rows // 2 + 1, rows // 2 + 1]
        print(self.editor_position)
        border_row = []
        data = [] 
        for i in range(rows):
            data.append("x") # auto fill data with set length determined by rows 
        for i in range(rows):
            border_row.append("|") # auto fill data with set length determined by rows
        data.insert(0 , "|")
        data.append("|")
        border_row.append("|")
        border_row.insert(0 , "|")
        self.grid.append(border_row)
        for i in range(rows): # auto fill data with set hight determined by rows 
            self.grid.append(data)
        self.grid.append(border_row)

        self.border_color = "grey3 on grey0"
        self.base_color = "grey100 on grey23"
        self.entity_color = "red on grey23"
        self.edtitor_color = "green1 on grey23"

    def __draw_level__(self):
        text = ""
        for y , row in enumerate(self.grid):
            for x , row_data in enumerate(row):
                if self.editor_position == [x , y]:
                    text += f"[{self.edtitor_color}]i [/{self.edtitor_color}]"
                elif row_data == "|":
                    text += f"[{self.border_color}]. [/{self.border_color}]"
                elif row_data == "H":
                    text += f"[{self.entity_color}]H [/{self.entity_color}]"
                else:
                    text += f"[{self.base_color}]{row_data} [/{self.base_color}]"
            text += "\n"
        print(text)

    def __move_editor__(self, movement):
        if movement == "D":
            self.editor_position[0] += 1
        elif movement == "A":
            self.editor_position[0] -= 1
        elif movement == "W":
            self.editor_position[1] -= 1
        elif movement == "S":
            self.editor_position[1] += 1
        else:
            self.__edit_tile__(movement)

    def __edit_tile__(self, movement):
        if movement in ["n", "s", "e", "w", "H", "X", "c"]:
            print(self.editor_position[0])
            self.grid[self.editor_position[0], self.editor_position[1]] = movement
        elif movement == "q":
            self.__draw_level__()
            print("ending level editor")
            os.exit(0)
        else:
            print('please use Arrow Keys or "n", "s", "e", "w", "H", "X", "c" ')

level_size = input("Enter the size of the Level")      
level_1 = Level("Debug", int(level_size))

while True:
    level_1.__draw_level__()
    player_input = input("")
    level_1.__move_editor__(player_input)


level_1.__draw_level__()
print("done")