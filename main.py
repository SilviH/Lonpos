print('Lonpos!')

playfield = (['H', 'H', 'B', 'B', 'B', 'C', 'C', 'C', 'C', 'K', 'K'],
			 ['D', 'H', 'H', 'B', 'B', 'C', 'A', 'A', 'A', 'K', 'K'],
			 ['D', 'D', 'H', 'E', 'E', 'L', 'I', 'I', 'A', '.', '.'],
			 ['D', 'E', 'E', 'E', 'L', 'L', 'L', 'I', '.', '.', '.'],
			 ['D', 'J', 'J', 'J', 'J', 'L', 'I', 'I', '.', '.', '.']
			 )

shapes = {'A': 0x44c0, 'B': 0x4cc0, 'C': 0x444c, 'D': 0x44c4,
		  'E': 0x44c8, 'F': 0x4c00, 'G': 0x22e0, 'H': 0x26c0,
		  'I': 0xae00, 'J': 0x8888, 'K': 0xcc00, 'L': 0x4e40,
		  }


def print_board():
	for row in playfield:
		for letter in row:
			print(' ' + letter, end='')

		print()
	print()


def available_shapes(): # returns set of available shapes (letters)
	used_shapes = set()
	for row in playfield:
		for letter in row:
			used_shapes.add(letter)
	return shapes.keys() - used_shapes


def display_shape(letter):
	x = shapes[letter]
	x = (str(bin(x)))[2:]
	x = (16 - len(x)) * '0' + x

	for number in range(16):
		print(x[number], end=' ')
		if (number + 1) % 4 == 0:
			print()
	print()


def display_available_shapes():
	for letter in available_shapes():
		display_shape(letter)



def board_area_to_number(row_start, letter_start): 
	accumulator = ''
	for row_index in range(row_start, row_start + 4):
		for letter_index in range(letter_start, letter_start + 4):  
			
			if row_index < len(playfield) and row_index >= 0 and letter_index < len(playfield[0]) \
			and letter_index >= 0 and playfield[row_index][letter_index] == '.':
			
				to_add = '0'
				
			else:
			
				to_add = '1'
				
			accumulator += to_add	
			
	return int(accumulator, base = 2)


def first_fitting_position(letter):
	for letter_index in range(-3, 11):
		for row_index in range(-3, 5):  
			window = board_area_to_number(row_index, letter_index)
			if shapes[letter] & window == 0:
				return (row_index, letter_index)
			
	return ()


# program starts here
print_board()
display_available_shapes()
check_area = board_area_to_number(-1, -8)

print(first_fitting_position('F'))



