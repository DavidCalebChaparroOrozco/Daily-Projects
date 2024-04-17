def quicksort(arr):
    if not isinstance(arr, list):
        # Check if the input is a list
        raise TypeError("Input must be a list")
    
    # Base case: if the array has 1 or fewer elements, it's already sorted
    if len(arr) <= 1:
        return arr
    else:
        # Selecting the first element as the pivot
        pivot = arr[len(arr) // 2]
        # Partitioning the array into two subarrays: left (elements less than pivot) and right (elements greater than or equal to pivot)
        left = [x for x in arr if x < pivot]
        equal = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        # Recursively sorting the left and right subarrays, then combining them with the pivot
        return quicksort(left) + equal + quicksort(right)

# Example usage
arr = [1, 7, 4, 1, 10, 9, -2]
sorted_arr = quicksort(arr)
print("Sorted Array in Ascending Order:")
print(sorted_arr)