input_list1 = [1, 2, 2, 3, 3, 4, 5, 5]
input_list2 = [5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6]

# append()
input_list1.append(10)
print("append:", input_list1)

# insert()
input_list1.insert(2, 99)
print("insert:", input_list1)

# extend()
input_list1.extend(input_list2)
print("extend:", input_list1)

# remove()
input_list1.remove(99)
print("remove:", input_list1)

# pop()
removed_item = input_list1.pop()
print("pop:", input_list1)
print("removed item:", removed_item)

# sort()
input_list1.sort()
print("sort:", input_list1)

# reverse()
input_list1.reverse()
print("reverse:", input_list1)

# count(x)
print("count of 5:", input_list1.count(5))

# index(x)
print("index of 5:", input_list1.index(5))