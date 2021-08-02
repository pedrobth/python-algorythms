from challenges.challenge_anagrams import bubble_sort, insertion_sort, is_anagram, remove_chars_list, generate_counter_dict, recursive_dict, slow_gen_counter_dict, remove_chars, slow_dict, heap_sort, quicksort, selection_sort, merge_sort, dec_bubble_sort
import timeit
import pprint

def gen_setup(method_to_test):
    return f"from challenges.challenge_anagrams import {method_to_test}"

def get_exec_time(method, first_string, second_string):
    return timeit.timeit(
        f'{method}("{first_string}", "{second_string}")',
        setup=f'{gen_setup(method)}',
        number=1000,
    )

all_test_algorithm_sum = {}
def handle_loops(first_str, second_str):
    methods_list = ("is_anagram", "remove_chars_list", "generate_counter_dict", "recursive_dict", "slow_gen_counter_dict","remove_chars", "slow_dict", "heap_sort", "bubble_sort", "insertion_sort", "quicksort", "merge_sort", "selection_sort", "dec_bubble_sort")
    times_dict = {}
    for method in methods_list:
        times_dict[method] = get_exec_time(method, first_str, second_str)
    times_sorted = sorted(times_dict.items(), key=lambda x: x[1])
    for t in times_sorted:
        print(f"time execution for {t[0] : >30}:   {t[1] :>5}")
        if t[0] in all_test_algorithm_sum:
            all_test_algorithm_sum.update({t[0]:  all_test_algorithm_sum[t[0]] + t[1]})
        else:
            all_test_algorithm_sum[t[0]] = t[1]

def test_compare_times():

    lorem_one_thirty_two = "Lorem ipsum dolor sit amer, consectetur adipiscing elit, do sed eiusmod tempor incididint ut labore et dolore magna aliqua"

    lorem_o_t_t = "do sed eiusmod tempor incididint ut labore et dolore magna aliqua Lorem ipsum dolor sit amer, consectetur adipiscing elit,"

    print(f'\n anagram check, two identical strings:\n"Lorem ipsum dolor sit amer, consectetur adipiscing elit, do sed eiusmod tempor incididint ut labore et dolore magna aliqua"\n algorithm comparison execution times are:')

    handle_loops(lorem_one_thirty_two, lorem_o_t_t)
    
    all_chars_once = "the quick brown fox jumps over the lazy dog"
    a_chars_o = "god yzal eht revo spmuj xof nworb kciuq eht"
    print(f'\nanagram check, two anagrams strings:\n"the quick brown fox jump over the lazy dog"\n algorithm comparison execution times are:')
    handle_loops(all_chars_once, a_chars_o)

    short_string = 'evil'
    short_str_anagram = 'vile'
    print(f'\nanagram check, two short anagrams strings:\n"evil | vile"\n algorithm comparison execution times are:')
    handle_loops(short_str_anagram, short_string)

    short_not_anagram = 'not anagram'
    short_n_angr = 'not anagran'
    print(f'\n "not anagram" compared to "not anagraN" algorithm comparison execution times are:')
    handle_loops(short_not_anagram, short_n_angr)

    lorem_fail = "Lorem ipsum dolor sit amer, consectetur adipiscing elit, du sed eiusmod tempor incididint ut labore et dolore magna aliqua"
    print(f'\n anagram check "Lorem ipsum dolor sit amer..." fail execution test')
    handle_loops(lorem_fail, short_n_angr)

    all_times_sorted = sorted(all_test_algorithm_sum.items(), key=lambda x:x[1])
    print('\nthe sum of algorithms execution times for all the cases above are:\n')
    for t in all_times_sorted:
        print(f"time execution for {t[0] : >30}:   {t[1] :>5}")
