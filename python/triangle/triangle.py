def equilateral(sides):
    check = lengths_valid(sides)
    if not check:
        is_equilateral = False
    else:
        is_equilateral = bool(sides[0] == sides[1] == sides[2])
    return is_equilateral


def isosceles(sides):
    check = lengths_valid(sides)
    if not check:
        is_isosceles = False
    else:
        is_isosceles = bool((sides[0] == sides[1]) or (sides[0] == sides[2]) or (sides[1] == sides[2]))
    return is_isosceles


def scalene(sides):
    check = lengths_valid(sides)
    if not check:
        is_scalene = False
    else:
        is_scalene = bool((sides[0] != sides[1]) and (sides[0] != sides[2]) and (sides[1] != sides[2]))
    return is_scalene
    
def lengths_valid(sides):
    for i in sides:
        if i <=0:
            no_sides = True
        else:
            no_sides = False
    if no_sides:
            lengths = False
    else:
        lengths = bool((int(sides[0]) + int(sides[1])) >= int(sides[2])) and ((int(sides[1]) + int(sides[2])) >= int(sides[0])) and ((int(sides[0]) + int(sides[2])) >= int(sides[1]))
    return lengths
            