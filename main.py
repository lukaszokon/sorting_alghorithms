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


def select_sort(list_to_sort):
    numbers = len(list_to_sort)
    for i in range(numbers):
        for j in range(i, numbers):
            if list_to_sort[i] > list_to_sort[j]:
                list_to_sort[i], list_to_sort[j] = list_to_sort[j], list_to_sort[i]


def merge_sort_prepare(list_to_sort):
    number_of_nums = len(list_to_sort)
    temp = [None] * number_of_nums
    merge_sort(0, number_of_nums - 1, list_to_sort, temp)


def merge_sort(start_index, end_index, list_to_sort, temp_list):
    middle_index = (start_index + end_index + 1) // 2

    if middle_index - start_index > 1:
        merge_sort(start_index, middle_index - 1, list_to_sort, temp_list)

    if end_index - middle_index > 0:
        merge_sort(middle_index, end_index, list_to_sort, temp_list)
    first_iterator = start_index
    second_iterator = middle_index

    for i in range(start_index, end_index + 1):

        if (first_iterator == middle_index) or (
                (second_iterator <= end_index
                ) and list_to_sort[first_iterator] > list_to_sort[second_iterator]):
            temp_list[i] = list_to_sort[second_iterator]
            second_iterator += 1
        else:
            temp_list[i] = list_to_sort[first_iterator]
            first_iterator += 1

    for i in range(start_index, end_index + 1):
        list_to_sort[i] = temp_list[i]


def prepare_quick_sort(list_to_sort):
    quick_sort(0, len(list_to_sort) - 1, list_to_sort)


def default_sort_function(list_to_sort):
    list_to_sort.sort()


def quick_sort(left_index, right_index, list_to_sort):
    if right_index <= left_index:
        return

    i = left_index
    j = right_index
    pivot = list_to_sort[(left_index + right_index) // 2]

    while True:
        while pivot > list_to_sort[i]:
            i += 1
        while pivot < list_to_sort[j]:
            j -= 1
        if i <= j:
            list_to_sort[i], list_to_sort[j] = list_to_sort[j], list_to_sort[i]
            i += 1
            j -= 1
        else:
            break
    if j > left_index:
        quick_sort(left_index, j, list_to_sort)
    if i < right_index:
        quick_sort(i, right_index, list_to_sort)


import multiprocessing


def prepare_multiprocessing_quick_sort(list_to_sort):
    multiprocessing_quick_sort(0, len(list_to_sort) - 1, list_to_sort, 2, 0)


def multiprocessing_quick_sort(left_index, right_index, list_to_sort, depth, threads_created):
    if right_index <= left_index:
        return

    i = left_index
    j = right_index
    pivot = list_to_sort[(left_index + right_index) // 2]

    while True:
        while pivot > list_to_sort[i]:
            i += 1
        while pivot < list_to_sort[j]:
            j -= 1
        if i <= j:
            list_to_sort[i], list_to_sort[j] = list_to_sort[j], list_to_sort[i]
            i += 1
            j -= 1
        else:
            break

    process_1 = None
    process_2 = None

    if j > left_index:
        if threads_created < depth:
            process_1 = multiprocessing.Process(target=multiprocessing_quick_sort,
                                                args=(left_index, j, list_to_sort, depth, threads_created + 1))
            process_1.start()
        else:
            multiprocessing_quick_sort(left_index, j, list_to_sort, depth, threads_created)
    if i < right_index:
        if threads_created < depth:
            process_2 = multiprocessing.Process(target=multiprocessing_quick_sort,
                                                args=(i, right_index, list_to_sort, depth, threads_created + 1))
            process_2.start()
        else:
            multiprocessing_quick_sort(i, right_index, list_to_sort, depth, threads_created)
    if process_1:
        process_1.join()
    if process_2:
        process_2.join()


from heapq import heappush, heappop


def heapsort(list_to_sort):
    h = []
    for value in list_to_sort:
        heappush(h, value)
    list_to_sort.clear()
    for i in range(len(h)):
        list_to_sort.append(heappop(h))


def sorting_test(name_of_sort_function, n, ilosc_testow=100):
    print(f'Sortowanie listy {n} liczb za pomoc??: {name_of_sort_function}')
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


def cezar_cipher(string_to_code, step):
    alphabet = 'a??bc??de??fghijkl??mn??o??prs??tuwxyz????'
    alphabet_n = len(alphabet)
    alphabet_upper = alphabet.upper()
    numeric = '0123456789'
    numeric_n = len(numeric)

    new_string = ''
    for letter in string_to_code:
        if letter.isalpha():
            if letter.isupper():
                index = alphabet_upper.index(letter)
                new_string += alphabet[(index + step) % alphabet_n]
            else:
                index = alphabet.index(letter)
                new_string += alphabet_upper[(index + step) % alphabet_n]
        elif letter.isdigit():
            index = numeric.index(letter)
            new_string += numeric[(index + step) % numeric_n]
        else:
            new_string += letter

    return new_string


def cezar_decipher(string_to_code, step):
    new_string = cezar_cipher(string_to_code, -step)
    return new_string


if __name__ == '__main__':
    text = cezar_cipher('Ala mia??a kota, ale ju?? go nie ma niestety. Za to ma 3 psy.', 3)
    print(text)
    text = cezar_decipher(text, 3)
    print(text)
    # lista = [5, 6, 3, 4, 5, 3, 11, 9]
    # prepare_multiprocessing_quick_sort(lista)
    # print(lista)
    # sorting_test('bubble_sort_1', 1000, 10)
    # sorting_test('bubble_sort_2', 1000, 10)
    # sorting_test('bubble_sort_3', 1000, 10)
    # sorting_test('bubble_sort_4', 1000, 10)
    # sorting_test('insert_sort', 1000, 10)
    # sorting_test('default_sort_function', 1000, 100)
    # sorting_test('merge_sort_prepare', 1000, 100)
    # sorting_test('select_sort', 1000, 10)
    # sorting_test('prepare_quick_sort', 10000, 1)
    # sorting_test('heapsort', 1000, 100)
    # sorting_test('prepare_multiprocessing_quick_sort', 100000, 1)
