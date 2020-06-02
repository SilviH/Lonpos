# list of 5 lists
import copy
class Playfield:
    init_board = []
    board = []
    
    def __init__(self, riddle):
        self.init_board = self.board = riddle
        
    def display(self):
        for row in self.board:
            for current_letter in row:
                print(' ' + current_letter, end='')

            print()
        print()


    def available_letters(self, shapes_keys):  # returns list of available shapes (letters), alphabetically sorted
        used_shapes = set()
        for row in self.board:
            for current_letter in row:
                used_shapes.add(current_letter)

        return sorted(list(shapes_keys - used_shapes))
 
       
    def display_available_shapes(self, shapes_dict):
        for current_letter in self.available_letters(shapes_dict.keys()):
            shapes_dict[current_letter].display()
            

    def initial_remaining_shapes(self, shapes_dict, available_shapes_keys):
        initial_shapes = []
        for length_index in range(len(available_shapes_keys)):
            initial_shapes.append(shapes_dict[available_shapes_keys[length_index]])
        return initial_shapes
  
    def initialize_number_board(self, num_board):
        for row in range(5):
            for character in range(11):
                if self.board[row][character] == '.':
                    num_board[row+3][character+3] = '0'
        return num_board
       
    def board_area_to_number(self, row_start, letter_start, num_board):
        accumulator = ''
        for row_index in range(row_start+3, row_start + 7):
            accumulator += num_board[row_index][letter_start + 3] + num_board[row_index][letter_start + 4]\
            + num_board[row_index][letter_start + 5] + num_board[row_index][letter_start + 6]              
        return int(accumulator, base=2)   
    

    def first_fitting_position(self, current_shape, num_playfield):  # returns tuple of coordinates
        number_board = self.initialize_number_board(num_playfield)
        for letter_index in range(-3, 11):
            for row_index in range(-3, 5):
                window = self.board_area_to_number(row_index, letter_index, number_board)
                if current_shape.get_number() & window == 0:
                    return row_index, letter_index
        return ()


    def insert_shape(self, current_shape, x, y):
        retval = copy.deepcopy(self.board)
        this_shape = current_shape.to_binary()
        for col_index in range(0, 4):
            for row_index in range(0, 4):
                offset = col_index + 4 * row_index
                if this_shape[offset] == '1':
                    retval[row_index + y][col_index + x] = current_shape.get_name()
        return Playfield(retval)


    def is_solved(self):
        for row in self.board:
            for current_letter in row:
                if current_letter == '.':
                    return False
        return True
        

