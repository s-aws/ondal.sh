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
        if not len(left) or not len(right):
            work.extend(left if len(left) else right)
            break
        else:
            if left[0] < right[0]:
                work.append(left.pop(0))
            else:
                work.append(right.pop(0))

    return work

print(merge_sort([7, 11, 22, 80, 44, 6, 9, 2, 1, 4, 13, 13, 13]))
# [1, 2, 4, 6, 7, 9, 11, 13, 13, 13, 22, 44, 80]
