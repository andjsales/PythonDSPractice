def min_max_keys(d):
    """Return tuple (min-keys, max-keys) in d.

        >>> min_max_keys({2: 'a', 7: 'b', 1: 'c', 10: 'd', 4: 'e'})
        (1, 10)

    Works with any kind of key that can be compared, like strings:

        >>> min_max_keys({"apple": "red", "cherry": "red", "berry": "blue"})
        ('apple', 'cherry')
    """

    # for keys in d.keys():
    #     if d.keys() == isinstance(int):

    keys = list(d.keys())

    if isinstance(keys[0], int):
        min_key = min(keys)  # Find the minimum numeric key
        max_key = max(keys)  # Find the maximum numeric key
    else:
        min_key = min(keys)  # Find the minimum string key (lexicographically)
        max_key = max(keys)  # Find the maximum string key (lexicographically)

    return {min_key, max_key}


min_max_keys({2: 'a', 7: 'b', 1: 'c', 10: 'd', 4: 'e'})
# (1, 10)
min_max_keys({"apple": "red", "cherry": "red", "berry": "blue"})
# ('apple', 'cherry')
