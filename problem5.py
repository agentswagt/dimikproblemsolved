x = int(input())
inputed_data = []
number_list = []
list_of_number_list = []
for i in range(x):
    inputed_data.append(int(input()))
symbol = "*"
for i in inputed_data:
    for z in range(i):
        print(i * symbol)
    print("\n")
