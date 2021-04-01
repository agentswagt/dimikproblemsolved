x = int(input())
inputed_data = []
number_list = []
list_of_number_list = []
for i in range(x):
    inputed_data.append(int(input()))
for i in inputed_data:
    for z in str(i):
        number_list.append(int(z))
    print("Sum = {}".format(number_list[0] + number_list[4]))
    number_list = []