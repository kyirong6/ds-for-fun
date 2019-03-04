def binary_search_iterative(data, target):
    """non-recursive implementation of binary search"""
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False


def reverse_iterative(S):
    """runs in O(n)"""
    start, stop = 0, len(S)
    while start < stop - 1:
        S[start], S[stop - 1] = S[stop - 1], S[start]
        start, stop = start + 1, stop - 1


"""Keep in mind that most recursive algorithms can 
be rewritten non-recursively with loops inside the body
of the function and some can even be as efficient"""
