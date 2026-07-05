"""file = open("Data.txt", "w")
file.write("This is a new line of text.\n")
file.close()"""



"""file = open("Data.txt", "r")
print(file.read())"""

file = open("Data.txt", "a")
file.write("This is an appended line of text.\n")
file = open("Data.txt", "r")
print(file.read())
file.close()

