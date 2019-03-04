def reverse(S, start, stop):
    if start < stop - 1:
        S[start], S[stop - 1] = S[stop - 1], S[start]
        reverse(S, start + 1, stop - 1)


S = [1, 2, 3, 4, 5, 6, 7, 8]
reverse(S, 0, 8)            # Reverses the sequence
print(S)
reverse(S, 4, 5)            # Nothing happens
print(S)
reverse(S, 3, 5)            # Something happens
print(S)
