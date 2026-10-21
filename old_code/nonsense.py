"""

file = open("essay.txt", "r")

content = len(file.read())

file.close()

print(content)

"""

file = open("../n/essay.txt", "r")
cara = len(file.read())

file.close()


print(f"The file contains {cara} characters")
