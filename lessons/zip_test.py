"""Test my zip function."""
from lessons.zip import zip
__author__ = "730668208"


def test_list_length() -> None:
    """Testing when a list equals zero."""
    assert zip(["Happy", "Yes"], []) == {}


def test_list_one_element() -> None:
    """Testing when there is one element in both lists."""
    assert zip(["Happy"], [1]) == {"Happy": 1}


def test_list_two_element() -> None:
    """Testing when there is two elements in both lists."""
    assert zip(["Happy", "Sad"], [1, 2]) == {"Happy": 1, "Sad": 2}