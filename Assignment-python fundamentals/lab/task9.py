# Program to demonstrate string slicing

text = "PythonProgramming"

print("Original String:", text)

print("First 6 characters:", text[:6])
print("From index 6 to end:", text[6:])
print("Characters from index 1 to 10:", text[1:10])
print("Every second character:", text[::2])
print("Reverse string:", text[::-1])

# Program to demonstrate various string methods

text = "  Hello Python Programming  "

print("Strip:", text.strip())

print("Uppercase:", text.upper())

print("Lowercase:", text.lower())

print("Replace:", text.replace("Python", "Java"))

print("Find 'Python':", text.find("Python"))

print("Split:", text.split())
