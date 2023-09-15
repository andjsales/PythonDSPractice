def truncate(phrase, n):
    """Return truncated-at-n-chars version of phrase.

    If the phrase is longer than, or the same size as, n make sure it ends with '...' and is no longer than n.

        >>> truncate("Hello World", 6)
        'Hel...'

        >>> truncate("Problem solving is the best!", 10)
        'Problem...'

        >>> truncate("Yo", 100)
        'Yo'

    The smallest legal value of n is 3; if less, return a message:

        >>> truncate('Cool', 1)
        'Truncation must be at least 3 characters.'

        >>> truncate("Woah", 4)
        'W...'

        >>> truncate("Woah", 3)
        '...'
    """

    if n < 3:
        return "Truncation must be at least 3 characters."

    # elif n == 3:
    #     return "..."

    # truncated_phrase = ''
    # if range(n):
    #     for char in phrase:
    #         truncated_phrase += char
    #         for char in truncated_phrase:
    #             truncated_phrase.replace(char, '...', -3)
    #     return truncated_phrase

    elif n <= len(phrase):
        return phrase[:n - 3] + "..."
    else:
        return phrase


truncate('Cool', 1)
truncate("Hello World", 6)
# 'Hel...'
