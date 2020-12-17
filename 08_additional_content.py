# list_of_numbers = []
loops = 5

# for i in range(loops):
#     if not i % 2:
#         list_of_numbers.append(i)
#     else:
#         list_of_numbers.append(-1)

# list_of_numbers = [i if not i % 2 else -1
#                    for i in range(loops)]

list_of_numbers = [i for i in range(loops) if not i % 2]

print(list_of_numbers)

# {true} if {condition} else {false}

a = 0
b = 1

# if b:
#     a = b
# else:
#     a = -1

a = b if b else -1
