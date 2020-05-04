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


def first_fitting_position(playfield, shape): # returns tuple of coordinates	
	for letter_index in range(-3, 11):
		for row_index in range(-3, 5):  
			window = board_area_to_number(playfield,row_index, letter_index)
			if shape.get_number() & window == 0:
				return (row_index, letter_index)
			
	return ()

	
def insert_shape(playfield, shape, x, y):
	retval = copy.deepcopy(playfield)
	this_shape = shape.to_binary()
	for col_index in range(0, 4):
		for row_index in range(0, 4):  
			offset = col_index + 4 * row_index
			if this_shape[offset] == '1':
				retval[row_index + y][col_index + x] = shape.get_name()
	return retval
		
#def recurse_process_shape(my_playfield, shape, remaining_shapes):
#	
#	for orientation in [0,'mirror_x']:
#		shape.set_orientation(orientation)
#		place = first_fitting_position(my_playfield, shape)
#		
#		if len(place) > 0:
#			my_playfield = insert_shape(my_playfield, shape, place[1], place[0])
#			next_shape = remaining_shapes[0]
#			remaining_shapes = remaining_shapes[1:]
#			recurse_process_shape(my_playfield, next_shape, remaining_shapes)
#			break

def recurse_process_shape(my_playfield, shape, remaining_shapes):
	
	for orientation in [0,'mirror_x']:
		
		shape.set_orientation(orientation)
		shape.display()
		place = first_fitting_position(my_playfield, shape)
		
		if len(place) > 0:
			my_playfield = insert_shape(my_playfield, shape, place[1], place[0])
			if len(remaining_shapes) > 0:
				next_shape = remaining_shapes[0]
				remaining_shapes = remaining_shapes[1:]
				my_playfield = recurse_process_shape(my_playfield, next_shape, remaining_shapes)
			break
			
	print(my_playfield)
	return my_playfield
	
	
# program starts here

print_board(initial_playfield)

for key,val in all_shapes.items():
	shapes[key]=shape.Shape(key, val)
	# create Shape dictionary
	
print('Available shapes:')
display_available_shapes(initial_playfield)

my_playfield = initial_playfield
temp = available_shapes(initial_playfield)
temp.reverse()


#available_shapes_lenght = len(temp)
#for letter_index in range(available_shapes_lenght): # how many available letters
#	initial_shape = shapes[temp[letter_index]] # take the available letters one by one as the einitial
#	 
#	for shape_index in range(available_shapes_lenght - 1): # number of remaining letters in the list as range 
#		initial_remaining = []
#		initial_remaining.append(shapes[temp[shape_index + 1]]) # list of remaining shapes (objects)
#		
#	available_shapes_lenght -= 1	

initial_shape = shapes[temp[0]]	

initial_remaining = [shapes[temp[1]]]

recurse_process_shape(my_playfield, initial_shape, initial_remaining)
