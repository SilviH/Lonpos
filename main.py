import copy
import shape
print('Lonpos!')
# riddle 005
initial_playfield = (['H', 'H', 'B', 'B', 'B', 'C', 'C', 'C', 'C', 'K', 'K'],
			 ['D', 'H', 'H', 'B', 'B', 'C', 'A', 'A', 'A', 'K', 'K'],
			 ['D', 'D', 'H', 'E', 'E', 'L', 'I', 'I', 'A', '.', '.'],
			 ['D', 'E', 'E', 'E', 'L', 'L', 'L', 'I', '.', '.', '.'],
			 ['D', 'J', 'J', 'J', 'J', 'L', 'I', 'I', '.', '.', '.']
			 )

# riddle 005
initial_playfield = (['J', 'J', 'J', 'J', 'H', 'H', 'D', 'D', 'D', 'D', 'F'],
			 ['C', 'C', 'I', 'I', 'L', 'H', 'H', 'D', 'E', 'F', 'F'],
			 ['C', 'G', 'I', 'L', 'L', 'L', 'H', 'E', 'E', '.', '.'],
			 ['C', 'G', 'I', 'I', 'L', 'B', 'B', 'E', '.', '.', '.'],
			 ['C', 'G', 'G', 'G', 'B', 'B', 'B', 'E', '.', '.', '.']
			 )

all_shapes = {'A': 0x44c0, 'B': 0x4cc0, 'C': 0x444c, 'D': 0x44c4,
		  'E': 0x44c8, 'F': 0x4c00, 'G': 0x22e0, 'H': 0x26c0,
		  'I': 0xae00, 'J': 0x8888, 'K': 0xcc00, 'L': 0x4e40,
		  }
shapes = {}

def print_board(playfield):
	for row in playfield:
		for letter in row:
			print(' ' + letter, end='')

		print()
	print()


def available_shapes(playfield): # returns list of available shapes (letters), alphabetically sorted
	used_shapes = set()
	for row in playfield:
		for letter in row:
			used_shapes.add(letter)
			
	return sorted(list(shapes.keys() - used_shapes))
	

def display_available_shapes(playfield):
	for letter in available_shapes(playfield):
		shapes[letter].display()


def board_area_to_number(playfield, row_start, letter_start): 
	accumulator = ''
	for row_index in range(row_start, row_start + 4):
		for letter_index in range(letter_start, letter_start + 4):  
			
			to_add = '1'
			if row_index < len(playfield) and row_index >= 0 and letter_index < len(playfield[0]) \
			and letter_index >= 0 and playfield[row_index][letter_index] == '.':
				to_add = '0'
			accumulator += to_add	
			
	return int(accumulator, base = 2)


def first_fitting_position(playfield, letter): # returns tuple of coordinates	
	for letter_index in range(-3, 11):
		for row_index in range(-3, 5):  
			window = board_area_to_number(playfield,row_index, letter_index)
			if shapes[letter].get_number() & window == 0:
				return (row_index, letter_index)
			
	return ()


#def insert_shape(playfield, letter, x, y):
#	retval = copy.deepcopy(playfield)
#	this_shape = shape_to_binary(letter)
#	for col_index in range(0, 4):
#		for row_index in range(0, 4):  
#			offset = col_index + 4 * row_index
#			if this_shape[offset] == '1':
#				retval[row_index + y][col_index + x] = letter
#	return retval
	
def insert_shape(playfield, letter, x, y):
	retval = copy.deepcopy(playfield)
	this_shape = shapes[letter].to_binary()
	for col_index in range(0, 4):
		for row_index in range(0, 4):  
			offset = col_index + 4 * row_index
			if this_shape[offset] == '1':
				retval[row_index + y][col_index + x] = letter
	return retval
		


# program starts here


for key,val in all_shapes.items():
	shapes[key]=shape.Shape(key, val)

print_board(initial_playfield)
print('Available shapes:')
display_available_shapes(initial_playfield)
check_area = board_area_to_number(initial_playfield, -1, -8)

my_playfield = initial_playfield
for shape in available_shapes(initial_playfield):
	place = first_fitting_position(my_playfield,shape)
	print(place, shape)
	if len(place)>0:
		my_playfield = insert_shape(my_playfield,shape,place[1], place[0])

print(my_playfield)

my_shape =shapes['A']
my_shape.mirror_x()
my_shape.display()

