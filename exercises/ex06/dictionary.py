"""Dictionary Functions."""
__author__ = "730668208"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and dictionaries in the list and returns the dictionary."""
    inverted_dict = {}
    key_list = []
    for keys in dictionary:
        inverted_dict[dictionary[keys]] = keys
        key_list.append(dictionary[keys])
    for x in range(0, len(key_list)):
        i = x + 1
        for i in range(x + 1, len(key_list)):
            if key_list[x] == key_list[i]:
                raise KeyError("Error! Repeated key value!")
    return inverted_dict


def favorite_color(dictionary: dict[str, str]) -> str:
    """Picks the most popular color out of the dictionary and returns it."""
    top_color = ""
    top_count = 0
    for items in dictionary:
        current_color = dictionary[items]
        color_count = 0
        for names in dictionary:
            if dictionary[names] == current_color:
                color_count += 1
        if color_count > top_count:
            top_color = dictionary[items]
            top_count = color_count
    return top_color


def count(unique_value: list[str]) -> dict[str, int]:
    """Key are items and when the items are repeated, the value goes up by one."""
    dictionary_result: dict[str, int] = {}
    for values in unique_value:
        if values in dictionary_result:
            dictionary_result[values] += 1
        else:
            dictionary_result[values] = 1
    return dictionary_result


def alphabetizer(words_list: list[str]) -> dict[str, list[str]]:
    """Organizes words into alpahbetical order."""
    dictionary: dict[str, list[str]] = {}
    for word in words_list:
        lower_case: str = word.lower()
        print(lower_case)
        cumulative_list = []
        alphabet_list = []
        if lower_case[0] in dictionary:
            cumulative_list = (dictionary[lower_case[0]])
            cumulative_list.append(word)
            dictionary[lower_case[0]] = cumulative_list
        else:
            alphabet_list.append(word)
            dictionary[lower_case[0]] = alphabet_list
    return dictionary


def update_attendance(weekly_attendance: dict[str, list[str]], day_week: str, student: str) -> dict[str, list[str]]:
    """Updates attendace based off the weekday."""
    cumulative_attendance = []
    if day_week in weekly_attendance:
        cumulative_attendance = weekly_attendance[day_week]
        if student in cumulative_attendance:
            return weekly_attendance
        else:
            cumulative_attendance.append(student)
        weekly_attendance[day_week] = cumulative_attendance
    else:
        cumulative_attendance.append(student)
        weekly_attendance[day_week] = cumulative_attendance
    return weekly_attendance
