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


def printboard():
    for row in playfield:
        for letter in row:
            print(' ' + letter, end='')

        print()


def available_shapes():
    used_shapes = set()
    for row in playfield:
        for letter in row:
            used_shapes.add(letter)
    return shapes.keys() - used_shapes


printboard()


def display_shape(letter):
    print(shapes[letter])


for letter in available_shapes():
    display_shape(letter)
