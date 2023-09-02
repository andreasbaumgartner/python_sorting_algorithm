from random import randint

from utils import gen_array, run_algo


def main():
    array = gen_array(1000)
    run_algo("base_sort", array)
    run_algo("base_sort_reverse", array)
    run_algo("bubble_sort", array)
    run_algo("insertion_sort", array)
    run_algo("merge_sort", array)
    run_algo("quick_sort", array)


# ---------------------- base sort ---------------------- #
def base_sort(array):
    """
    Sorts an array using the built-in sorted() function
    """
    test = 1
    return sorted(array)


# ---------------------- base sort (reverse) ---------------------- #
def base_sort_reverse(array):
    """
    Sorts an array using the built-in sorted() function in reverse order
    """
    return sorted(array, reverse=True)


# ---------------------- bubble sort ---------------------- #
def bubble_sort(array):
    """
    Sorts an array using the bubble sort algorithm
    """
    n = len(array)

    for i in range(n):
        already_sorted = True

        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                already_sorted = False

        if already_sorted:
            break

    return array


# ---------------------- insertion sort ---------------------- #
def insertion_sort(array):
    """
    Sorts an array using the insertion sort algorithm
    """
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1

        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = key

    return array


# ---------------------- merge sort ---------------------- #
def merge(left, right):
    """
    Merges two arrays
    """
    if len(left) == 0:
        return right

    if len(right) == 0:
        return left

    result = []
    index_left = index_right = 0

    while len(result) < len(left) + len(right):
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1

        if index_right == len(right):
            result += left[index_left:]
            break

        if index_left == len(left):
            result += right[index_right:]
            break

    return result


def merge_sort(array):
    """
    Sorts an array using the merge sort algorithm
    """

    if len(array) < 2:
        return array

    mid = len(array) // 2

    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    return merge(left, right)


# ---------------------- quick sort ---------------------- #
def quick_sort(array):
    """
    Sorts an array using the quick sort algorithm
    """

    if len(array) < 2:
        return array

    low, same, high = [], [], []

    pivot = array[randint(0, len(array) - 1)]

    for item in array:
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)

    return quick_sort(low) + same + quick_sort(high)


if __name__ == "__main__":
    main()
