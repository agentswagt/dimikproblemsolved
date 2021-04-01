###input taking mechanism###
number_of_numberspair = int(input())
list_of_numbers_pair = []
for i in range(number_of_numberspair):
    numbers_list = []
    number1, number2 = input().split()
    numbers_list.append(number1)
    numbers_list.append(number2)
    print(numbers_list)
    list_of_numbers_pair.append(numbers_list)
    numbers_list = []
print(list_of_numbers_pair)
###------------------------------###
prime_list = []
multi_list = []
for num in range(1, 20 + 1):  
   if num > 1:  
       for i in range(2,num):  
           if (num % i) == 0:  
               break  
       else:  
           for f in range(5):
                prime_list.append(num)
           
print(prime_list)
for xx in list_of_numbers_pair:
    number_list = xx
    print(number_list)
    for i in number_list:
        for z in prime_list:
            multi_list.append(int(i)*z)
    print(multi_list)
    final_list = list(set(multi_list))
    print(final_list)
    remove_list = []
    for i in final_list:
        if i % int(number_list[0]) == 0 and i % int(number_list[1]) == 0:
            remove_list.append(i)
    print(remove_list)


    remove_list.sort()

    print(remove_list)
    print(f"This is the value: {remove_list[0]}")

    