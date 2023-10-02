ex1 = input("Write your sentences")

ex1_tuple = tuple(ex1)

print(ex1_tuple)

ex2 = ('T', 'h', 'e', 'B', 'i', 'g', 'B', 'e', 'n')

ex2_result = ''.join(ex2)

print(ex2_result)

ex3_tuple_a = (1, 2, 3, 4, 5, 6, 7)
ex3_tuple_b = (5, 6, 7, 9, 7, 1, 10, 10)

ex3_mid = len(ex3_tuple_a) // 2

result_tuple = ex3_tuple_a[:ex3_mid] + ex3_tuple_b[ex3_mid:]

print(result_tuple)

ex4_one = input("Write your elements ")

element_count = {}

for element in ex4_one:
    if element in element_count:
        element_count[element] += 1
    else:
        element_count[element] = 1

result_tuple_ex4 = tuple((key, value) for key, value in element_count.items())

print(result_tuple_ex4)

ex5 = (55, 6, 777, 70.0, '7', 'A')

result_tuple_ex5 = []

current_data = type(ex5[0])

current_tuple = []

for item in ex5:
    ex5_type = type(item)

    if ex5_type != current_data:
        result_tuple_ex5.append(tuple(current_tuple))
        current_tuple = []
        current_data = ex5_type

    current_tuple.append(item)

if current_tuple:
    result_tuple_ex5.append(tuple(current_tuple))

for t in result_tuple_ex5:
    print(t)

user_result = input("Enter your string")

char_set = {char for char in user_result}

print(char_set)

setA = {1, 2, 3, 4, 5}

setB = {5, 7, 8, 9, 2, 10}

dif_set = setA - setB

print(dif_set)

#########
set_A_ex = {1, 2, 3, 4, 5}
set_B_ex = {5, 7, 8, 9, 2, 10}

set_A_ex.difference_update(set_B_ex)

print(set_A_ex)

######
set_ex = {1, 2, 3, 4, 7}
set_ex1 = {8, 7, 9, 4, 2, 0, 10}
set_ex2 = {4, 0, 1}

for element in set_ex.copy():
    if element in set_ex2:
        set_ex.remove(element)
        set_ex1.add(element)

set_ex2.update(set_ex, set_ex2)

print("Updated set_ex2 =", set_ex2)

#####
from itertools import combinations

A = {1, 2, 3, 4, 5, 6}
n = 3
m = 5

list_of_sets = []

for combo in combinations(A, n):
    list_of_sets.append(set(combo))
    if len(list_of_sets) == m:
        break

print(list_of_sets)
####
from itertools import groupby

cars_list = [('BMW', 'X6'), ('Toyota', 'Yaris'), ('Fiat', '500'), ('Fiat', 'Panda'), ('Toyota', 'Camry 30')]

cars_list.sort(key=lambda x: x[0])

for manufacturer, group in groupby(cars_list, key=lambda x: x[0]):

    count = len(list(group))

    print(manufacturer, count)

    for model in group:
        print(f"- {model[1]}")

################################
