x = int(input())
inputed_data = []
number_list = []
list_of_number_list = []
for i in range(x):
    inputed_data.append(input())

for i in inputed_data:
    number_list = i.split()
    a, b, c = number_list[0], number_list[1], number_list[2]
    if a >= b and a >= c:
        a = number_list[0]
    

    

    