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

       
            

    def board_area_to_number(self, row_start, letter_start):
        accumulator = 0
        board_height = len(self.board)
        board_length = len(self.board[0])
        value_to_add = 2**15
        for row_index in range(row_start, row_start + 4):
            for letter_index in range(letter_start, letter_start + 4):


                if not(board_height > row_index >= 0 and \
                        board_length > letter_index >= 0 and \
                        self.board[row_index][letter_index] == '.'):
                    accumulator += value_to_add
                
                value_to_add = value_to_add >> 1
        return accumulator



    def first_fitting_position(self, current_shape):  # returns tuple of coordinates
        for letter_index in range(-3, 11):
            for row_index in range(-3, 5):
                window = self.board_area_to_number(row_index, letter_index)
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
        

