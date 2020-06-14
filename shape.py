
class Shape:
    letter_name = ''
    init_representation = 0
    representation = 0

    def __init__(self, name, number):
        self.letter_name = name
        self.init_representation = self.representation = number

    def get_number(self):
        return self.representation

    def get_name(self):
        return self.letter_name
    
    def reset(self):
        self.representation = self.init_representation
        
    def to_binary(self):  # returns string
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

    def mirror_y(self):
        lut_mirror_y = {"0000": "0000", "0001": "1000", "0010": "0100", "0011": "1100",
                        "0100": "0010", "0101": "1010", "0110": "0110", "0111": "1110",
                        "1000": "0001", "1001": "1001", "1010": "0101", "1011": "1101",
                        "1100": "0011", "1101": "1011", "1110": "0111", "1111": "1111"}
        binary_representation = self.to_binary()
        mirror = ''
        for row_start in range(0, 16, 4):
            tmp = binary_representation[row_start: row_start + 4]
            mirror = mirror + lut_mirror_y[tmp]
        self.representation = int(mirror, 2)

    def mirror_x(self):
        binary_representation = self.to_binary()
        mirror = ''
        for row_start in range(12, -1, -4):
            mirror += binary_representation[row_start: row_start + 4]
        self.representation = int(mirror, 2)
        
    def rotate(self, angle):
        binary_representation = self.to_binary()
        rotation_buffer = list(16 * '0')
        for y in range(4):
            for x in range(4):
                offset = x + 4 * y
                if binary_representation[offset] == '1':
                    offset2 = y + 4 * x
                    rotation_buffer[offset2] = '1'
        self.representation = int(''.join(rotation_buffer), 2)
        if angle == 90:
            self.mirror_x()
        if angle == 270:
            self.mirror_y()   
    
    @staticmethod
    def get_all_orientations():
        return ['rot_0', 'rot_90', 'rot_180', 'rot_270',
                'mirror_x', 'mirr_rot_90', 'mirr_rot_180', 'mirr_rot_270', 'mirror_y']
        
    def set_orientation(self, orientation):
        self.reset()
        if orientation == 'rot_0':
            return
        if orientation == 'mirror_x':
            self.mirror_x()
        if orientation == 'mirror_y':
            self.mirror_y()
        if orientation == 'rot_90':
            self.rotate(90)
        if orientation == 'rot_180':
            self.mirror_x()
            self.mirror_y()
        if orientation == 'rot_270':
            self.rotate(270)
        if orientation == 'mirr_rot_90':
            self.mirror_x()
            self.rotate(90)
        if orientation == 'mirr_rot_180':
            self.mirror_y()
        if orientation == 'mirr_rot_270':
            self.mirror_x()
            self.rotate(270)


if __name__ == "__main__":
    my_shape = Shape('A', 0x44c0)

    for rotation in my_shape.get_all_orientations():
        my_shape.set_orientation(rotation)
        my_shape.display()
