def is_odd_string(word):
    """Is the sum of the character-positions odd?

    Word is a simple word of uppercase/lowercase letters without punctuation.

    For each character, find it's "character position" ("a"=1, "b"=2, etc).
    Return True/False, depending on whether sum of those numbers is odd.

    For example, these sum to 1, which is odd:

        >>> is_odd_string('a')
        True

        >>> is_odd_string('A')
        True

    These sum to 4, which is not odd:

        >>> is_odd_string('aaaa')
        False

        >>> is_odd_string('AAaa')
        False

    Longer example:

        >>> is_odd_string('amazing')
        True
    """

    # # Initialize a variable to keep track of the sum of character positions
    # char_position_sum = 0

    # for char in word:
    #     # Use the ord() function to get the ASCII code of the character and subtract ord('a') for lowercase letters
    #     # You can also handle uppercase letters by converting them to lowercase using the lower() method
    #     char_position = ord(char.lower()) - ord('a') + 1

    #     # Add the character position to the sum
    #     char_position_sum += char_position

    # # Check if the sum is odd and return True or False accordingly
    # return char_position_sum % 2 == 1

    DIFF = ord("a") - 1

    total = sum((ord(c) - DIFF) for c in word.lower())

    return total % 2 == 1


is_odd_string('a')
# True
is_odd_string('A')
# True
is_odd_string('aaaa')
# False
is_odd_string('AAaa')
# False
is_odd_string('amazing')
# True
