def two_oldest_ages(ages):
    """Return two distinct oldest ages as tuple (second-oldest, oldest)..

        >>> two_oldest_ages([1, 2, 10, 8])
        (8, 10)

        >>> two_oldest_ages([6, 1, 9, 10, 4])
        (9, 10)

    Even if more than one person has the same oldest age, this should return
    two *distinct* oldest ages:

        >>> two_oldest_ages([1, 5, 5, 2])
        (2, 5)
    """

    # NOTE: don't worry about an optimized runtime here; it's fine if
    # you have a runtime worse than O(n)

    # NOTE: you can sort lists with lst.sort(), which works in place (mutates);
    # you may find it helpful to research the `sorted(iter)` function, which
    # can take *any* type of list-like-thing, and returns a new, sorted list
    # from it.

    # oldest_ages = ()
    # for age in list(ages):
    #     if ages.index(age) > age:
    #         oldest_ages.append(age)
    # return oldest_ages

    unique_ages = list(set(ages))
    unique_ages.sort(reverse=True)

    # Check if there are at least two distinct ages in the list
    if len(unique_ages) >= 2:
        # Return a tuple with the second-oldest and oldest ages
        return (unique_ages[1], unique_ages[0])
    else:
        # If there are fewer than two distinct ages, return what's available
        return tuple(unique_ages)


two_oldest_ages([1, 2, 10, 8])
# (8, 10)
two_oldest_ages([6, 1, 9, 10, 4])
# (9, 10)
two_oldest_ages([1, 5, 5, 2])
# (2, 5)
