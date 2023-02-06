def my_recursion(x):
    if x == 1:
        return 1
    else:
        return x * my_recursion(x - 1)


def sum_arr(arr):
    if arr == []:
        return 0
    else:
        return arr[0] + sum_arr(arr[1:])


def count_arr(arr):
    if arr == []:
        return 0
    else:
        return 1 + count_arr(arr[1:])


def max_num(arr):
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    my_max = max_num(arr[1:])
    return arr[0] if arr[0] > my_max else my_max


my_arr = [2, 1, 5, 3, 7, 9, 0]
print(max_num(my_arr))
print(count_arr(my_arr))
print(sum_arr([2, 4, 8, 1]))
print(my_recursion(7))

