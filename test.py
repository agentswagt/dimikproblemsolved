number1 = 105
number2 = 15
#making prime numbers list
number_list = [number1, number2]
prime_list = []
multi_list = []
###Prime List ####
for num in range(1, 20 + 1):  
   if num > 1:  
       for i in range(2,num):  
           if (num % i) == 0:  
               break  
       else:  
           for f in range(5):
                prime_list.append(num)
           
print(prime_list)

for i in number_list:
    for z in prime_list:
        multi_list.append(i*z)
print(multi_list)
final_list = list(set(multi_list))
print(final_list)
remove_list = []
for i in final_list:
    if i % number1 == 0 and i % number2 == 0:
        remove_list.append(i)
print(remove_list)


remove_list.sort()

print(remove_list)
print(f"This is the value: {remove_list[0]}")
