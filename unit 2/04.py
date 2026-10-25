
# Accept two strings from the user
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

# a) Display strings and their lengths
print("First String:", str1)
print("Length of First String:", len(str1))
print("Second String:", str2)
print("Length of Second String:", len(str2))

# b) Access characters using positive and negative indexing
if len(str1) > 0:
    print("First character of first string:", str1[0])
    print("Last character of first string:", str1[-1])

if len(str2) > 0:
    print("First character of second string:", str2[0])
    print("Last character of second string:", str2[-1])

# c) Extract substrings using slicing
print("Substring of first string:", str1[0:3])
print("Substring of second string:", str2[0:3])

# d) Repeat and concatenate strings
print("Repeated First String:", str1 * 2)
print("Concatenated Strings:", str1 + str2)

# e) Check whether a character or substring exists
sub = input("Enter a character or substring to search: ")
print("Substring exists (in):", sub in str1)
print("Substring does not exist (not in):", sub not in str1)

# f) Compare two strings
print("str1 == str2:", str1 == str2)
print("str1 != str2:", str1 != str2)
print("str1 < str2:", str1 < str2)
print("str1 > str2:", str1 > str2)

# g) Convert strings to uppercase and lowercase
print("First String in Uppercase:", str1.upper())
print("First String in Lowercase:", str1.lower())
print("Second String in Uppercase:", str2.upper())
print("Second String in Lowercase:", str2.lower())
