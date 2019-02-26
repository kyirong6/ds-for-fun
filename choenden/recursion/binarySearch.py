def binarySearch(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binarySearch(data, target,low, mid - 1)
        else:
            return binarySearch(data, target, mid + 1, high)


if '__main__' == __name__:
    lst = [1,2,3,4,5,6,7,8,9]
    print(binarySearch(lst, 2, 0, 8))