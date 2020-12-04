import math
def find_next_square(sq):
    if int(math.sqrt(sq) + 0.5) **2 == sq:
        return (math.sqrt(sq) + 1) * (math.sqrt(sq) + 1)
    else:
        return -1
    
