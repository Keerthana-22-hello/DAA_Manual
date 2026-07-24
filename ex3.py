# Interpolation Search Function
def interpolation_search(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high and arr[low] <= x <= arr[high]:

        # Prevent division by zero
        if arr[low] == arr[high]:
            if arr[low] == x:
                return low
            return -1

        # Estimate the probable position
        pos = low + ((high - low) * (x - arr[low])) // (arr[high] - arr[low])

        # Check if the estimated position is correct
        if arr[pos] == x:
            return pos

        # Search in the upper part
        elif arr[pos] < x:
            low = pos + 1

        # Search in the lower part
        else:
            high = pos - 1

    return -1


# Example Usage
arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
x = 70

result = interpolation_search(arr, x)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")