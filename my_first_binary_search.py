def play(my_list, item):
    low = 0
    high = len(my_list) - 1
    while low <= high:
        mid = low + high
        guess = my_list[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        elif guess < item:
            low = mid + 1
        else:
            return None


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(play(my_list, 6))
