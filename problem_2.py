"""Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms."""



def evenFibSum(input):
    if (input < 2):
        return 0

    ef1 = 0
    ef2 = 2
    sm = ef1 + ef2

    # calculating sum of even Fibonacci value
    while (ef2 <= input):

        ef3 = 4 * ef2 + ef1

        if (ef3 > input):
            break

        # sum
        ef1 = ef2
        ef2 = ef3
        sm = sm + ef2

    return sm

inp = int(input())
print(evenFibSum(inp))