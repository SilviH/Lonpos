#TO DO:
#
import cProfile, pstats, io
from pstats import SortKey
pr = cProfile.Profile()
pr.enable()
# ... do something ...

import copy
import shape
import playfield

print('Lonpos!')
## riddle 005
#initial_playfield = (['H', 'H', 'B', 'B', 'B', 'C', 'C', 'C', 'C', 'K', 'K'],
#                     ['D', 'H', 'H', 'B', 'B', 'C', 'A', 'A', 'A', 'K', 'K'],
#                     ['D', 'D', 'H', 'E', 'E', 'L', 'I', 'I', 'A', '.', '.'],
#                     ['D', 'E', 'E', 'E', 'L', 'L', 'L', 'I', '.', '.', '.'],
#                     ['D', 'J', 'J', 'J', 'J', 'L', 'I', 'I', '.', '.', '.']
#                     )

## riddle 006
#initial_playfield = (['J', 'J', 'J', 'J', 'H', 'H', 'D', 'D', 'D', 'D', 'F'],
#                     ['C', 'C', 'I', 'I', 'L', 'H', 'H', 'D', 'E', 'F', 'F'],
#                     ['C', 'G', 'I', 'L', 'L', 'L', 'H', 'E', 'E', '.', '.'],
#                     ['C', 'G', 'I', 'I', 'L', 'B', 'B', 'E', '.', '.', '.'],
#                     ['C', 'G', 'G', 'G', 'B', 'B', 'B', 'E', '.', '.', '.']
#                     )

### riddle 007 needs vertical mirror
#initial_playfield = (['E', 'E', 'G', 'G', 'G', 'D', 'D', 'D', 'D', 'K', 'K'],
#			 ['J', 'E', 'E', 'E', 'G', 'C', 'D', 'H', 'H', 'K', 'K'],
#			 ['J', 'I', 'I', 'L', 'G', 'C', 'H', 'H', '.', '.', '.'],
#			 ['J', 'I', 'L', 'L', 'L', 'C', 'H', 'F', '.', '.', '.'],
#			 ['J', 'I', 'I', 'L', 'C', 'C', 'F', 'F', '.', '.', '.']
#			 )

### riddle 008
#initial_playfield = (['B', 'B', 'D', 'D', 'D', 'D', 'H', 'H', 'A', 'A', 'A'],
#			 ['B', 'B', 'B', 'F', 'D', 'H', 'H', 'E', 'E', 'E', 'A'],
#			 ['I', 'I', 'L', 'F', 'F', 'H', 'E', 'E', '.', '.', '.'],
#			 ['I', 'L', 'L', 'L', 'C', 'C', 'C', 'C', '.', '.', '.'],
#			 ['I', 'I', 'L', 'J', 'J', 'J', 'J', 'C', '.', '.', '.']
#			 )

## riddle 025
initial_playfield = (['J', 'I', 'I', 'L', 'F', 'F', '.', '.', '.', '.', '.'],
			 ['J', 'I', 'L', 'L', 'L', 'F', '.', '.', '.', '.', '.'],
			 ['J', 'I', 'I', 'L', 'E', 'E', 'H', 'A', '.', '.', '.'],
			 ['J', 'D', 'E', 'E', 'E', 'H', 'H', 'A', '.', '.', '.'],
			 ['D', 'D', 'D', 'D', 'H', 'H', 'A', 'A', '.', '.', '.']
			 )


all_shapes = {'A': 0x44c0, 'B': 0x4cc0, 'C': 0x444c, 'D': 0x44c4,
              'E': 0x44c8, 'F': 0x4c00, 'G': 0x22e0, 'H': 0x26c0,
              'I': 0xae00, 'J': 0x8888, 'K': 0xcc00, 'L': 0x4e40,
              }
shapes = {}



# fits in the first possible fitting orientations
def recurse_process_shape(playfield, current_shape, rest_shapes): 
    # saving parametres for rerun
    remaining_shapes = list(rest_shapes)
    playfield2 = copy.deepcopy(playfield)
    for orientation in current_shape.get_all_orientations():
        current_shape.set_orientation(orientation)
        place = playfield2.first_fitting_position(current_shape)
        if len(place) > 0:
            playfield2 = playfield2.insert_shape(current_shape, place[1], place[0])
            if playfield2.is_solved():
                playfield.board = copy.deepcopy(playfield2.board)
                break
            if len(remaining_shapes) > 0:
                next_shape = remaining_shapes[0]
                remaining_shapes = remaining_shapes[1:]
                playfield2 = recurse_process_shape(playfield2, next_shape, remaining_shapes)
                if playfield2.is_solved():
                    playfield = copy.deepcopy(playfield2)
                    break
                else:
                    playfield2 = copy.deepcopy(playfield)
                    remaining_shapes = list(rest_shapes) 
    return playfield


# program starts here

# create playfield object
riddle = playfield.Playfield(initial_playfield)
riddle.display()

for key, val in all_shapes.items():
    shapes[key] = shape.Shape(key, val)

temp = riddle.available_letters(shapes.keys())


starting_remaining_shapes = riddle.initial_remaining_shapes(shapes, riddle.available_letters(shapes.keys()))
for letter in range(len(temp)):  # how many available letters
    initial_shape = shapes[temp[letter]]  # take the available letters one by one as the einitial

    starting_remaining_shapes = starting_remaining_shapes[1:]
    result = recurse_process_shape(riddle, initial_shape, starting_remaining_shapes)
    if result.is_solved():
        print('RESULT')
        result.display()
        break
    starting_remaining_shapes.append(initial_shape)  # list of remaining shapes (objects)

pr.disable()
s = io.StringIO()
sortby = SortKey.CUMULATIVE
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
print(s.getvalue())

