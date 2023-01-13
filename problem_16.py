"""215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?

"""

def twotothepower(N):
    number = 2**N
    sumnum = sum(int(digit) for digit in str(number))
    return sumnum

print(twotothepower(1000))