
# Accept a sentence from the user
sentence = input("Enter a sentence: ")

# Remove leading and trailing spaces
print("Original Sentence:", repr(sentence))
print("After lstrip():", repr(sentence.lstrip()))
print("After rstrip():", repr(sentence.rstrip()))
sentence = sentence.strip()
print("After strip():", repr(sentence))

# a) Search for a substring using find() and index()
sub = input("Enter substring to search: ")

print("Using find():", sentence.find(sub))

try:
    print("Using index():", sentence.index(sub))
except ValueError:
    print("Substring not found using index()")

# b) Count occurrences of a word
word = input("Enter word to count: ")
print("Occurrences:", sentence.count(word))

# c) Replace a word or character
old = input("Enter word/character to replace: ")
new = input("Enter replacement: ")
print("After replace():", sentence.replace(old, new))

# d) Split sentence into words and join them
words = sentence.split()
print("Words:", words)
print("Joined Sentence:", "-".join(words))

# e) Demonstrate string immutability
try:
    sentence[0] = "X"
except TypeError:
    print("Cannot modify a string character using indexing.")
    print("Strings are immutable in Python.")

# f) Sort words alphabetically
sorted_words = sorted(words, key=str.lower)
print("Words in Alphabetical Order:", sorted_words)
