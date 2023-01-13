"""145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included.

"""

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