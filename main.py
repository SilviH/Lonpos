#TO DO:
# Stop the cycle when filled

import copy
import shape

print('Lonpos!')
# riddle 005
initial_playfiel5 = (['H', 'H', 'B', 'B', 'B', 'C', 'C', 'C', 'C', 'K', 'K'],
                     ['D', 'H', 'H', 'B', 'B', 'C', 'A', 'A', 'A', 'K', 'K'],
                     ['D', 'D', 'H', 'E', 'E', 'L', 'I', 'I', 'A', '.', '.'],
                     ['D', 'E', 'E', 'E', 'L', 'L', 'L', 'I', '.', '.', '.'],
                     ['D', 'J', 'J', 'J', 'J', 'L', 'I', 'I', '.', '.', '.']
                     )

# riddle 006
initial_playfield = (['J', 'J', 'J', 'J', 'H', 'H', 'D', 'D', 'D', 'D', 'F'],
                     ['C', 'C', 'I', 'I', 'L', 'H', 'H', 'D', 'E', 'F', 'F'],
                     ['C', 'G', 'I', 'L', 'L', 'L', 'H', 'E', 'E', '.', '.'],
                     ['C', 'G', 'I', 'I', 'L', 'B', 'B', 'E', '.', '.', '.'],
                     ['C', 'G', 'G', 'G', 'B', 'B', 'B', 'E', '.', '.', '.']
                     )

# riddle 007 needs vertical mirror
initial_playfield = (['E', 'E', 'G', 'G', 'G', 'D', 'D', 'D', 'D', 'K', 'K'],
			 ['J', 'E', 'E', 'E', 'G', 'C', 'D', 'H', 'H', 'K', 'K'],
			 ['J', 'I', 'I', 'L', 'G', 'C', 'H', 'H', '.', '.', '.'],
			 ['J', 'I', 'L', 'L', 'L', 'C', 'H', 'F', '.', '.', '.'],
			 ['J', 'I', 'I', 'L', 'C', 'C', 'F', 'F', '.', '.', '.']
			 )

## riddle 008
#initial_playfield = (['B', 'B', 'D', 'D', 'D', 'D', 'H', 'H', 'A', 'A', 'A'],
#			 ['B', 'B', 'B', 'F', 'D', 'H', 'H', 'E', 'E', 'E', 'A'],
#			 ['I', 'I', 'L', 'F', 'F', 'H', 'E', 'E', '.', '.', '.'],
#			 ['I', 'L', 'L', 'L', 'C', 'C', 'C', 'C', '.', '.', '.'],
#			 ['I', 'I', 'L', 'J', 'J', 'J', 'J', 'C', '.', '.', '.']
#			 )

all_shapes = {'A': 0x44c0, 'B': 0x4cc0, 'C': 0x444c, 'D': 0x44c4,
              'E': 0x44c8, 'F': 0x4c00, 'G': 0x22e0, 'H': 0x26c0,
              'I': 0xae00, 'J': 0x8888, 'K': 0xcc00, 'L': 0x4e40,
              }
shapes = {}


def print_board(playfield):
    for row in playfield:
        for current_letter in row:
            print(' ' + current_letter, end='')

        print()
    print()


def available_letters(playfield):  # returns list of available shapes (letters), alphabetically sorted
    used_shapes = set()
    for row in playfield:
        for current_letter in row:
            used_shapes.add(current_letter)

    return sorted(list(shapes.keys() - used_shapes))


def display_available_shapes(playfield):
    for current_letter in available_letters(playfield):
        shapes[current_letter].display()


def board_area_to_number(playfield, row_start, letter_start):
    accumulator = ''
    for row_index in range(row_start, row_start + 4):
        for letter_index in range(letter_start, letter_start + 4):

            to_add = '1'
            if len(playfield) > row_index >= 0 and \
                    len(playfield[0]) > letter_index >= 0 and \
                    playfield[row_index][letter_index] == '.':
                to_add = '0'
            accumulator += to_add

    return int(accumulator, base=2)


def first_fitting_position(playfield, current_shape):  # returns tuple of coordinates
    for letter_index in range(-3, 11):
        for row_index in range(-3, 5):
            window = board_area_to_number(playfield, row_index, letter_index)
            if current_shape.get_number() & window == 0:
                return row_index, letter_index

    return ()


def insert_shape(playfield, current_shape, x, y):
    retval = copy.deepcopy(playfield)
    this_shape = current_shape.to_binary()
    for col_index in range(0, 4):
        for row_index in range(0, 4):
            offset = col_index + 4 * row_index
            if this_shape[offset] == '1':
                retval[row_index + y][col_index + x] = current_shape.get_name()
    return retval


def recurse_process_shape(playfield, current_shape, remaining_shapes):
    for orientation in ['rot_0', 'mirror_x']:

        current_shape.set_orientation(orientation)
        current_shape.display()
        place = first_fitting_position(playfield, current_shape)

        if len(place) > 0:
            playfield = insert_shape(playfield, current_shape, place[1], place[0])
            if len(remaining_shapes) > 0:
                next_shape = remaining_shapes[0]
                remaining_shapes = remaining_shapes[1:]
                playfield = recurse_process_shape(playfield, next_shape, remaining_shapes)
            break

    print(playfield)
    return playfield


# program starts here

print_board(initial_playfield)

for key, val in all_shapes.items():
    shapes[key] = shape.Shape(key, val)
# create Shape dictionary

my_playfield = initial_playfield
temp = available_letters(initial_playfield)

initial_remaining_shapes = []
for length_index in range(len(temp)):
    initial_remaining_shapes.append(shapes[temp[length_index]])

for letter in range(len(temp)):  # how many available letters
    initial_shape = shapes[temp[letter]]  # take the available letters one by one as the einitial

    initial_remaining_shapes = initial_remaining_shapes[1:]
    recurse_process_shape(my_playfield, initial_shape, initial_remaining_shapes)
    initial_remaining_shapes.append(initial_shape)  # list of remaining shapes (objects)
