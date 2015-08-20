__author__ = 'mark'

"""
File that contains functions to solve problems in the cracking the code interview book.
This module is imported by the unit testing classes and run assertions through them.
"""


def str_unique_chars(text):
    """
    1.1 Problem : Create a function that determines
    if the string contains only unique chars.

    :param text: string
    :return: boolean
    """
    if len(text) > 256:  # No string with unique chars can have more than 256 different chars
        return False

    repeated_chars = []
    for c in text:
        if c in repeated_chars:
            return False
        else:
            repeated_chars.append(c)

    return True


def str_replace_spaces(text, replace='%20'):
    """
    1.4 Replace all spaces in a string with %20 character
    Input: "Hello World"
    Output: "Hello%20World"

    :param text: string
    :param replace: string
    :return: string
    """
    return text.replace(" ", replace)


def str_compress(text):
    """
    Problem 1.5: Create method that compress a string using the count of repeated chars
    Example: aabccdddd would become a2b1c2d4 (only compress when the result is smaller than original)

    :param text: string
    :return: string
    """

    repeated_chars = {}
    for c in text:
        if c == ' ':
            continue
        repeated_chars[c] = repeated_chars.get(c, 0) + 1

    # We unpack the characters and repetitions and join them as string
    result = ["%s%d" % (k, v) for k, v in repeated_chars.items()]
    result = "".join(result)

    return result if len(result) < len(text) else text
