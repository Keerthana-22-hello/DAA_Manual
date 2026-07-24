import random
import time
import matplotlib.pyplot as plt


# Recursive Binary Search Function
def binary_search_recursive(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search_recursive(arr, low, mid - 1, x)
        else:
            return binary_search_recursive(arr, mid + 1, high, x)
    else:
        return -1


# Performance Testing Function
def test_binary_search_recursive():
    sizes = [10, 100, 1000, 10000, 100000]
    times = []

    for n in sizes:
        # Generate and sort the array
        arr = [random.randint(1, n) for _ in range(n)]
        arr.sort()

        # Random element to search
        x = random.randint(1, n)

        # Measure execution time
        start_time = time.time()
        result = binary_search_recursive(arr, 0, n - 1, x)
        end_time = time.time()

        # Display result
        if result == -1:
            print(f"Element {x} not found in the array")
        else:
            print(f"Element {x} found at index {result}")

        elapsed_time = end_time - start_time
        print(f"Time taken to search in array of size {n}: {elapsed_time:.6f} seconds")
        print("=" * 50)

        times.append(elapsed_time)

    # Plot the graph
    plt.figure(figsize=(8, 5))
    plt.plot(sizes, times, marker='o')
    plt.title("Recursive Binary Search Performance")
    plt.xlabel("Size of Array")
    plt.ylabel("Time Taken (seconds)")
    plt.xscale("log")
    plt.yscale("log")
    plt.grid(True)
    plt.show()


# Main Function
test_binary_search_recursive()