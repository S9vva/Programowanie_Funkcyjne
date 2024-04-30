class Zadanie_Nine:
    def __init__(self):
        pass
    
    def create_3x3_matrix(self):
        return [[(i*3) + j + 1 for j in range(3)] for i in range(3)]
    
    # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
