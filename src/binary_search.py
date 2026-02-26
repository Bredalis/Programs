
# Algorithm to find an element in a sorted list using binary search


def binary_search(numbers, target):
    """Searches for a number in a list and indicates its position."""
    if len(numbers) == 0:
        return "Empty list"

    numbers.sort()

    center = len(numbers) // 2
    left = numbers[:center]
    right = numbers[center:]

    if numbers[center] == target:
        return f"{target} is in the center"

    if target in left:
        return f"{target} is on the left"

    if target in right:
        return f"{target} is on the right"

    return "The number is not in the list"
