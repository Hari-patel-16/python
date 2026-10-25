
# Create a tuple containing ten values, including repeated values
t = (10, 20, 30, 40, 20, 50, 60, 10, 70, 80)

# a) Display tuple and access elements
print("Original Tuple:", t)
print("Positive Indexing (index 0):", t[0])
print("Negative Indexing (index -1):", t[-1])
print("Slicing (index 2 to 5):", t[2:6])

# b) Tuple concatenation and repetition
print("Concatenation (+):", t + (90, 100))
print("Repetition (*):", t * 2)

# c) Check whether an element exists
num = int(input("Enter a number to check: "))
print("Element exists (in):", num in t)
print("Element does not exist (not in):", num not in t)

# d) Maximum, minimum, and length
print("Maximum:", max(t))
print("Minimum:", min(t))
print("Length:", len(t))

# e) Count occurrences of a value
value = int(input("Enter a value to count: "))
print("Occurrences:", t.count(value))

# f) Search for an element using index()
search = int(input("Enter a value to find its index: "))

if search in t:
    print("Element found at index:", t.index(search))
else:
    print("Element not found in the tuple")
