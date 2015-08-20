# Problem : Create a function that determines
# if the string contains only unique chars.


def unique_chars(str):
    if len(str) > 256:  # No string with unique chars can have more than 256 different chars
        return False

    repeated_chars = []
    for c in str:
        if c in repeated_chars:
            return False
        else:
            repeated_chars.append(c)

    return True
