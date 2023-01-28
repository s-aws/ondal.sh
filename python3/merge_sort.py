""" I don't usually like wikipedia but one section from: https://en.wikipedia.org/wiki/Merge_sort really helped me understand.

    To help understand this, consider an array with two elements. The elements are copied to B[], then merged back to A[].
    If there are four elements, when the bottom of the recursion level is reached, single element runs from A[] are merged to B[],
    and then at the next higher level of recursion, those two-element runs are merged to A[]. This pattern continues with each level
    of recursion."""

def merge_sort(value):
    def get_left_right_segments(length):
        if length % 2:
            midpoint =  int((length-1)/2)
        else:
            midpoint =  int((length/2))
        return (value[:midpoint], value[midpoint:])

    length = len(value)

    if length == 1:
        return value

    left, right = get_left_right_segments(length)
    left, right = merge_sort(left), merge_sort(right)

    work = []

    while True:
        if len(left) and len(right):
            if left[0] < right[0]:
                work.append(left.pop(0))
            else:
                work.append(right.pop(0))
        else:
            work.extend(left if len(left) else right)
            break
    return work

print(merge_sort([7, 11, 22, 80, 44, 6, 9, 2, 1, 4, 13, 13, 13]))
# [1, 2, 4, 6, 7, 9, 11, 13, 13, 13, 22, 44, 80]
