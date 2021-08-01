from challenges.challenge_anagrams import bubble_sort, insertion_sort, is_anagram, remove_chars_list, generate_counter_dict, recursive_dict, slow_gen_counter_dict, remove_chars, slow_dict, heap_sort, quicksort, selection_sort
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
    setup_selection_sort = "from challenges.challenge_anagrams" " import selection_sort"

    first_string = (
        "Lorem ipsum dolor sit amer, consectetur "
        "adipiscing elit, do sed eiusmod tempor "
        "incididint ut labore et dolore magna aliqua"
    )

    second_string = (
        "Lorem ipsum dolor sit amer, consectetur "
        "adipiscing elit, do sed eiusmod tempor "
        "incididint ut labore et dolore magna aliqua"
    )

    algorithms_correct = is_anagram(first_string, second_string) is True
    time_is_anagram = timeit.timeit(
        f'is_anagram("{first_string}", "{second_string}")',
        setup=f"{setup_import}",
        number=10000,
    )
    correct_time = time_is_anagram <= 0.2
    assert (
        algorithms_correct and correct_time
    ), f"Falhou, o tempo foi: {time_is_anagram}, algoritmo correto? {algorithms_correct}"

    algorithms_correct = remove_chars_list(first_string, second_string) is True
    time_remove_chars_list = timeit.timeit(
        f'remove_chars_list("{first_string}", "{second_string}")',
        setup=f"{setup_remove_chars_list}",
        number=10000,
    )
    correct_time = time_remove_chars_list <= 0.2
    assert (
        algorithms_correct and correct_time
    ), f"Falhou, o tempo foi: {time_remove_chars_list}, algoritmo correto? {algorithms_correct}"

    algorithms_correct = generate_counter_dict(first_string, second_string) is True
    time_generate_counter_dict = timeit.timeit(
        f'generate_counter_dict("{first_string}", "{second_string}")',
        setup=f"{setup_generate_counter_dict}",
        number=10000,
    )
    correct_time = time_generate_counter_dict <= 0.2
    assert (
        algorithms_correct and correct_time
    ), f"Falhou, o tempo foi: {time_generate_counter_dict}, algoritmo correto? {algorithms_correct}"


    algorithms_correct = recursive_dict(first_string, second_string) is True
    time_recursive_dict = timeit.timeit(
        f'recursive_dict("{first_string}", "{second_string}")',
        setup=f"{setup_recursive_dict}",
        number=10000,
    )
    correct_time = time_recursive_dict <= 0.2
    assert (
        algorithms_correct and correct_time
    ), f"Falhou, o tempo foi: {time_recursive_dict}, algoritmo correto? {algorithms_correct}"


    algorithms_correct = slow_gen_counter_dict(first_string, second_string) is True
    time_slow_gen_counter_dict = timeit.timeit(
        f'slow_gen_counter_dict("{first_string}", "{second_string}")',
        setup=f"{setup_slow_gen_counter_dict}",
        number=10000,
    )
    correct_time = time_slow_gen_counter_dict <= 0.2
    assert (
        algorithms_correct and correct_time
    ), f"Falhou, o tempo foi: {time_slow_gen_counter_dict}, algoritmo correto? {algorithms_correct}"


    algorithms_correct = remove_chars(first_string, second_string) is True
    time_remove_chars = timeit.timeit(
        f'remove_chars("{first_string}", "{second_string}")',
        setup=f"{setup_remove_chars}",
        number=10000,
    )
    correct_time = time_remove_chars <= 7.2
    assert (
        algorithms_correct and correct_time
    ), f"Falhou, o tempo foi: {time_remove_chars}, algoritmo correto? {algorithms_correct}"

    algorithms_correct = slow_dict(first_string, second_string) is True
    time_slow_dict = timeit.timeit(
        f'slow_dict("{first_string}", "{second_string}")',
        setup=f"{setup_slow_dict}",
        number=10000,
    )
    correct_time = time_slow_dict <= 7.2
    assert (
        algorithms_correct and correct_time
    ), f"Falhou, o tempo foi: {time_slow_dict}, algoritmo correto? {algorithms_correct}"


    algorithms_correct = heap_sort(first_string, second_string) is True
    time_heap_sort = timeit.timeit(
        f'heap_sort("{first_string}", "{second_string}")',
        setup=f"{setup_heap_sort}",
        number=10000,
    )
    correct_time = time_heap_sort <= 7.2
    assert (
        algorithms_correct and correct_time
    ), f"Falhou, o tempo foi: {time_heap_sort}, algoritmo correto? {algorithms_correct}"


    algorithms_correct = bubble_sort(first_string, second_string) is True
    time_bubble_sort = timeit.timeit(
        f'bubble_sort("{first_string}", "{second_string}")',
        setup=f"{setup_bubble_sort}",
        number=10000,
    )
    correct_time = time_bubble_sort <= 15
    assert (
        algorithms_correct and correct_time
    ), f"Falhou, o tempo foi: {time_bubble_sort}, algoritmo correto? {algorithms_correct}"


    algorithms_correct = insertion_sort(first_string, second_string) is True
    time_insertion_sort = timeit.timeit(
        f'insertion_sort("{first_string}", "{second_string}")',
        setup=f"{setup_insertion_sort}",
        number=10000,
    )
    correct_time = time_insertion_sort <= 7.2
    assert (
        algorithms_correct and correct_time
    ), f"Falhou, o tempo foi: {time_insertion_sort}, algoritmo correto? {algorithms_correct}"

    algorithms_correct = quicksort(first_string, second_string) is True
    time_quicksort = timeit.timeit(
        f'quicksort("{first_string}", "{second_string}")',
        setup=f"{setup_quicksort}",
        number=10000,
    )
    correct_time = time_quicksort <= 7.2
    assert (
        algorithms_correct and correct_time
    ), f"Falhou, o tempo foi: {time_quicksort}, algoritmo correto? {algorithms_correct}"

    algorithms_correct = selection_sort(first_string, second_string) is True
    time_selection_sort = timeit.timeit(
        f'selection_sort("{first_string}", "{second_string}")',
        setup=f"{setup_selection_sort}",
        number=10000,
    )
    correct_time = time_selection_sort <= 7.2
    assert (
        algorithms_correct and correct_time
    ), f"Falhou, o tempo foi: {time_selection_sort}, algoritmo correto? {algorithms_correct}"

    print(f'\ntime execution for        Counter() from typing :  {time_is_anagram}')
    print(f'time execution for             remove_chars_list:  {time_remove_chars_list}')
    print(f'time execution for         generate_counter_dict:  {time_generate_counter_dict}')
    print(f'time execution for                recursive_dict:  {time_recursive_dict}')
    print(f'time execution for         slow_gen_counter_dict:  {time_slow_gen_counter_dict}')
    print(f'time execution for                  remove_chars:  {time_remove_chars}')
    print(f'time execution for                     slow_dict:  {time_slow_dict}')
    print(f'time execution for                     heap_sort:  {time_heap_sort}')
    print(f'time execution for                     quicksort:  {time_quicksort}')
    print(f'time execution for                insertion_sort:  {time_insertion_sort}')
    print(f'time execution for                selection_sort:  {time_selection_sort}')
    print(f'time execution for                   bubble_sort:  {time_bubble_sort}')


