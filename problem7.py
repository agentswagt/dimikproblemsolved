x = int(input())
inputed_data = []
number_list = []
list_of_number_list = []
for i in range(x):
    inputed_data.append(input())
for i in inputed_data:
    x = i.split()
    print(len(x))
