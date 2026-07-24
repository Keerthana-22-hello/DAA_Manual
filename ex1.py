import time
import matplotlib.pyplot as plt
import random


# Linear Search Function
def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1


# Different input sizes
n_values = [100, 1000, 10000, 100000, 1000000]
time_values = []

# Measure execution time
for n in n_values:
    # Generate random array
    arr = [random.randint(1, n * 10) for _ in range(n)]

    # Select an element to search
    x = random.choice(arr)

    # Start timer
    start_time = time.time()

    # Perform Linear Search
    linear_search(arr, x)

    # End timer
    end_time = time.time()

    # Store execution time
    time_values.append(end_time - start_time)

# Plot the graph
plt.figure(figsize=(8, 5))
plt.plot(n_values, time_values, marker='o')
plt.title('Linear Search')
plt.xlabel('Number of Elements')
plt.ylabel('Time Taken (seconds)')
plt.grid(True)
plt.show()