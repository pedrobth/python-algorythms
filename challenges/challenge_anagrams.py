from typing import Counter


"""Although to run a serious benchmark the machine should run ONLY the program,
the execution times commented bellow - for a lorem text with  might represent
a comparison of those algorithms"""


def remove_chars_list(first_string, second_string):
    # https://github.com/tryber/sd-07-project-algorithms/tree/MoisesSantana-Algorithms
    first_list = list(first_string)
    second_list = list(second_string)
    for letter in first_list:
        try:
            index = second_list.index(letter)
        except ValueError:
            return False

        second_list.remove(second_list[index])

    return True


def generate_counter_dict(first_str, second_str):
    return gen_dict(list(first_str)) == gen_dict(list(second_str))


def gen_dict(lista):
    dic = {}

    for letra in lista:
        if letra in dic:
            dic[letra] += 1
        else:
            dic[letra] = 1

    return dic


def recursive_dict(first_str, second_str):
    return str_to_dict_recusrsive(
        first_str, {}
    ) == str_to_dict_recusrsive(second_str, {})


def str_to_dict_recusrsive(string, str_dict={}):
    if len(string) == 0:
        return str_dict
    str_dict[string[0]] = string.count(string[0])
    return str_to_dict_recusrsive(string.replace(string[0], ''), str_dict)


def slow_gen_counter_dict(first_string, second_string):
    return slow_str_to_dict(list(
        first_string
    )) == slow_str_to_dict(list(second_string))


def slow_str_to_dict(lista):
    dic = {letra: 0 for letra in lista}

    for letra in lista:
        dic[letra] += 1

    return dic


def remove_chars(first_string, second_string):
    for letter in first_string:
        try:
            index = second_string.index(letter)
        except ValueError:
            return False

        second_string = second_string[:index] + second_string[index + 1:]

    return True


def slow_dict(f_str, s_str):
    first_dict = {i: f_str.count(i) for i in f_str}
    second_dict = {a: s_str.count(a) for a in s_str}
    return first_dict == second_dict


# complexity O(n log n)
def quicksort(first_string, second_string):
    return quicksort_str(
        list(first_string), 0, len(first_string) - 1
    ) == quicksort_str(
        list(second_string), 0, len(second_string) - 1
    )


# pivot for quicksort
def partition(array, low, high):
    # https://github.com/tryber/sd-07-project-algorithms/tree/luciano-berchon-project-algorithms
    i = low - 1
    pivot = array[high]

    for j in range(low, high):

        if array[j] <= pivot:

            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]

    return i + 1


def quicksort_str(array, low, high):
    # https://github.com/tryber/sd-07-project-algorithms/tree/luciano-berchon-project-algorithms
    if len(array) == 1:
        return array

    if low < high:
        partition_index = partition(array, low, high)

        quicksort_str(array, low, partition_index - 1)
        quicksort_str(array, partition_index + 1, high)

    return array


def merge(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0

    left_list_length, right_list_length = len(left_list), len(right_list)

    for _ in range(left_list_length + right_list_length):
        if (
            left_list_index < left_list_length
            and right_list_index < right_list_length
        ):
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1

        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1

    return sorted_list


def m_sort(string):
    if len(string) <= 1:
        return string

    mid = len(string) // 2

    left_list = m_sort(string[:mid])
    right_list = m_sort(string[mid:])

    return merge(left_list, right_list)


# complexity O(n log(n))
def merge_sort(first_string, second_string):
    return m_sort(list(first_string)) == m_sort(list(second_string))


# complexity O(n log(n))
def heapify(str_list, heap_size, r_index):
    limit = r_index
    left_child = (2 * r_index) + 1
    right_child = (2 * r_index) + 2

    if left_child < heap_size and str_list[left_child] > str_list[limit]:
        limit = left_child

    if right_child < heap_size and str_list[right_child] > str_list[limit]:
        limit = right_child

    if limit != r_index:
        str_list[r_index], str_list[limit] = str_list[limit], str_list[r_index]
        heapify(str_list, heap_size, limit)


def heap_st(string):
    n = len(string)
    str_list = list(string)

    for i in range(n, -1, -1):
        heapify(str_list, n, i)

    for i in range(n - 1, 0, -1):
        str_list[i], str_list[0] = str_list[0], str_list[i]
        heapify(str_list, i, 0)


# complexity O(n log(n))
def heap_sort(first_string, second_string):
    return heap_st(first_string) == heap_st(second_string)


def insertion_s(x):
    for i in range(1, len(x)):
        item_to_insert = x[i]
        j = i - 1
        while j >= 0 and x[j] > item_to_insert:
            x[j + 1] = x[j]
            j -= 1
        x[j + 1] = item_to_insert


# complexity O(n^2)
def insertion_sort(first_string, second_string):
    return insertion_s(list(first_string)) == insertion_s(list(second_string))


# complexity O(n^2)
def selection_sort(first_str, second_str):
    return selection_sort_str(first_str) == selection_sort_str(second_str)


def selection_sort_str(string):
    str_list = list(string)
    for i in range(len(str_list)):
        min_index = i
        for j in range(i + 1, len(str_list)):
            if str_list[min_index] > str_list[j]:
                min_index = j
        str_list[i], str_list[min_index] = str_list[min_index], str_list[i]
    return str_list


def dec_b_sort(string):
    s_list = list(string)
    for index in range(len(s_list) - 1, 0, -1):
        for s in range(index):
            if s_list[s] > s_list[s + 1]:
                s_list[s], s_list[s + 1] = s_list[s + 1], s_list[s]
    return s_list


# complexity O(n^2)
def dec_bubble_sort(first_string, second_string):
    return dec_b_sort(first_string) == dec_b_sort(second_string)


def b_sort(string):
    # We set swapped to True so the loop looks runs at least once
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(string) - 1):
            if string[i] > string[i + 1]:
                # Swap the elements
                string[i], string[i + 1] = string[i + 1], string[i]
                # Set the flag to True so we'll loop again
                swapped = True


# complexity O(n^2)
def bubble_sort(first_string, second_string):
    return b_sort(list(first_string)) == b_sort(list(second_string))


# tim sort https://en.wikipedia.org/wiki/Timsort complexity O(n log n)
def py_sort(f_str, s_str):
    return list(f_str).sort() == list(s_str).sort()


def is_anagram(first_string, second_string):
    # if (
    #     not isinstance(first_string, str)
    #     or not isinstance(second_string, str)
    #     or len(first_string) != len(second_string)
    # ):
    #     return False

    # Counter py method turned to be the fastest - I am not surprised at all
    return Counter(first_string) == Counter(second_string)
