'''
The Dutch National Flag Algorithm sorts an array of 0s, 1s and 2s in a single pass.
Invariant during execution:
0 0 0 0 0 ..... 0 | 1 1 1 1 1 ..... 1 | unsorted array | 2 2 2 2 2 ..... 2 
^                   ^                   ^                ^               ^
0                  low                 mid              high           n - 1

Case I: arr[mid] == 0

                            swap
                    |-------------------|
0 0 0 0 0 ..... 0 | 1 1 1 1 1 ..... 1 | 0 ..... unsorted array | 2 2 2 2 2 ..... 2 
^                   ^                   ^                        ^               ^
0                  low                 mid                      high           n - 1

Case II: arr[mid] == 1

0 0 0 0 0 ..... 0 | 1 1 1 1 1 ..... 1 | 1 ..... unsorted array | 2 2 2 2 2 ..... 2 
^                   ^                   ^                        ^               ^
0                  low                 mid                      high           n - 1

Case III: arr[mid] == 2

                                                     swap
                                        |----------------------------|
0 0 0 0 0 ..... 0 | 1 1 1 1 1 ..... 1 | 2 ..... unsorted array ..... X | 2 2 2 2 2 ..... 2 
^                   ^                   ^                            ^                   ^
0                  low                 mid                       high - 1              n - 1
'''

def DNF(arr):
    low, mid, high = 0, 0, len(arr) - 1
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr
