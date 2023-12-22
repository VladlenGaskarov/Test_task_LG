import random


def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers
    smaller_numbers = []
    equal_numbers = []
    bigger_numbers = []
    random_index = random.randint(0, len(numbers)-1)
    for n in numbers:
        if n < numbers[random_index]:
            smaller_numbers.append(n)
        elif n > numbers[random_index]:
            bigger_numbers.append(n)
        else:
            equal_numbers.append(n)
    return quick_sort(smaller_numbers)+equal_numbers+quick_sort(bigger_numbers)
