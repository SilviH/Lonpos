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
        self.is_mirror_y = True
        binary_representation = self.to_binary()
        mirror = ''
        for row_start in range(0, 16, 4):
            tmp = binary_representation[row_start: row_start + 4]
            mirror = mirror + lut_mirror_y[tmp]
        self.representation = int(mirror, 2)

    def mirror_x(self):
        self.is_mirror_x = True
        binary_representation = self.to_binary()
        mirror = ''
        for row_start in range(12, -1, -4):
            mirror += binary_representation[row_start: row_start + 4]
        self.representation = int(mirror, 2)

    def set_orientation(self, orientation):
        if orientation == 0:
            return
        if orientation == 'mirror_x':
            self.mirror_x()


if __name__ == "__main__":
    my_shape = Shape('A', 0x44c0)
    my_shape.mirror_y()
    my_shape.display()
