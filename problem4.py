x = int(input())
inputed_data = []
number_list = []
list_of_number_list = []
for i in range(x):
    inputed_data.append(int(input()))
for i in inputed_data:
    for z in range(1, i + 1):
        if i % z == 0:
            number_list.append(str(z))
        
    
    list_of_number_list.append(number_list)
    number_list = []


for i in list_of_number_list:
    case_number = list_of_number_list.index(i) + 1
    x  = " ".join(i)
    
    print(f"Case {case_number}: {x}")
