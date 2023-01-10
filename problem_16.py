def twotothepower(N):
    number = 2**N
    sumnum = sum(int(digit) for digit in str(number))
    return sumnum

print(twotothepower(1000))