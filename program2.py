def seriesOfNumbers1(a):
    for i in range(1, a*2):
        if (i % 2 != 0):
            print(i)
a = int(input("Enter the number: "))
seriesOfNumbers1(a)