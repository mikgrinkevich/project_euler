"""n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!"""

def factorial(n):
    x = n
    for i in range(1, n):
        x = x*(n-i)
    return x


sumOfDigits = sum(int(digit) for digit in str(factorial(100))) # gets the number of digits in string 


print("The sum of digits for factorial 100 is " +str(sumOfDigits))   