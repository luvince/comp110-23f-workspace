"""EX04- List Util!"""
__author__ = "730668208"


def all(input: list[int], number: int) -> bool:
    """Makes sure the list has the same numbers."""
    i = 0
    result = False
    while i < len(input):
        if number == input[i]:
            i += 1
            result = True
        else:
            return False
    return result


def max(input: list[int]) -> int:
    """Gets the max number from the list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    i = 0
    max_from_list = input[0]
    while i < len(input):
        if input[i] >= max_from_list:
            max_from_list = input[i]
        i += 1
    return max_from_list


def is_equal(input_one: list[int], input_two: list[int]) -> bool:
    """Makes sure the two lists are equal to each other."""
    result = True
    if len(input_one) != len(input_two):
        return False
    i = 0
    while i < len(input_one):
        if input_one[i] == input_two[i]:
            i += 1
        else:
            result = False
            i += 1
    return result
