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
