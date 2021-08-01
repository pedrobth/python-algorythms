from challenges.challenge_anagrams import bubble_sort, insertion_sort, is_anagram, remove_chars_list, generate_counter_dict, recursive_dict, slow_gen_counter_dict, remove_chars, slow_dict, heap_sort, quicksort, selection_sort, merge_sort
import timeit

def test_compare_times():
    setup_import = "from challenges.challenge_anagrams" " import is_anagram"
    setup_remove_chars_list = "from challenges.challenge_anagrams" " import remove_chars_list"
    setup_generate_counter_dict = "from challenges.challenge_anagrams" " import generate_counter_dict"
    setup_recursive_dict = "from challenges.challenge_anagrams" " import recursive_dict"
    setup_slow_gen_counter_dict = "from challenges.challenge_anagrams" " import slow_gen_counter_dict"
    setup_remove_chars = "from challenges.challenge_anagrams" " import remove_chars"
    setup_slow_dict = "from challenges.challenge_anagrams" " import slow_dict"
    setup_heap_sort = "from challenges.challenge_anagrams" " import heap_sort"
    setup_bubble_sort = "from challenges.challenge_anagrams" " import bubble_sort"
    setup_insertion_sort = "from challenges.challenge_anagrams" " import insertion_sort"
    setup_quicksort = "from challenges.challenge_anagrams" " import quicksort"
    setup_merge_sort = "from challenges.challenge_anagrams" " import merge_sort"
    setup_selection_sort = "from challenges.challenge_anagrams" " import selection_sort"

    first_string = (
        "Lorem ipsum dolor sit amer, consectetur adipiscing elit, do sed eiusmod tempor incididint ut labore et dolore magna aliqua"
    )

    second_string = (
        "Lorem ipsum dolor sit amer, consectetur "
        "adipiscing elit, do sed eiusmod tempor "
        "incididint ut labore et dolore magna aliqua"
    )

    time_is_anagram = timeit.timeit(
        f'is_anagram("{first_string}", "{second_string}")',
        setup=f"{setup_import}",
        number=10000,
    )
    print(f'\n anagram check, two identical strings:\n"Lorem ipsum dolor sit amer, consectetur adipiscing elit, do sed eiusmod tempor incididint ut labore et dolore magna aliqua"\n algorithm comparison execution times are:')
    print(f'\ntime execution for           Counter() from typing:  {time_is_anagram}')


    time_remove_chars_list = timeit.timeit(
        f'remove_chars_list("{first_string}", "{second_string}")',
        setup=f"{setup_remove_chars_list}",
        number=10000,
    )
    print(f'time execution for               remove_chars_list:  {time_remove_chars_list}')


    time_generate_counter_dict = timeit.timeit(
        f'generate_counter_dict("{first_string}", "{second_string}")',
        setup=f"{setup_generate_counter_dict}",
        number=10000,
    )

    print(f'time execution for           generate_counter_dict:  {time_generate_counter_dict}')


    time_recursive_dict = timeit.timeit(
        f'recursive_dict("{first_string}", "{second_string}")',
        setup=f"{setup_recursive_dict}",
        number=10000,
    )
    print(f'time execution for                  recursive_dict:  {time_recursive_dict}')


    time_slow_gen_counter_dict = timeit.timeit(
        f'slow_gen_counter_dict("{first_string}", "{second_string}")',
        setup=f"{setup_slow_gen_counter_dict}",
        number=10000,
    )
    print(f'time execution for           slow_gen_counter_dict:  {time_slow_gen_counter_dict}')


    time_remove_chars = timeit.timeit(
        f'remove_chars("{first_string}", "{second_string}")',
        setup=f"{setup_remove_chars}",
        number=10000,
    )
    print(f'time execution for                    remove_chars:  {time_remove_chars}')


    time_slow_dict = timeit.timeit(
        f'slow_dict("{first_string}", "{second_string}")',
        setup=f"{setup_slow_dict}",
        number=10000,
    )
    print(f'time execution for                       slow_dict:  {time_slow_dict}')


    time_quicksort = timeit.timeit(
        f'quicksort("{first_string}", "{second_string}")',
        setup=f"{setup_quicksort}",
        number=10000,
    )
    print(f'time execution for                       quicksort:  {time_quicksort}')
    
        
    time_merge_sort = timeit.timeit(
        f'merge_sort("{first_string}", "{second_string}")',
        setup=f"{setup_merge_sort}",
        number=10000,
    )
    print(f'time execution for                      merge_sort:  {time_merge_sort}')


    time_heap_sort = timeit.timeit(
        f'heap_sort("{first_string}", "{second_string}")',
        setup=f"{setup_heap_sort}",
        number=10000,
    )
    print(f'time execution for                       heap_sort:  {time_heap_sort}')


    time_insertion_sort = timeit.timeit(
        f'insertion_sort("{first_string}", "{second_string}")',
        setup=f"{setup_insertion_sort}",
        number=10000,
    )
    print(f'time execution for                  insertion_sort:  {time_insertion_sort}')
    


    
    time_selection_sort = timeit.timeit(
        f'selection_sort("{first_string}", "{second_string}")',
        setup=f"{setup_selection_sort}",
        number=10000,
    )
    print(f'time execution for                  selection_sort:  {time_selection_sort}')


    time_bubble_sort = timeit.timeit(
        f'bubble_sort("{first_string}", "{second_string}")',
        setup=f"{setup_bubble_sort}",
        number=10000,
    )
    print(f'time execution for                     bubble_sort:  {time_bubble_sort}')



    all_chars_once = (
        "the quick brown fox jump over the lazy dog"
    )

    second_time_is_anagram = timeit.timeit(
        f'is_anagram("{all_chars_once}", "{all_chars_once}")',
        setup=f"{setup_import}",
        number=10000,
    )

    second_time_remove_chars_list = timeit.timeit(
        f'remove_chars_list("{all_chars_once}", "{all_chars_once}")',
        setup=f"{setup_remove_chars_list}",
        number=10000,
    )

    second_time_generate_counter_dict = timeit.timeit(
        f'generate_counter_dict("{all_chars_once}", "{all_chars_once}")',
        setup=f"{setup_generate_counter_dict}",
        number=10000,
    )

    second_time_recursive_dict = timeit.timeit(
        f'recursive_dict("{all_chars_once}", "{all_chars_once}")',
        setup=f"{setup_recursive_dict}",
        number=10000,
    )

    second_time_slow_gen_counter_dict = timeit.timeit(
        f'slow_gen_counter_dict("{all_chars_once}", "{all_chars_once}")',
        setup=f"{setup_slow_gen_counter_dict}",
        number=10000,
    )

    second_time_remove_chars = timeit.timeit(
        f'remove_chars("{all_chars_once}", "{all_chars_once}")',
        setup=f"{setup_remove_chars}",
        number=10000,
    )

    second_time_slow_dict = timeit.timeit(
        f'slow_dict("{all_chars_once}", "{all_chars_once}")',
        setup=f"{setup_slow_dict}",
        number=10000,
    )

    second_time_heap_sort = timeit.timeit(
        f'heap_sort("{all_chars_once}", "{all_chars_once}")',
        setup=f"{setup_heap_sort}",
        number=10000,
    )

    second_time_bubble_sort = timeit.timeit(
        f'bubble_sort("{all_chars_once}", "{all_chars_once}")',
        setup=f"{setup_bubble_sort}",
        number=10000,
    )

    second_time_insertion_sort = timeit.timeit(
        f'insertion_sort("{all_chars_once}", "{all_chars_once}")',
        setup=f"{setup_insertion_sort}",
        number=10000,
    )

    second_time_merge_sort = timeit.timeit(
        f'merge_sort("{all_chars_once}", "{all_chars_once}")',
        setup=f"{setup_merge_sort}",
        number=10000,
    )

    second_time_quicksort = timeit.timeit(
        f'quicksort("{all_chars_once}", "{second_string}")',
        setup=f"{setup_quicksort}",
        number=10000,
    )

    second_time_selection_sort = timeit.timeit(
        f'selection_sort("{all_chars_once}", "{second_string}")',
        setup=f"{setup_selection_sort}",
        number=10000,
    )

    times_q_b_f = sorted(
        {'Counter() from typing': second_time_is_anagram,
        'remove_chars_list': second_time_remove_chars_list,
        'generate_counter_dict': second_time_generate_counter_dict,
        'recursive_dict': second_time_recursive_dict,
        'slow_gen_counter_dict': second_time_slow_gen_counter_dict,
        'remove_chars': second_time_remove_chars,
        'slow_dict': second_time_slow_dict,
        'heap_sort': second_time_heap_sort,
        'quicksort': second_time_quicksort,
        'merge_sort': second_time_merge_sort,
        'insertion_sort': second_time_insertion_sort,
        'selection_sort': second_time_selection_sort,
        'bubble_sort': second_time_bubble_sort}.items(), key=lambda x:x[1]
        )

    print(f'\nanagram check, two identical strings:\n"the quick brown fox jump over the lazy dog"\n algorithm comparison execution times are:')    
    for t in times_q_b_f:
        print(f"time execution for {t[0] : >30}:   {t[1] : >5}")
