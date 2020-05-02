class Shape:
	letter_name = ''
	rotation = 0
	is_mirror_x = False
	is_mirror_y = False
	representation = 0
	
	def __init__(self, name, number):
		self.letter_name = name
		self.representation = number
	
	def get_number(self):
		return self.representation
		
	def get_name(self):
		return self.letter_name
	
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
		self.is_mirror_x = True
		binary_representation = self.to_binary()
		mirror = ''
		for row_start in range(12, -1, -4):
			mirror += binary_representation[row_start : row_start + 4]
		self.representation = int(mirror,2)	
		
	def set_orientation(self, orientation):
		if orientation == 0:
			return
		if orientation == 'mirror_x':
			self.mirror_x()
