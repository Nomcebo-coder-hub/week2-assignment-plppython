my_list = [10, 20, 30, 40]
print(my_list)

my_list.append(15)
print("After Append:" , my_list)

my_list = [10, 20, 30, 40]
print("List1:" , my_list)

even_numbers = [50, 60, 70]
print("List2:" , even_numbers)

my_list.extend(even_numbers)

print("List after append:" , my_list)

my_list = [10, 20, 30, 40]
del my_list[3]
print(my_list)