price = float(input())
quantity = int(input())

total_amount = price * quantity
tax = total_amount * 0.05
final_amount = total_amount + tax

print(total_amount)
print(final_amount)