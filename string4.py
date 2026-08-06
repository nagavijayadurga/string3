# ==============================
# 1. Count number of vowels in a string
# ==============================
s = input("Enter a string: ")
count = sum(1 for ch in s.lower() if ch in "aeiou")
print("Vowels:", count)

# ==============================
# 2. Remove duplicate characters
# ==============================
s = input("Enter a string: ")
result = ""
for ch in s:
    if ch not in result:
        result += ch
print("Without duplicates:", result)

# ==============================
# 3. Check if string is palindrome
# ==============================
s = input("Enter a string: ")
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

# ==============================
# 4. Replace all vowels with '*'
# ==============================
s = input("Enter a string: ")
result = ""
for ch in s:
    if ch.lower() in "aeiou":
        result += "*"
    else:
        result += ch
print(result)

# ==============================
# 5. Check if two strings are anagrams
# ==============================
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
if sorted(s1.lower()) == sorted(s2.lower()):
    print("Anagrams")
else:
    print("Not Anagrams")

# ==============================
# 6. Find all occurrences of a substring
# ==============================
s = input("Enter main string: ")
sub = input("Enter substring: ")
index = 0
while True:
    pos = s.find(sub, index)
    if pos == -1:
        break
    print(pos)
    index = pos + 1

# ==============================
# 7. Reverse each word in a sentence
# ==============================
s = input("Enter sentence: ")
print(" ".join(word[::-1] for word in s.split()))

# ==============================
# 8. Find longest word in a sentence
# ==============================
s = input("Enter sentence: ")
words = s.split()
print("Longest word:", max(words, key=len))

# ==============================
# 9. Extract digits from a string
# ==============================
s = input("Enter string: ")
digits = "".join(ch for ch in s if ch.isdigit())
print(digits)

# ==============================
# 10. Remove digits from a string
# ==============================
s = input("Enter string: ")
result = "".join(ch for ch in s if not ch.isdigit())
print(result)

# ==============================
# 11. Convert camelCase to snake_case
# ==============================
s = input("Enter camelCase string: ")
result = ""
for ch in s:
    if ch.isupper():
        result += "_" + ch.lower()
    else:
        result += ch
print(result)

# ==============================
# 12. Count frequency of characters
# ==============================
s = input("Enter string: ")
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
print(freq)

# ==========================================
# 13. Keep only alphanumeric characters
# ==========================================
s = input("Enter a string: ")
result = ""

for ch in s:
    if ch.isalnum():
        result += ch

print("Result:", result)


# ==========================================
# 14. Capitalize first letter of each word
# ==========================================
s = input("Enter a sentence: ")
print(s.title())


# ==========================================
# 15. Replace multiple spaces with single space
# ==========================================
s = input("Enter a sentence: ")
print(" ".join(s.split()))


# ==========================================
# 16. Encode string with ROT13 cipher
# ==========================================
s = input("Enter a string: ")
result = ""

for ch in s:
    if 'a' <= ch <= 'z':
        result += chr((ord(ch) - ord('a') + 13) % 26 + ord('a'))
    elif 'A' <= ch <= 'Z':
        result += chr((ord(ch) - ord('A') + 13) % 26 + ord('A'))
    else:
        result += ch

print("ROT13:", result)


# ==========================================
# 17. Mask a string like a password
# ==========================================
s = input("Enter a string: ")
print("*" * len(s))


# ==========================================
# 18. Add ordinal suffix to number
# ==========================================
n = int(input("Enter a number: "))

if n % 10 == 1 and n % 100 != 11:
    print(str(n) + "st")
elif n % 10 == 2 and n % 100 != 12:
    print(str(n) + "nd")
elif n % 10 == 3 and n % 100 != 13:
    print(str(n) + "rd")
else:
    print(str(n) + "th")


# ==========================================
# 19. Custom trim function
# ==========================================
s = input("Enter a string: ")
print(s.strip())


# ==========================================
# 20. Find common characters in two strings
# ==========================================
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

common = ""

for ch in s1:
    if ch in s2 and ch not in common:
        common += ch

print("Common characters:", common)


# ==========================================
# 21. Convert tab-separated string to list
# ==========================================
s = input("Enter tab-separated values: ")
print(s.split("\t"))


# ==========================================
# 22. Count uppercase and lowercase characters
# ==========================================
s = input("Enter a string: ")

upper = 0
lower = 0

for ch in s:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1

print("Uppercase letters:", upper)
print("Lowercase letters:", lower)


# ==========================================
# 23. Extract email from a string
# ==========================================
text = input("Enter text: ")

words = text.split()

for word in words:
    if "@" in word and "." in word:
        print("Email:", word)


# ==========================================
# 24. Count lines in a multi-line string
# ==========================================
text = input("Enter text (use \\n for new line): ")

lines = text.split("\\n")

print("Number of lines:", len(lines))


# ==========================================
# 25. Escape characters in a string
# ==========================================
s = input("Enter a string: ")
print("Escaped string:")
print(repr(s))


# ==========================================
# 26. Replace multiple substrings
# ==========================================
s = input("Enter a string: ")

s = s.replace("apple", "mango")
s = s.replace("red", "green")
s = s.replace("cat", "dog")
print(s)


# ==========================================
# 27. Parse key-value pairs from string
# ==========================================
s = input("Enter data (name=Ram,age=20): ")

pairs = s.split(",")

for i in pairs:
    print(i)


# 28. Check for balanced parentheses
# ==========================================
s = input("Enter parentheses: ")

count = 0
balanced = True

for ch in s:
    if ch == "(":
        count += 1
    elif ch == ")":
        count -= 1

    if count < 0:
        balanced = False
        break

if count == 0 and balanced:
    print("Balanced")
else:
    print("Not Balanced")

# 29. Remove HTML tags from string
# ==========================================
import re

s = input("Enter HTML string: ")

result = re.sub("<.*?>", "", s)

print("Without HTML tags:", result)


# ==========================================
# 30. Convert numeric string to integer safely
# ==========================================
s = input("Enter a number: ")

if s.isdigit():
    print(int(s))
else:
    print("Invalid Number")


# ==========================================
# 31. Count words starting with vowels
# ==========================================
s = input("Enter a sentence: ")

count = 0

for word in s.split():
    if word[0].lower() in "aeiou":
        count += 1

print(count)


# ==========================================
# 32. Group words by first character
# ==========================================
s = input("Enter words: ")

words = s.split()

for word in words:
    print(word[0], ":", word)


# ==========================================
# 33. Sort string characters
# ==========================================
s = input("Enter a string: ")

print("".join(sorted(s)))


# ==========================================
# 34. Remove nth character
# ==========================================
s = input("Enter a string: ")
n = int(input("Enter index: "))

print(s[:n] + s[n+1:])


# ==========================================
# 35. Remove all whitespaces from string
# ==========================================
s = input("Enter a string: ")

result = ""

for ch in s:
    if ch != " ":
        result += ch

print("Without spaces:", result)



# ==========================================
# 36. Create a string with your name and print it
# ==========================================
name = input("Enter your name: ")
print(name)


# ==========================================
# 37. Print the first character
# ==========================================
name = input("Enter your name: ")
print(name[0])


# ==========================================
# 38. Print the last character
# ==========================================
name = input("Enter your name: ")
print(name[-1])


# ==========================================
# 39. Join two strings
# ==========================================
first = input("Enter first name: ")
last = input("Enter last name: ")

print(first + " " + last)


# ==========================================
# 40. Repeat a string 3 times
# ==========================================
text = input("Enter a string: ")
print(text * 3)


# ==========================================
# 41. Print first 5 characters
# ==========================================
text = input("Enter a string: ")
print(text[:5])


# ==========================================
# 42. Reverse a string
# ==========================================
text = input("Enter a string: ")
print(text[::-1])


# ==========================================
# 43. Check substring
# ==========================================
text = input("Enter a string: ")
sub = input("Enter substring: ")

print(sub in text)


# ==========================================
# 44. Find length of a string
# ==========================================
text = input("Enter a string: ")
print(len(text))


# ==========================================
# 45. Convert to uppercase
# ==========================================
text = input("Enter a string: ")
print(text.upper())


# ==========================================
# 46. Convert to lowercase
# ==========================================
text = input("Enter a string: ")
print(text.lower())


# ==========================================
# 47. Capitalize first letter
# ==========================================
text = input("Enter a string: ")
print(text.capitalize())


# ==========================================
# 48. Convert to title case
# ==========================================
text = input("Enter a sentence: ")
print(text.title())


# ==========================================
# 49. Remove leading spaces
# ==========================================
text = input("Enter a string with spaces: ")
print(text.lstrip())


# ==========================================
# 50. Remove trailing spaces
# ==========================================
text = input("Enter a string with spaces: ")
print(text.rstrip())


# ==========================================
# 51. Remove spaces from both ends
# ==========================================
text = input("Enter a string with spaces: ")
print(text.strip())

# ==========================================
# 52. Replace all spaces with underscores
# ==========================================
s = "hello world python"
print(s.replace(" ", "_"))


# ==========================================
# 53. Count how many times a character appears
# ==========================================
s = "hello world python"
ch = "o"
print(s.count(ch))


# ==========================================
# 54. Find index of a character using find()
# ==========================================
s = "hello world python"
print(s.find("w"))


# ==========================================
# 55. Find last occurrence using rfind()
# ==========================================
s = "hello world python"
print(s.rfind("o"))


# ==========================================
# 56. Find substring position using index()
# ==========================================
s = "hello world python"
print(s.index("world"))


# ==========================================
# 57. Split a string by spaces
# ==========================================
s = "hello world python"
print(s.split())


# ==========================================
# 58. Join a list of words into a string
# ==========================================
words = ["hello", "world", "python"]
print(" ".join(words))


# ==========================================
# 59. Check string starts with Hello
# ==========================================
text = "Hello world"
print(text.startswith("Hello"))


# ==========================================
# 60. Check string ends with python
# ==========================================
s = "hello world python"
print(s.endswith("python"))


# ==========================================
# 61. Check if string is digit
# ==========================================
num = "12345"
print(num.isdigit())


# ==========================================
# 62. Check if string is alphabet
# ==========================================
name = "Aarav"
print(name.isalpha())


# ==========================================
# 63. Check if string is alphanumeric
# ==========================================
value = "Aarav123"
print(value.isalnum())


# ==========================================
# 64. Get ASCII value of character
# ==========================================
ch = "A"
print(ord(ch))


# ==========================================
# 65. Convert ASCII to character
# ==========================================
print(chr(65))


# ==========================================
# 66. Remove punctuation from string
# ==========================================
import string

text = "Hello, world! How are you?"

for ch in string.punctuation:
    text = text.replace(ch, "")

print(text)


# ==========================================
# 67. Swap case of characters
# ==========================================
text = "HeLLo"
print(text.swapcase())


# ==========================================
# 68. Count total words in a string
# ==========================================
s = "hello world python"
print(len(s.split()))


# ==========================================
# 69. Count total sentences in a string
# ==========================================
text = "Hello world. Python is easy! Is it fun?"

count = text.count(".") + text.count("!") + text.count("?")

print(count)


# ==========================================
# 70. Convert string to list of characters
# ==========================================
s = "hello"
print(list(s))