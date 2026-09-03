numbers = list(map(int, input().split()))

if numbers == sorted(numbers):
    print("Sorted")
else:
    print("Not sorted")