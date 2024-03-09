def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[len(array) // 2]
    left = [char for char in array if char < pivot]
    middle = [char for char in array if char == pivot]
    right = [char for char in array if char > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def is_anagram(first_string, second_string):

    first_string = first_string.lower()
    second_string = second_string.lower()

    list_first_string = quick_sort(list(first_string))
    list_second_string = quick_sort(list(second_string))

    result_first = "".join(list_first_string)
    result_second = "".join(list_second_string)

    is_anagramm = result_first == result_second

    return (result_first, result_second, is_anagramm)
