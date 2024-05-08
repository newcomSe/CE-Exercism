def square(number):
    #Variable seeded with amount in first square
    grains_in_square = 1
    #Exception
    if number < 1 or number > 64:
        raise ValueError('square must be between 1 and 64')
    else:
        #Loop to  determine grains in a given square
        i = 2
        while i <= number:
            grains_in_square = grains_in_square * 2
            i = i +1
    return grains_in_square


def total():
    #Variables seeded with amount in first square
    grains_in_square = 1
    total_grains = 1
    #Loop to add grains from all squares starting from second square and stopping at the 64th
    i = 2
    while i < 65:
        grains_in_square = grains_in_square * 2
        total_grains = total_grains + grains_in_square
        i = i +1
    return total_grains
        
