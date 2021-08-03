import timeit


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
    methods_list = (
        "is_anagram",
        "remove_chars_list",
        "generate_counter_dict",
        "recursive_dict",
        "slow_gen_counter_dict",
        "remove_chars",
        "slow_dict",
        "heap_sort",
        "bubble_sort",
        "insertion_sort",
        "quicksort",
        "merge_sort",
        "selection_sort",
        "dec_bubble_sort",
        "py_sort",
    )
    times_dict = {}
    for method in methods_list:
        times_dict[method] = get_exec_time(method, first_str, second_str)
    times_sorted = sorted(times_dict.items(), key=lambda x: x[1])
    for t in times_sorted:
        print(f"time execution for {t[0] : >30}:   {t[1] :>5}")
        if t[0] in all_test_algorithm_sum:
            all_test_algorithm_sum.update(
                {t[0]:  all_test_algorithm_sum[t[0]] + t[1]}
            )
        else:
            all_test_algorithm_sum[t[0]] = t[1]


def test_compare_times():

    lorem_text = "Lorem ipsum dolor sit amer, consectetur adipiscing" \
    + "elit, do sed eiusmod tempor incididint ut labore et dolore magna aliqua"

    lorem_o_t_t = "do sed eiusmod tempor incididint ut labore et dolore magna" \
    + " aliqua Lorem ipsum dolor sit amer, consectetur adipiscing elit,"

    print('\nanagram check, two identical strings 133 chars:')
    print(f'{lorem_text}"\nalgorithm execution times are:')

    handle_loops(lorem_text, lorem_o_t_t)

    all_chars_once = "the quick brown fox jumps over the lazy dog"
    a_chars_o = "god yzal eht revo spmuj xof nworb kciuq eht"
    print('\nanagram check, two anagrams strings:')
    print(f'"{all_chars_once}" | "{a_chars_o}"\nalgorithm execution times are:')
    handle_loops(all_chars_once, a_chars_o)

    short_string = 'evil'
    short_str_anagram = 'vile'
    print('\nanagram check, two short anagrams strings:')
    print('"evil | vile"\nalgorithm execution times are:')
    handle_loops(short_str_anagram, short_string)

    short_not_anagram = 'not anagram'
    short_n_angr = 'not anagran'
    print('\nanagram check, fail test case:'
        '\n"not anagram" | "not anagraN"\nalgorithm execution times are:')
    handle_loops(short_not_anagram, short_n_angr)

    lorem_fail = "Lorem ipsum dolor sit amer, consectetur adipiscing elit, du" \
    + " sed eiusmod tempor incididint ut labore et dolore magna aliqua"
    lorem_f = "Lorem ipsum dolor sit amer, consectetur adipiscing elit, du" \
    + " sed eiusmod tempor incididint ut labore et dolore magna aliquZ"
    print(f'\nanagram check, fail test case:\n"{lorem_fail}"\n' \
        + f'"{lorem_f}"\nalgorithm execution times are:')
    handle_loops(lorem_fail, lorem_f)

    repeat_char = 'aaaaaaaa'
    print('\nanagram check, same repeated char:'
        f'\n"{repeat_char}"\nalgorithm execution times are:')
    handle_loops(repeat_char, repeat_char)

    repeat_char = 'aaaaaaaa'
    repeat_char_dif = 'aaaaaaab'
    print('\nanagram check, fail test case:'
        f'\n"{repeat_char}" | "{repeat_char_dif}"\nalgorithm execution times are:')
    handle_loops(repeat_char, repeat_char_dif)

    
    all_times_sorted = sorted(
        all_test_algorithm_sum.items(), key=lambda x: x[1]
    )
    print('\ntime sum of algorithms execution for all the cases above are:\n')
    for t in all_times_sorted:
        print(f"time execution for {t[0] : >30}:   {t[1] :>5}")
