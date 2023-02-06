def smallest_num(arr):
    smallest_index = 0
    smallest = arr[0]

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def biggest_num(arr):
    biggest_num = arr[len(arr) -1]
    biggest_num_index = len(arr) - 1
    for i in range(1, len(arr)):
        if arr[i] > biggest_num:
            biggest_num = arr[i]
            biggest_num_index = i
    return biggest_num_index


def selection_sort_small(arr):
    new_arr = []
    for i in range(len(arr)):
        sort_smallest = smallest_num(arr)
        new_arr.append(arr.pop(sort_smallest))
    return new_arr


def selection_sort_big(arr):
    new_arr =[]
    for i in range(len(arr)):
        sort_biggest = biggest_num(arr)
        new_arr.append(arr.pop(sort_biggest))
    return new_arr


print(selection_sort_small([2, 6, 7, 1, 9]))
print(selection_sort_big([2, 6, 7, 1, 9]))