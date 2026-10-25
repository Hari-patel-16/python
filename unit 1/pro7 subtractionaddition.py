def addition(num1,num2):
    return num1+num2
def subtraction(num1,num2):
    return num1-num2
def multiplication(num1,num2):
    return num1*num2
def division(num1,num2):
    return num1/num2


print("------------Menu----------")
print("1. Addition ")
print("2. Subtraction ")
print("3. Multiplication ")
print("4. Division ")
choice = int(input("Please select the choice (1-4): "))

num1 = int(input("Please enter Num1 : "))
num2 = int(input("Please enter Num2 : "))

if choice==1:
 print("Subtraction = ",subtraction(num1,num2))

elif choice==3:
 print("Multiplication = ",multiplication(num1,num2))

elif choice==4:

    if (num2 != 0):
      print("Division =",division(num1, num2))

    else:
      print("Can not divide by zero")

else:
  print("Invalid Choice")