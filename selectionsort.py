def selection_sort(arr):
    for i in range(len(arr)):
        # Find the minimum element in the remaining unsorted array
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Example usage:
arr = [38, 27, 43, 3, 9, 82, 10]
selection_sort(arr)
print("Sorted array is:", arr)
