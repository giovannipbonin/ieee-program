from math import sqrt
from sys import stdout
from typing import Set, Tuple

X = 0
Y = 1

def choose_dimensions(area: int) -> Tuple[int, int]:
    """
    Determine the dimensions of a rectangle of area at least as big as `area`.
    Since we can describe a rectangle by just two points, we will assume that the
    bottom left point is (1,1). All we need to do is determine the top right point
    :return: Tuple of the x-y coordinates of the top-right point
    """
    pass

def send_and_get_results(curr_x: int, curr_y: int) -> Tuple[int, int]:
    """
    Interacts with `testing_tool.py` to get a random number in the 3x3 square determined by curr_x, curr_y
    The gopher will randomly pick one of the numbers in the 3x3 square
    :param curr_x:
    :param curr_y:
    :return: Tuple of the position filled. Returns (-1,-1) if an error occurred
    """

    print(curr_x, curr_y)
    stdout.flush()
    return tuple(map(int, input().split(" ")))


def update_current_position(curr_x: int, curr_y: int, dims: Tuple[int, int]) -> Tuple[int, int]:
    """
    A function to pick the next point to let our gopher fill
    :param curr_x:
    :param curr_y:
    :param dims:
    :return:
    """
    xMax, yMax = dims
    if curr_y == yMax - 1: # at the top of the box
        nextY = 2
        if curr_x == xMax - 1:
            nextX = 2
        else:
            nextX = min(curr_x + 3, xMax - 1)
    else:
        nextY = min(curr_y + 3, yMax - 1)
        nextX = curr_x
    return nextX, nextY


def cube_is_filled(curr_x: int, curr_y: int, already_filled: Set[Tuple[int, int]], dims: Tuple[int, int]) -> bool:
    """
    Given a center position for your cube, return whether the 3x3 cube around the center of the cube is filled.
    curr_x: x-coordinate of the center of the cube
    curr_y: y-coordinate of the center of the cube
    already_filled: A set of tuples (int, int) that contain the positions of the already filled squares
    dims: The dimensions of the rectangle we're trying to fill
    return: True if the 3x3 cube is filled. False otherwise
    """
    pass

def rectangle_is_filled(already_filled: Set[Tuple[int, int]], dims: Tuple[int, int]) -> bool:
    """
    Determine whether all squares within our rectangle 
    (with (1,1) as the bottom-left point and `dims` as the top right point )
    is filled.
    return: Boolean
    """
    pass


def fill_the_rectangle(DIMS):
    """
    Runs an algorithm to fill the rectangle
    :param DIMS:
    :return:
    """
    already_filled = set()

    curr_x = 0
    curr_y = -1

    number_of_gopher_fillings = 0 # The number of times you have asked your gopher to get to work

    while number_of_gopher_fillings < 1000:
        curr_x, curr_x= update_current_position(curr_x, curr_y, DIMS)

        if cube_is_filled(curr_x, curr_y, already_filled, DIMS):
            update_current_position(curr_x, curr_y, DIMS)
            continue

        x, y = send_and_get_results(curr_x, curr_y)
        number_of_gopher_fillings += 1

        if x == 0 and y == 0 and rectangle_is_filled(already_filled, DIMS):
            return True
        elif x == -1 and y == -1:
            return False
        elif (x, y) not in already_filled:
            already_filled.add((x, y))



T = int(input())
for _ in range(T):
    area = int(input()) # The area of the rectangle you need to fill

    # We'll choose these dimensions for our rectangle such that the area of our rectangle is at least `area
    # We need to fill everything inside of this rectangle
    DIMS = choose_dimensions(area)

    if not fill_the_rectangle(DIMS):
        raise Exception("FAILED TO FILL THE RECTANGLE")