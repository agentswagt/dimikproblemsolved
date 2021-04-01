x = int(input())
inputed_data = []
for i in range(x):
    inputed_data.append(int(input()))
for i in inputed_data:
    if i % 2 == 0:
        print("even")
    else:
        print("odd")
    
