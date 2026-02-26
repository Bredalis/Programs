
# Algorithm to sort numeric sequences
# by finding the minimum and placing it in the first position

def selection_sort(numbers):
    if not isinstance(numbers, list):
        return None

    sorted_list = []
    numbers_copy = numbers.copy()

    for _ in range(len(numbers_copy)):
        minimum = min(numbers_copy)
        sorted_list.append(minimum)
        numbers_copy.remove(minimum)

    return sorted_list
