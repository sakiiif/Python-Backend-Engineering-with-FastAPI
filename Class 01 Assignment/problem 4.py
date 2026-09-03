number = input()

# number = number + 5
# print(number)

# error message-> TypeError: can only concatenate str (not "int") to str

# Fixing below:
number = int(number)
number = number + 10

print(number)