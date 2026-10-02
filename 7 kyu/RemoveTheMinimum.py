## Given an array of integers, remove the smallest value. Do not mutate the original array/list. If there are multiple elements with the same value, remove the one with the lowest index. If you get an empty array/list, return an empty array/list.

def remove_smallest(numbers):
    if not numbers:
        return []
    idx = numbers.index(min(numbers))
    return numbers[:idx] + numbers[idx + 1:]