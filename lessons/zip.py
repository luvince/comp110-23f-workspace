"""Combining two lists into a dictionary."""
__author__ = "730668208"


def zip(string_list: list[str], int_list: list[int]) -> dict[str, int]:
    """Uses two lists: One list is used as the key type, and the other is used for the value type."""
    dictionary: dict[str, int] = {}
    if len(string_list) == 0 or len(int_list) == 0:
        return dictionary
    if len(string_list) != len(int_list):
        return dictionary
    index = 0
    while index < len(string_list):
        dictionary[string_list[index]] = int_list[index]
        index += 1
    return dictionary
    