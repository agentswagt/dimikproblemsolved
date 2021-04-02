x = int(input())
inputed_data = []
number_list = []
list_of_number_list = []
for i in range(x):
    inputed_data.append(input())

for i in inputed_data:
    number_list = i.split()
    a, b, c = int(number_list[0]), int(number_list[1]), int(number_list[2])
    if a < b and a < c:
        number_list[0] = a
        if b < c:
            number_list[1] = b
            number_list[2] = c
        else:
            number_list[2] = b
            number_list[1] = c

    if b < a and b < c:
        number_list[0] = b
        if a < c:
            number_list[1] = a
            number_list[2] = c
        else:
            number_list[2] = a
            number_list[1] = c
    if c < b and c < a:
        number_list[0] = c
        if a < b:
            number_list[1] = a
            number_list[2] = b
        else:
            number_list[2] = a
            number_list[1] = b
    list_of_number_list.append(number_list)
    number_list = []
for i in list_of_number_list:
    case_counter = list_of_number_list.index(i) + 1 
    print(f"Case {case_counter}: {i}")

    

    