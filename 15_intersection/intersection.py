def intersection(l1, l2):
    """Return intersection of two lists as a new list::

        >>> intersection([1, 2, 3], [2, 3, 4])
        [2, 3]

        >>> intersection([1, 2, 3], [1, 2, 3, 4])
        [1, 2, 3]

        >>> intersection([1, 2, 3], [3, 4])
        [3]

        >>> intersection([1, 2, 3], [4, 5, 6])
        []
    """

    l3 = []

    for item1 in l1:
        for item2 in l2:
            if item1 == item2:
                l3.append(item1)
    return l3

    # set2 = set(l2)
    # return [val for val in l1 if val in set2]


intersection([1, 2, 3], [2, 3, 4])
intersection([1, 2, 3], [1, 2, 3, 4])
intersection([1, 2, 3], [3, 4])
intersection([1, 2, 3], [4, 5, 6])
