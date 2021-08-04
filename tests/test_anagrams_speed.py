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
        "unicode_sum",
        "smart_dict"
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

    all_diff = 'qwertyuiopasd'
    all_diff_dif = 'fghjklzxcvbnm'
    print('\nanagram check, fail test case:'
        f'\n"{all_diff}" | "{all_diff_dif}"\nalgorithm execution times are:')
    handle_loops(all_diff, all_diff_dif)

    long_lorem = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Bibendum ut tristique et egestas quis ipsum. Sed viverra tellus in hac habitasse platea dictumst vestibulum rhoncus. Integer quis auctor elit sed. Id aliquet risus feugiat in ante metus dictum at. Congue eu consequat ac felis donec et odio pellentesque diam. Consectetur adipiscing elit pellentesque habitant morbi tristique senectus et. Ac feugiat sed lectus vestibulum mattis ullamcorper velit sed. Lobortis elementum nibh tellus molestie nunc non. Turpis egestas pretium aenean pharetra magna ac. Mi in nulla posuere sollicitudin aliquam ultrices sagittis orci a. At risus viverra adipiscing at in tellus integer feugiat scelerisque. Vulputate dignissim suspendisse in est ante in. Ultrices dui sapien eget mi proin sed libero. Id cursus metus aliquam eleifend mi in nulla. Mattis pellentesque id nibh tortor. Hendrerit dolor magna eget est lorem ipsum dolor sit amet. Senectus et netus et malesuada fames ac turpis egestas maecenas. Bibendum neque egestas congue quisque egestas diam in. Leo vel orci porta non pulvinar neque laoreet. Sem integer vitae justo eget magna fermentum iaculis. Amet justo donec enim diam vulputate ut pharetra sit. Sit amet purus gravida quis blandit turpis cursus in hac. Ac feugiat sed lectus vestibulum. At auctor urna nunc id cursus metus. Sed ullamcorper morbi tincidunt ornare massa. Eget velit aliquet sagittis id. Turpis in eu mi bibendum neque. Condimentum vitae sapien pellentesque habitant morbi tristique. Habitant morbi tristique senectus et netus et malesuada frames ac.'

    print('\nanagram check, reversed text comparison test case:'
        f'\n"long_lorem" | "reversed(long_lorem) 1640 chars each"\nalgorithm execution times are - this might take several minuetes:')
    handle_loops(long_lorem, reversed(long_lorem))
    all_times_sorted = sorted(
        all_test_algorithm_sum.items(), key=lambda x: x[1]
    )
    print('\ntime sum of algorithms execution for all the cases above are:\n')
    for t in all_times_sorted:
        print(f"time execution for {t[0] : >30}:   {t[1] :>5}")
