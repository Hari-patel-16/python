
# Create a list containing five student names
list1 = ["Hari", "Diya", "Mansi", "Om", "Denisha"]

# Create a nested list containing student names and marks
list2 = [
    ["Hari", 85],
    ["Diya", 92],
    ["Mansi", 78],
    ["Om", 88],
    ["Denisha", 95]
]

# a) Search for a student name and display its index
name = input("Enter student name to search: ")

if name in list1:
    print("Student found at index:", list1.index(name))
else:
    print("Student not found")

# b) Sort student names in ascending and descending order
list1.sort()
print("Ascending order using sort():", list1)

print("Descending order using sorted():", sorted(list1, reverse=True))

# c) Add, insert, and remove student names
list1.append("Rahul")
print("After adding a student:", list1)

list1.insert(2, "Priya")
print("After inserting a student:", list1)

list1.remove("Rahul")
print("After removing a student:", list1)

# d) Display all student records using a loop
print("\nStudent Records:")
for student in list2:
    print("Name:", student[0], "Marks:", student[1])

# e) Find the student with the highest marks and calculate average
topper = max(list2, key=lambda student: student[1])
print("\nStudent with Highest Marks:", topper[0])
print("Highest Marks:", topper[1])

total = sum(student[1] for student in list2)
average = total / len(list2)
print("Average Marks:", average)

# f) Display the number of student records
print("Number of Student Records:", len(list2))
