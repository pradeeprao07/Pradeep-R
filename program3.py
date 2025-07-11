def seriesOfNumbers2(a):
    reference = []
    if(a % 2 != 0):
        for i in range(1, a*2):
            if(i % 2 != 0):
                print(i)
                reference.append(i)
    elif(a % 2 == 0):
        for i in range(1, a*2):
            if(i % 2 != 0):
                reference.append(i)
                print(reference, "ref")
        for i in range(len(reference)-1):
            print(reference[i])
a = int(input("Enter the number: "))
seriesOfNumbers2(a)