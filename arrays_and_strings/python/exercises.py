__author__ = 'mark'

"""
File that contains functions to solve problems in the cracking the code interview book.
This module is imported by the unit testing classes and run assertions through them.
"""


def str_unique_chars(text):
    """
    Problem : Create a function that determines
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
    return text.replace (" ", replace)
