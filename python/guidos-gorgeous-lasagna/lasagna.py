"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""



EXPECTED_BAKE_TIME = 40


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    result = EXPECTED_BAKE_TIME - elapsed_bake_time
    return result
    



def preparation_time_in_minutes(number_of_layers):
    """Calculate the prep time.

    :param number_of_layers: int - number of layers in lasagna.
    :return: int - prep time (in minutes) derived from number_of_layers.

    Function that takes the number of layers of the lasagna and determines the prep time at two           minutes per layer.
    """

    result = number_of_layers * 2
    return result



def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
     
    prep_time = number_of_layers * 2
    result = prep_time + elapsed_bake_time
    return result
    