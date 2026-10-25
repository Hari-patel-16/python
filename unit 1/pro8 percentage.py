print("----- Percentage Calculations -----")
marks1 = int(input("Enter marks of subject1 : "))
marks2 = int(input("Enter marks of subject2 : "))
marks3 = int(input("Enter marks of subject3 : "))
total = marks1 + marks2 + marks3
percentage = total / 3

if percentage >= 90:
  grade = "O"

elif percentage >= 80:
  grade = "A"

elif percentage >= 70:
   grade = "B"

elif percentage >= 60:
   grade = "C"

elif percentage >= 50:
    grade = "D"

elif percentage >= 40:
   grade = "E"

elif percentage < 40:
   grade = "F"

print("="*25)
print("Subject1 = ",marks1)
print("Subject2 = ",marks2)
print("Subject3 = ",marks3)
print("Total = ",total)
print("Percentage = {:.2f}%".format(percentage))
print("Grade = ",grade)
print("="*25)