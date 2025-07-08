from typing import List, Optional

def bubble_sort_iterative(array: List[int]) -> None:     # O(n^2)
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

def bubble_sort_rec(array: List[int], n: Optional[int] = None) -> None:     # O(n^2)
    if n is None:
        n = len(array)
    if n <= 1:
        return None
    for i in range(n - 1):
        if array[i] > array[i + 1]:
            array[i], array[i + 1] = array[i + 1], array[i]
    bubble_sort_rec(array, n - 1)

def selection_sort_iter(array: List[int]) -> None:     # O(n^2)
    n = len(array)
    for i in range(n - 1, -1, -1):
        max_num_index = i
        for j in range(0, i + 1):
            if array[j] > array[max_num_index]:
                max_num_index = j
        array[i], array[max_num_index] = array[max_num_index], array[i]

def _prefix_max(array: List[int], i: int) -> int:
    if i == 0:
        return 0
    j = _prefix_max(array, i - 1)
    if array[j] > array[i]:
        return j
    else:
        return i

def selection_sort_rec(array: List[int], i: Optional[int] = None) -> None:     # O(n^2)
    if i is None:
        i = len(array) - 1
    if i > 0:
        j = _prefix_max(array, i)
        array[i], array[j] = array[j], array[i]
        selection_sort_rec(array, i - 1)

def insertion_sort_iter(array: List[int]) -> None:
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key

def _insert_last(array: List[int], i: int) -> None:
    if i > 0 and array[i] < array[i - 1]:
        array[i], array[i - 1] = array[i - 1], array[i]
        _insert_last(array, i - 1)

def insertion_sort_rec(array: List[int], i: Optional[int] = None) -> None:     # O(n^2)
    if i is None:
        i = len(array) - 1
    if i > 0:
        insertion_sort_rec(array, i - 1)
        _insert_last(array, i)

def _merge(left: List[int], right: List[int], array: List[int], len_left: int, len_right: int, l: int, r: int) -> None:
    if l < r:
        if (len_right <= 0) or (len_left > 0 and left[len_left - 1] > right[len_right - 1]):
            array[r - 1] = left[len_left - 1]
            len_left -= 1
        else:
            array[r - 1] = right[len_right - 1]
            len_right -= 1
        _merge(left, right, array, len_left, len_right, l, r - 1)

def merge_sort_rec(array: List[int], l: int = 0, r: Optional[int] = None) -> None:     # O(nlogn)
    if r is None:
        r = len(array)
    if 1 < r - l:
        m = (l + r + 1) // 2
        merge_sort_rec(array, l, m)
        merge_sort_rec(array, m, r)
        left, right = array[l:m], array[m:r]
        _merge(left, right, array, len(left), len(right), l, r)