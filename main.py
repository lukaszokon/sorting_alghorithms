import bisect
import datetime
from random import randint
import timeit


# sorted_list = []
# sorted_reverse_list = []
# random_list = []


def prepare_data(n):
    sorted_list = []
    sorted_reverse_list = []
    random_list = []
    for i in range(n):
        liczba = randint(1, n * 100)
        random_list.append(liczba)
        bisect.insort(sorted_list, liczba)
        sorted_reverse_list = sorted_list[::-1]
    return sorted_list, sorted_reverse_list, random_list


def bubble_sort_1(list_to_sort):
    for lap in range(len(list_to_sort)):
        for i in range(len(list_to_sort) - 1):
            if list_to_sort[i + 1] < list_to_sort[i]:
                temp = list_to_sort[i]
                list_to_sort[i] = list_to_sort[i + 1]
                list_to_sort[i + 1] = temp


def bubble_sort_2(list_to_sort):
    laps = len(list_to_sort)
    nums = laps - 1
    for lap in range(laps):
        for i in range(nums):
            if list_to_sort[i + 1] < list_to_sort[i]:
                temp = list_to_sort[i]
                list_to_sort[i] = list_to_sort[i + 1]
                list_to_sort[i + 1] = temp
        nums -= 1


def bubble_sort_3(list_to_sort):
    laps = len(list_to_sort)
    nums = laps - 1
    for lap in range(laps):
        was_change = False
        for i in range(nums):
            if list_to_sort[i + 1] < list_to_sort[i]:
                temp = list_to_sort[i]
                list_to_sort[i] = list_to_sort[i + 1]
                list_to_sort[i + 1] = temp
                was_change = True
        if not was_change:
            return
        nums -= 1


def bubble_sort_4(list_to_sort):
    laps = len(list_to_sort)
    nums = laps - 1
    start_index = 0
    for lap in range(laps):
        was_change = False
        for i in range(start_index, nums):
            if list_to_sort[i + 1] < list_to_sort[i]:
                temp = list_to_sort[i]
                list_to_sort[i] = list_to_sort[i + 1]
                list_to_sort[i + 1] = temp
                if not was_change:
                    was_change = True
                    start_index = i - 1
                    if start_index < 0:
                        start_index = 0
        if not was_change:
            return
        nums -= 1


def insert_sort(list_to_sort):
    nums = len(list_to_sort)
    for i in range(1, nums):
        value = list_to_sort[i]
        before_index = i - 1
        while before_index >= 0 and value < list_to_sort[before_index]:
            list_to_sort[before_index + 1] = list_to_sort[before_index]
            before_index -= 1
        list_to_sort[before_index + 1] = value


def sorting_test(name_of_sort_function, n, ilosc_testow=100):
    print(f'Sortowanie listy {n} liczb za pomocą: {name_of_sort_function}')
    setup = f"""
from __main__ import prepare_data, {name_of_sort_function}
"""

    statement1 = f"""
sorted_list, sorted_reverse_list, random_list = prepare_data({n})
{name_of_sort_function}(sorted_list)   
"""
    statement2 = f"""
sorted_list, sorted_reverse_list, random_list = prepare_data({n})
{name_of_sort_function}(sorted_reverse_list)    
"""
    statement3 = f"""
sorted_list, sorted_reverse_list, random_list = prepare_data({n})
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
    # sorting_test('bubble_sort_1', 1000, 10)
    # sorting_test('bubble_sort_2', 1000, 10)
    # sorting_test('bubble_sort_3', 1000, 10)
    sorting_test('bubble_sort_4', 1000, 10)
    sorting_test('insert_sort', 1000, 10)
