"""Unit Tests."""
import pytest
from exercises.ex06.dictionary import invert
from exercises.ex06.dictionary import favorite_color
from exercises.ex06.dictionary import count
from exercises.ex06.dictionary import alphabetizer
from exercises.ex06.dictionary import update_attendance

__author__ = "730668208"


def test_invert_one() -> None:
    """Tests the invert function use case."""
    assert invert({"Ten": "Turkeys"}) == {"Turkeys": "Ten"}


def test_invert_two() -> None:
    """Tests the invert function again use case."""
    assert invert({"Dog": "Corn"}) == {"Corn": "Dog"}


def test_invert_special() -> None:
    """Tests the invert function edge case."""
    with pytest.raises(KeyError):
        my_dictionary = {"Dog": "Corn", "Hole": "Corn"}
        invert(my_dictionary)


def test_favorite_color_one() -> None:
    """Tests the favorite_color function use case."""
    assert favorite_color({"Vincent": "Pink", "Tom": "Pink", "Bryan": "Blue"}) == "Pink"


def test_favorite_color_two() -> None:
    """Tests the favorite_color function again use case."""
    assert favorite_color({"Vincent": "Red", "Tom": "Pink", "Bryan": "Red"}) == "Red"


def test_favorite_color_special() -> None:
    """Tests the favorite_color function edge case."""
    assert favorite_color({"Vincent": "Pink", "Tom": "Red", "Bryan": "Blue"}) == "Pink"


def test_count_one() -> None:
    """Tests the count function use case."""
    assert count(["apple", "bannana", "bannana", "apple", "orange"]) == {"apple": 2, "bannana": 2, "orange": 1}

    
def test_count_two() -> None:
    """Tests the count function use case."""
    assert count(["Micahel", "Sarah", "Sarah", "Emily"]) == {"Michael": 1, "Sarah": 2, "Emily": 1}


def test_count_special() -> None:
    """Tests the count function edge case."""
    assert count([1, 2, 3]) == {1: 1, 2: 1, 3: 1}


def test_alphabetizer_one() -> None:
    """Tests the alphabetizer function use case."""
    assert alphabetizer(["mouse", "mice", "morning", "apple"]) == {"m": ["mouse", "mice", "morning"], "a": ["apple"]}


def test_alphabetizer_two() -> None:
    """Tests the alphabetizer function use case."""
    assert alphabetizer(["cupcake", "cost", "bread", "ban"]) == {"c": ["cupcake, cost"], "b": ["bread", "ban"]}


def test_alphabetizer_special() -> None:
    """Tests the alphabetizer function edge case."""
    assert alphabetizer(["Michael", "man", "orange"]) == {"m": ["Michael", "man"], "o": ["orange"]}


def test_update_attendance_one() -> None:
    """Tests update_attendance function use case."""
    attendance_log: dict = {"Tuesday": ["Michael", "Tom"], "Thursday": ["Marissa"]}
    assert update_attendance(attendance_log, "Tuesday", "Ali") == {"Tuesday": ["Michael", "Tom", "Ali"], "Thursday": ["Marissa"]}


def test_update_attendance_two() -> None:
    """Tests update_attendance function use case."""
    attendance_log: dict = {"Tuesday": ["Michael", "Tom"], "Thursday": ["Marissa"]}
    assert update_attendance(attendance_log, "Wednesday", "Michael") == {"Tuesday": ["Michael", "Tom"], "Thursday": ["Marissa"], "Wednesday": "Michael"}


def test_update_attendance_special() -> None:
    """Tests update_attendance function edge case."""
    attendance_log: dict = {"Tuesday": ["Michael", "Tom"], "Thursday": ["Marissa"]}
    assert update_attendance(attendance_log, 2, "Ali") == "2 is not a day of the week, try again!"