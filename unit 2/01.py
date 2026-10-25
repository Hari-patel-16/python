
# Create a list of ten integers using range()
numbers = list(range(1, 11))

# a) Display list, positive indexing, negative indexing, and slicing
print("Original List:", numbers)
print("Positive Indexing (index 0):", numbers[0])
print("Negative Indexing (index -1):", numbers[-1])
print("Slicing (index 2 to 5):", numbers[2:6])

# b) Update an element at a specified index
index = int(input("Enter index to update (0-9): "))
if 0 <= index < len(numbers):
    value = int(input("Enter new value: "))
    numbers[index] = value
    print("Updated List:", numbers)
else:
    print("Invalid index!")

# c) List concatenation and repetition
print("Concatenation (+):", numbers + [11, 12])
print("Repetition (*):", numbers * 2)

# d) Check whether a number exists using in and not in
num = int(input("Enter number to search: "))
print("Number exists (in):", num in numbers)
print("Number does not exist (not in):", num not in numbers)

# e) List methods
numbers.append(20)
print("After append(20):", numbers)

numbers.insert(2, 15)
print("After insert(2, 15):", numbers)

if 15 in numbers:
    numbers.remove(15)
print("After remove(15):", numbers)

removed = numbers.pop()
print("Popped element:", removed)
print("After pop():", numbers)

numbers.reverse()
print("After reverse():", numbers)

numbers.append(numbers[0])
print("Count of first element:", numbers.count(numbers[0]))

# f) Ascending and descending order using sort() and sorted()
numbers.sort()
print("Ascending using sort():", numbers)

print("Descending using sorted():", sorted(numbers, reverse=True))

# g) Aliasing and cloning
alias = numbers
clone = numbers.copy()

alias[0] = 100
print("Original after modifying alias:", numbers)
print("Alias:", alias)
print("Clone (unchanged):", clone)

# h) Maximum, minimum, and length
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Length:", len(numbers))
