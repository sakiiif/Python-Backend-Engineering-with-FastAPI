age = int(input())
is_citizen = input() == "True"

if age >= 18 and is_citizen:
    print("Can vote")
else:
    print("Cannot vote")