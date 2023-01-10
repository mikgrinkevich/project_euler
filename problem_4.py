def greatest_product():
    container = []

    for i in range(100, 999):
        for j in range(100, 999):
            num = i * j
            if str(num) == str(num)[::-1]:
                container.append(num)
    return container
print(max(greatest_product()))