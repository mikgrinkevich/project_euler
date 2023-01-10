def smallmultiple(N):
    """This function will return the smallest positive number that is evenly divisible by concurrent numbers from 1 to N"""
    answer = 1
    list = []
    for i in range(2,N):
        list.append(i)
    for i in range(0, len(list)):
        for j in range(1, i+1):
            if list[i] % list[i-j] == 0:
                list[i] = int(list[i] / list[i-j])
    for i in range(0, len(list)):
        answer *= list[i]
    return answer

print(smallmultiple(20))