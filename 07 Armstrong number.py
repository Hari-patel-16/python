num = int(input("Enter a number: "))


temp = num
len = len(str(num))
total = 0


while temp > 0:
    digit = temp % 10
    #print(digit)
    total = total + digit ** len
    #print(total)
    temp = temp // 10
    #print(temp)
if total == num:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
