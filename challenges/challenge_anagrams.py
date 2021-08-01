from typing import Counter


"""Although to run a serious benchmark the machine should run ONLY the program,
the execution times commented bellow might represent
a comparison of those algorithms"""


#  0.121676 ~ 0.122801 seconds
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

# 0.147181 ~  0.15807
def generate_counter_dict(first_str, second_str):
    return gen_dict(list(first_str)) == gen_dict(list(second_str))

# 0.147181 ~  0.15807
def gen_dict(lista):
    dic = {}

    for letra in lista:
        if letra in dic:
            dic[letra] += 1
        else:
            dic[letra] = 1

    return dic

# 0.165924 ~ 0.168763 seconds
def recursive_dict(first_str, second_str):
    return str_to_dict_recusrsive(first_str, {}) == str_to_dict_recusrsive(second_str, {})
# 0.165924 ~ 0.168763 seconds
def str_to_dict_recusrsive(string, str_dict={}):
    if len(string) == 0:
        return str_dict
    str_dict[string[0]] = string.count(string[0])
    return str_to_dict_recusrsive(string.replace(string[0], ''), str_dict)


# 0.163752 ~ 0.184378
def slow_gen_counter_dict(first_string, second_string):
    return slow_str_to_dict(list(first_string)) == slow_str_to_dict(list(second_string))
# 0.163752 ~ 0.184378
def slow_str_to_dict(lista):
    dic = {letra: 0 for letra in lista}

    for letra in lista:
        dic[letra] += 1

    return dic

#  0.21519 ~ 0.21801 seconds
def remove_chars(first_string, second_string):
    for letter in first_string:
        try:
            index = second_string.index(letter)
        except ValueError:
            return False

        second_string = second_string[:index] + second_string[index + 1:]

    return True


# 0.375300 ~ 0.386072 seconds
def slow_dict(f_str, s_str):
    first_dict = {i: f_str.count(i) for i in f_str}
    second_dict = {a: s_str.count(a) for a in s_str}
    return first_dict == second_dict


# 2.41763 ~ 2.47492 seconds
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
# 2.41763 ~ 2.47492 seconds
def quicksort_str(array, low, high):
    # https://github.com/tryber/sd-07-project-algorithms/tree/luciano-berchon-project-algorithms
    if len(array) == 1:
        return array

    if low < high:
        partition_index = partition(array, low, high)

        quicksort_str(array, low, partition_index - 1)
        quicksort_str(array, partition_index + 1, high)

    return array



# 3.419441 seconds complexity O(nlog(n))
def heapify(str_list, heap_size, root_index):
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    if left_child < heap_size and str_list[left_child] > str_list[largest]:
        largest = left_child

    if right_child < heap_size and str_list[right_child] > str_list[largest]:
        largest = right_child

    if largest != root_index:
        str_list[root_index], str_list[largest] = str_list[largest], str_list[root_index]
        heapify(str_list, heap_size, largest)
def heap_st(string):
    n = len(string)
    str_list = list(string)

    for i in range(n, -1, -1):
        heapify(str_list, n, i)

    for i in range(n - 1, 0, -1):
        str_list[i], str_list[0] = str_list[0], str_list[i]
        heapify(str_list, i, 0)
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
# 5.4131 seconds  complexity O(n^2)
def insertion_sort(first_string, second_string):
    return insertion_s(list(first_string)) == insertion_s(list(second_string))


def selection_sort(first_string, second_string):
    return selection_sort_str(first_string) == selection_sort_str(second_string)
# 5.7930 ~ 5.82011 seconds complexity O(n^2)
def selection_sort_str(string):
    str_list = list(string)
    for i in range(len(str_list)):
        min_index = i
        for j in range(i + 1, len(str_list)):
            if str_list[min_index] > str_list[j]:
                min_index = j
        str_list[i], str_list[min_index] = str_list[min_index], str_list[i]
    return str_list



# 14.596026 seconds
def b_sort(nums):
    # We set swapped to True so the loop looks runs at least once
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                # Swap the elements
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Set the flag to True so we'll loop again
                swapped = True
# 14.596026 seconds complexity O(n^2)
def bubble_sort(first_string, second_string):
    return b_sort(list(first_string)) == b_sort(list(second_string))

def is_anagram(first_string, second_string):
    if (
        not isinstance(first_string, str)
        or not isinstance(second_string, str)
        or len(first_string) != len(second_string)
    ):
        return False

    # Counter py method turned to be the fastest - I am not surprised at all
    # 0.076248 ~ 0.09043 seconds
    return Counter(first_string) == Counter(second_string)


# first_string = (
#         "Lorem ipsum dolor sit amer, consectetur "
#         "adipiscing elit, do sed eiusmod tempor "
#         "incididint ut labore et dolore magna aliqua"
#     )
# bucket_sort(first_string, first_string)
