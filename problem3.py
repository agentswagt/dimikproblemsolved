x = 1000
number_list = []
while x > 0:
    number_list.append(x)
    
    x = x - 1
for i in number_list:
    if number_list.index(i) % 5 == 0:
        print("\n")
    print(i, end=" ")

print("completed boss")