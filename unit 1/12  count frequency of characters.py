file = open("sample.txt", "r")


text = file.read()


frequency = {}


for char in text:
    if char in frequency:
        frequency[char] = frequency[char] + 1
    else:
        frequency[char] = 1


file.close()


print("Character Frequency:")


for char, count in frequency.items():
    print(char, ":", count)
