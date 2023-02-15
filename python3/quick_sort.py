""" It looks like wikipedia wins again: https://en.wikipedia.org/wiki/Quicksort

    Quicksort is a type of divide and conquer algorithm for sorting an array,
    based on a partitioning routine; the details of this partitioning can vary
    somewhat, so that quicksort is really a family of closely related
    algorithms. Applied to a range of at least two elements, partitioning
    produces a division into two consecutive non empty sub-ranges, in such a
    way that no element of the first sub-range is greater than any element of
    already in its final location. Due to its recursive nature, quicksort (like
    the partition routine) has to be formulated so as to be callable for a
    range within a larger array, even if the ultimate goal is to sort a complete
    array.  """

def quick_sort(value, pivot=None, max_count=None, insert_pos=0):
    """ trying to do this in-place """

    if pivot is None:
        pivot = value[insert_pos]

    if max_count is None:
        max_count = len(value)
    else:
        max_count += insert_pos

    noop = 0
    count = insert_pos
    pivot_pos = insert_pos
    pivot_count = 0

    while count < max_count:
        if value[count] < pivot:
            value.insert(pivot_pos, value.pop(count))
            pivot_pos += 1
        elif value[count] == pivot:
            pivot_count += 1
            value.insert(pivot_pos, value.pop(count))
        else:
            noop += 1
        count += 1

    pos_movement = pivot_pos - insert_pos
    if pos_movement > 1:
        quick_sort(value, value[insert_pos], pos_movement, insert_pos)

    if noop > 1:
        noop_insert_pos = pivot_pos + pivot_count
        quick_sort(value, value[noop_insert_pos], noop, noop_insert_pos)

foo = [13, 7, 11, 22, 13, 80, 44, 6, 9, 2, 1, 4, 13, 7, 11, 22, 13, 80, 44, 6, 9, 2, 1, 4, 13, 7, 11, 22, 13, 80, 44, 6, 9, 2, 1, 4, 13]
answer = [1, 1, 1, 2, 2, 2, 4, 4, 4, 6, 6, 6, 7, 7, 7, 9, 9, 9, 11, 11, 11, 13, 13, 13, 13, 13, 13, 13, 22, 22, 22, 44, 44, 44, 80, 80, 80]

quick_sort(foo)
print(foo == answer)
