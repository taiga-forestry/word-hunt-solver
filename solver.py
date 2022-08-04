import trie

class Solver:
    ''' Class representing the Word Hunt Solver '''

    def __init__(self, file_path):
        ''' Constructor for the Solver class '''
        
        self.board = [[0] * 4 for i in range(0, 4)]
        self.dictionary = self.fill_trie(file_path)
        self.solutions = {} # word length -> word -> one possible path
        self.visited = []


    def fill_board(self, letters: str):
        ''' 
        Fills the Word Hunt game board
        
        Parameters:
        letters (str) -- the letters of the Word Hunt Board

        Exceptions:
        (ValueError) -- raised if non-alphabetical characters are present
        '''
        
        letters = letters.upper()
        
        if True in [ord(letter) < 65 or ord(letter) > 90 for letter in letters]:
            raise ValueError("only alphabetical characters allowed!")
    
        for i in range(0, 4):
            for j in range(0, 4):
                self.board[i][j] = letters[4 * i + j]


    def fill_trie(self, file_path: str) -> "trie":
        ''' 
        Fills the trie, which functions as the dictionary 
        
        Parameters:
        file_path (str) -- path to the dictionary file

        Returns:
        (trie) -- returns the trie filled with all words in the dictionary
        '''
        
        with open(file_path) as f:
            lines = f.readlines()
            dictionary = trie.Trie()
            
            for line in lines:
                dictionary.add(line.strip())

            return dictionary


    def solve_board(self):
        ''' Solves the given Word Hunt board '''

        for i in range(0, 4):
            for j in range(0, 4):
                self.solve_from(i, j, "")


    def solve_from(self, i: int, j: int, curr_word: str):
        ''' 
        Solves the given Word Hunt board starting from a given position

        Parameters:
        i (int) -- vertical position on the board
        j (int) -- horizontal position on the board
        curr_word (str) -- word created so far
        '''

        # position is off the board, position has been visited already, or trie does not contain this subword
        if i < 0 or j < 0 or i > 3 or j > 3 or self.board[i][j] == "*" or not self.dictionary.contains(curr_word, True):
            return
        else:
            curr_letter = self.board[i][j]
            new_word = curr_word + curr_letter
            self.board[i][j] = "*"
            self.visited.append((i, j))

            if len(new_word) >= 3 and self.dictionary.contains(new_word, False):
                self.solutions.setdefault(len(new_word), {})[new_word] = [4 * pos[0] + pos[1] for pos in self.visited]

            # solve the board in every direction 
            self.solve_from(i - 1, j - 1, new_word)
            self.solve_from(i - 1, j, new_word)
            self.solve_from(i - 1, j + 1, new_word)
            self.solve_from(i, j - 1, new_word)
            self.solve_from(i, j + 1, new_word)
            self.solve_from(i + 1, j - 1, new_word)
            self.solve_from(i + 1, j, new_word)
            self.solve_from(i + 1, j + 1, new_word)

            self.board[i][j] = curr_letter
            self.visited.pop()


    def display_solutions(self):
        ''' Displays all solutions to the Word Hunt board '''

        for i in range(15, -1, -1):
            if i in self.solutions and len(self.solutions[i]) > 0 and i >= 4:
                for key in self.solutions[i]:
                    print(key + ":", self.solutions[i][key])

        self.solutions = [{} for i in range(0, 17)] # reset solutions


###############################################################
########################### REPL ##############################
###############################################################

if __name__ == "__main__":
    solver = Solver("ENGLISH_DICT.txt")
    letters = input("Word Hunt Solver> input the game board as one string, no spaces: ").upper()

    while letters != "QUIT":
        try:
            solver.fill_board(letters)
            solver.solve_board()
            solver.display_solutions()
        except:
            print("invalid input, try again!")
        
        letters = input("Word Hunt Solver> input the game board as one string, no spaces: ").upper()
