def find_sorted_subarray(arr):
    if len(set(arr)) == 1:
        return [0, 0]

    is_sorted = sorted(arr) == arr or sorted(arr, reverse=True) == arr
    if is_sorted:
        return [0, 0]  

    sorted_arr = sorted(arr)
    start_index = None
    end_index = None

    for i in range(len(arr)):
        if arr[i] != sorted_arr[i]:
            start_index = i
            break

    for i in range(len(arr)-1, -1, -1):
        if arr[i] != sorted_arr[i]:
            end_index = i
            break

    return [start_index, end_index]


# Test case
arr = [1, 2, 3, 6, 4, 4]
result = find_sorted_subarray(arr)
print(result)
