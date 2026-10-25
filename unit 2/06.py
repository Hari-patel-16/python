
import array

# Create an integer array containing eight elements
a = array.array('i', [10, 20, 30, 40, 50, 60, 70, 80])

# a) Display array and access elements using indexing and slicing
print("Original Array:", a)
print("First Element:", a[0])
print("Last Element:", a[-1])
print("Sliced Array:", a[2:6])

# b) Insert a new element at a specified position
a.insert(2, 25)
print("After insert():", a)

# c) Remove a specified element and the last element
a.remove(40)
print("After remove(40):", a)

removed = a.pop()
print("Popped Element:", removed)
print("After pop():", a)

# d) Search for an element and display its index
num = int(input("Enter element to search: "))

if num in a:
    print("Element found at index:", a.index(num))
else:
    print("Element not found in the array")

# e) Check element membership
check = int(input("Enter element to check membership: "))
print("Element exists (in):", check in a)
print("Element does not exist (not in):", check not in a)

# f) Display maximum, minimum, and length
print("Maximum Element:", max(a))
print("Minimum Element:", min(a))
print("Length of Array:", len(a))

# g) Reverse the array
a.reverse()
print("Reversed Array:", a)
