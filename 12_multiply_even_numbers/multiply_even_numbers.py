def multiply_even_numbers(nums):
    """Multiply the even numbers.

        >>> multiply_even_numbers([2, 3, 4, 5, 6])
        48

        >>> multiply_even_numbers([3, 4, 5])
        4

    If there are no even numbers, return 1.

        >>> multiply_even_numbers([1, 3, 5])
        1
    """

    evens_product = 1  # Initialize the product to 1
    for num in nums:
        if num % 2 == 0:
            evens_product *= num  # Multiply the even number with the product

    return evens_product  # Return the final product


multiply_even_numbers([2, 3, 4, 5, 6])  # Output: 48
