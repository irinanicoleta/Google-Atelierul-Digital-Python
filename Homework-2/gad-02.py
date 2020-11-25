# initial list
my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

# sort the list in ascending order
ordered_list = my_list.copy()
ordered_list.sort()
print(ordered_list)

# sort the list in descending order
ordered_list = my_list.copy()
ordered_list.sort()
ordered_list.reverse()
print(ordered_list)

# show even numbers from list
ordered_list.reverse()
length = len(ordered_list)
print(ordered_list[0:length:2])

# show odd numbers from list
length = len(ordered_list)
print(ordered_list[1:length:2])

# show multiples of 3 from list
multiples = []
for i in range(length):
    if ordered_list[i] % 3 == 0:
        multiples.append(ordered_list[i])
print(multiples)
