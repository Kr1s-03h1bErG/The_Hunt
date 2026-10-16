class Grid:
    def __init__(self, width):
        self.width = width
        self.height = width

    def print_grid(self):
        for i in range(self.width):
            for x in range(self.height):
                print(".", end = " ")
            print("")



    def increase_grid_size_by(self, x):
        self.width += x
        self.height += x 

grid1 = Grid(5)
grid1.increase_grid_size_by(1)
grid1.print_grid()