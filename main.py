import bisect
import datetime
from random import randint
import timeit

sorted_list = []
sorted_reverse_list = []
random_list = []


def prepare_data(n):
    global sorted_list, sorted_reverse_list, random_list
    for i in range(n):
        liczba = randint(1, n * 100)
        random_list.append(liczba)
        bisect.insort(sorted_list, liczba)
        sorted_reverse_list = sorted_list[::-1]


def bubble_sort_1(list_to_sort):
    for lap in range(len(list_to_sort)):
        for i in range(len(list_to_sort) - 1):
            if list_to_sort[i + 1] < list_to_sort[i]:
                temp = list_to_sort[i]
                list_to_sort[i] = list_to_sort[i + 1]
                list_to_sort[i + 1] = temp


def bubble_sort_2(list_to_sort):
    laps = len(list_to_sort)
    nums = len(list_to_sort) - 1
    for lap in range(laps):
        for i in range(nums):
            if list_to_sort[i + 1] < list_to_sort[i]:
                temp = list_to_sort[i]
                list_to_sort[i] = list_to_sort[i + 1]
                list_to_sort[i + 1] = temp
        nums -= 1


def sorting_test(name_of_sort_function, n, ilosc_testow=100):
    print(f'Sortowanie listy {n} liczb za pomocą: {name_of_sort_function}')
    setup = f"""
from __main__ import prepare_data, {name_of_sort_function}
sorted_list = []
sorted_reverse_list = []
random_list = []
prepare_data({n})
"""

    statement1 = f"""
{name_of_sort_function}(sorted_list)    
"""
    statement2 = f"""
{name_of_sort_function}(sorted_reverse_list)    
"""
    statement3 = f"""
{name_of_sort_function}(random_list)    
"""
    t1 = timeit.timeit(stmt=statement1, setup=setup, number=ilosc_testow)
    t2 = timeit.timeit(stmt=statement2, setup=setup, number=ilosc_testow)
    t3 = timeit.timeit(stmt=statement3, setup=setup, number=ilosc_testow)
    print('Sortowanie posortowanej listy: ', t1 / ilosc_testow)
    print('Sortowanie posortowanej odwrotnie listy: ', t2 / ilosc_testow)
    print('Sortowanie nieposortowanej listy: ', t3 / ilosc_testow)
    print()


if __name__ == '__main__':
    sorting_test('bubble_sort_1', 10000)
    sorting_test('bubble_sort_2', 10000)
