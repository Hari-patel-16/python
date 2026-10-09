n = int(input("Enter N: "))
total = 0


for i in range(2, n + 1):
    total = total + (1 / i)


print("Sum of series =", total)
