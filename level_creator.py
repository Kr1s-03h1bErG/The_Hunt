from inputimeout import inputimeout, TimeoutOccurred
import time

class Level:
    def __init__(self, name, rows):
        self.name = name
        self.grid = []
        border_row = []
        data = [] 
        for i in range(rows):
            data.append("i") # auto fill data with set length determined by rows 
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
        
        

level_size = input("Enter the size of the Level")      
level_1 = Level("dummy name", int(level_size)) 

for row in level_1.grid:
    for row_data in row:
        print(row_data, end=" ")
    print("")

