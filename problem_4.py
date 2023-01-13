"""A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

"""

def greatest_product():
    container = []

    for i in range(100, 999):
        for j in range(100, 999):
            num = i * j
            if str(num) == str(num)[::-1]:
                container.append(num)
    return container
print(max(greatest_product()))