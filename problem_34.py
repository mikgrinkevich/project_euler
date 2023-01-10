import math

def check_sum(number):
    list_digits = list(str(number))
    check_sum = sum([math.factorial(int(digit)) for digit in list_digits])
    return check_sum == number

def final_sum(counter_min=3, counter_max=200000):
    """Find the sum of all the numbers."""
    final_sum = 0
    for counter in range(counter_min, counter_max):
        if check_sum(counter):
             final_sum += counter
    return final_sum

print(final_sum())