def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        lesser_nums = [i for i in arr[1:] if i <= pivot]
        greater_nums = [i for i in arr[1:] if i > pivot]
        return quick_sort(lesser_nums) + [pivot] + quick_sort(greater_nums)


print(quick_sort([4, 1, 5, 9, 0, 3, 2]))
