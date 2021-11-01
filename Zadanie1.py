class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        for r in self.my_list:
            for i in r:
                print(f"{i:4}", end="")
            print()
        return ''

    def __add__(self, other):
        for i in range(len(self.my_list)):
            for i_2 in range(len(other.my_list[i])):
                self.my_list[i][i_2] = self.my_list[i][i_2] + other.my_list[i][i_2]
        return Matrix.__str__(self)


m = Matrix([[41, 24, 54], [57, 34, 2], [56, 70, 4]])
new_m = Matrix([[45, 79, 92], [49, 46, 64], [38, 28, 1]])
print(m.__add__(new_m))