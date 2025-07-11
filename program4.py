def countNumOfMultiples():
    ip = [1,2,8,9,12,46,76,82,15,20,30]
    output = {}
    for i in range(1, 10):
        count = 0
        for j in ip:
            if (j % i == 0):
                count += 1
        output[i] = count
    return output
result = countNumOfMultiples()
print(result)
