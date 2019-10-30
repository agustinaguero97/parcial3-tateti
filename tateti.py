class TaTeTi():

    def __init__(self, board = None):

        self.board = board
        self.set_up()

    def set_up(self):
        if self.board == None:
            self.board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    def full(self):
        if self.board.count(' ') > 0:
            return False
        else:
            return True
    
    def win(self):
        matrix_row = self.set_matrix_row()
        matrix_column = self.set_matrix_column()
        vector_diagonal_1 = self.set_vector_diagonal_1()
        vector_diagonal_2 = self.set_vector_diagonal_2()

        for row in range(3):
            x_row = matrix_row[row].count("x")
            o_row = matrix_row[row].count("o")
            x_column = matrix_column[row].count("x")
            o_column = matrix_column[row].count("o")
            if  x_row == 3 or o_row == 3 or x_column == 3 or o_column == 3:
                return True
        
        v1_x = vector_diagonal_1.count("x")
        v1_o = vector_diagonal_1.count("o")
        v2_x = vector_diagonal_2.count("x")
        v2_o = vector_diagonal_2.count("o")
        if v1_x == 3 or v1_o == 3 or v2_x == 3 or v2_o == 3:
            return True
        
        return False

    def set_matrix_row(self):
        matrix = []
        count = 0
        for row in range(3):
            matrix.append([])
            for column in range(3):
                matrix[row].append(self.board[column + count])
            count += 3
        return matrix
    
    def set_matrix_column(self):
        matrix = []
        for row in range(3):
            count = 0
            matrix.append([])
            count = count + row
            for column in range(3):
                matrix[row].append(self.board[column + count])
                count += 2
        return matrix

    def set_vector_diagonal_1(self):
        vector = []
        for item in range(0, 9, 4):
            vector.append(self.board[item])
        return vector
    
    def set_vector_diagonal_2(self):
        vector = []
        for item in range(2, 7, 2):
            vector.append(self.board[item])
        return vector
    

    def validate(self, position):
        if self.board[position - 1] == " ":
            return True
        else:
            return False

    def assign(self, position, piece):
        if self.board[position -1] != " ":
            raise Exception
        else:
            self.board[position -1] = piece
        

    def draw_board(self):
        display = ""
        slot = 0
        for row in range(3):
            display  = display + "\n"
            for num in range(3):
                slot += 1
                if self.board[num + (row * 3)] == ' ':
                    display = display + f" {slot} "
                else:
                    display = display + f" {self.board[num + (row * 3)]} "
                if num < 2:
                    display = display + "|"
            if row < 2:
                display = display + "\n---+---+---"
        display = display + "\n"
        return display