class Shape:
	letter_name = ''
	rotation = 0
	mirror_x = False
	mirror_y = False
	representation = 0
	
	def __init__(self, name, number):
		self.letter_name = name
		self.representation = number
	
	def get_number(self):
		return self.representation
	
	def to_binary(self): # returns string
		retval = (str(bin(self.representation)))[2:]
		retval = (16 - len(retval)) * '0' + retval
		return retval
		
	def display(self):
		x = self.to_binary()
		for number in range(16):
			print(x[number], end=' ')
			if (number + 1) % 4 == 0:
				print()
		print()

	def mirror_x(self):  
		self.mirror_x = True
		binary_representation = self.to_binary()
		retval = ''
		for row_start in range(12, -1, -4):
			retval += binary_representation[row_start : row_start + 4]
		self.representation = int(retval,2)	
		
	def horizontally_swap_shape(letter):  # return binary 16 digits long string
		retval = ''
		for row_start in range(12, -1, -4):
			retval += shapes[letter].to_binary()[row_start : row_start + 4]
		return retval
