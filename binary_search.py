def binary_search(list, item):
    start = 0
    end = len(list) - 1

    while start <= end:
        mid = round((start + end) / 2) # it should be int instead of float 
        guess = list[mid]
        if guess == item:
            return mid
        elif guess < item:
            start = mid + 1
        else:
            end = mid - 1
    return None


l = [1, 3, 4, 6, 8, 9] # it should be a list sorted order.
result = binary_search(l, 8)
print(result)
