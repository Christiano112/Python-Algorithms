def smallest_num(arr):
    smallest_index = 0
    smallest = arr[0]

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return arr[smallest_index]


def biggest_num(arr):
    biggest_index = 0
    biggest = arr[len(arr) - 1]

    for i in range(1, len(arr)):
        if arr[i] > biggest:
            biggest = arr[i]
            biggest_index = i
    return arr[biggest_index]


arr = [1, 4, 5, 9, 1, 3]
print(smallest_num(arr))
print(biggest_num(arr))
