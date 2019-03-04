def bad_power(x, n):
    """This definition of power function runs in O(n) since the parameter is decreasing by one in each function call"""
    if n == 0:
        return 1
    else:
        return x * bad_power(n - 1)


def good_power(x, n):
    """This one runs in O(log n)"""
    if n == 0:
        return 1
    else:
        partial = good_power(x, n//2)
        result = partial * partial
        if n % 2 == 1:
            result *= x             # if n is odd, include an extra factor of x
        return result
