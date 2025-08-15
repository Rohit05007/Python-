name = "rohit singh"

nameshort = name[1]
print(nameshort)

nametwo = name[0:3]  # start from index 0 all the way till 3 (excluding 3)
print(nametwo)

print(name[-4:-1])  # Negative slicing
print(name[1:4])  # corresponding positive index

print(name[:4])  # is same as print(name[0:4])
print(name[1:])  # is same as print(name[1:5])

# Strings  Funtions----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 1. Length of string
print(len(name))  # 11

# 2. Convert to uppercase
print(name.upper())  # ROHIT SINGH

# 3. Convert to lowercase
print(name.lower())  # rohit singh

# 4. First letter capital
print(name.capitalize())  # Rohit singh

# 5. First letter of each word capital
print(name.title())  # Rohit singh

# 6. Replace text
print(name.replace("singh", "bisht"))  # rohit singh

# 7. Count occurrences of a character
print(name.count("r"))  # 2

# 8. Find index of substring
print(name.find("singh"))  # 6

# 9. Check if starts with substring
print(name.startswith("roh"))  # True

# 10. Check if ends with substring
print(name.endswith("ngh"))  # True

# Escap sequence characters----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 1. Newline
print("Hello\nWorld")

# 2. Tab
print("Hello\tWorld")

# 3. Single quote inside single-quoted string
print("It's Python")

# 4. Double quote inside double-quoted string
print('He said "Python is fun"')

# 5. Backslash
print("This is a backslash: \\")

# 6. Backspace
print("Hello\bWorld")

# 7. Carriage return
print("Hello\rWorld")

# 8. Form feed
print("Hello\fWorld")

# 9. Unicode character
print("Unicode heart: \u2764")
