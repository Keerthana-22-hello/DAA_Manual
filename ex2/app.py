import streamlit as st
import time
import random
import pandas as pd
import matplotlib.pyplot as plt


# -----------------------------
# Search Algorithms
# -----------------------------
def interpolation_search(arr, target):
    low, high = 0, len(arr) - 1
    comparisons = 0

    while (
        low <= high
        and low < len(arr)
        and high < len(arr)
        and arr[low] <= target <= arr[high]
    ):
        comparisons += 1

        if arr[low] == arr[high]:
            if arr[low] == target:
                return low, comparisons
            break

        pos = low + int(
            ((target - arr[low]) * (high - low))
            / (arr[high] - arr[low])
        )

        if pos < low or pos > high:
            break

        if arr[pos] == target:
            return pos, comparisons

        elif arr[pos] < target:
            low = pos + 1

        else:
            high = pos - 1

    return -1, comparisons


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    comparisons = 0

    while low <= high:
        comparisons += 1
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid, comparisons

        elif arr[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return -1, comparisons


# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(
    page_title="Interpolation Search Analysis",
    layout="wide"
)

st.title("🔍 Interpolation Search Performance Analysis")

st.write(
    """
Compare **Interpolation Search** and **Binary Search**
based on execution time and number of comparisons.
"""
)

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.header("Input")

array_input = st.sidebar.text_input(
    "Sorted Array",
    "2,5,10,15,23,35,48,60,75,90,105,120"
)

target = st.sidebar.number_input(
    "Target",
    value=35
)

if st.sidebar.button("Run Search"):

    arr = list(map(int, array_input.split(",")))

    # Interpolation
    start = time.perf_counter()
    idx1, comp1 = interpolation_search(arr, target)
    time1 = (time.perf_counter() - start) * 1000

    # Binary
    start = time.perf_counter()
    idx2, comp2 = binary_search(arr, target)
    time2 = (time.perf_counter() - start) * 1000

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Interpolation Search")

        st.metric("Index Found", idx1)
        st.metric("Comparisons", comp1)
        st.metric("Execution Time (ms)", f"{time1:.6f}")

    with col2:
        st.subheader("Binary Search")

        st.metric("Index Found", idx2)
        st.metric("Comparisons", comp2)
        st.metric("Execution Time (ms)", f"{time2:.6f}")

# -----------------------------
# Performance Analysis
# -----------------------------
st.header("Performance Analysis")

sizes = [1000, 5000, 10000, 50000, 100000]

if st.button("Run Performance Test"):

    results = []

    progress = st.progress(0)

    for i, size in enumerate(sizes):

        arr = sorted(random.sample(range(size * 10), size))
        target = random.choice(arr)

        # Interpolation
        start = time.perf_counter()

        for _ in range(100):
            _, comp_is = interpolation_search(arr, target)

        is_time = ((time.perf_counter() - start) / 100) * 1000

        # Binary
        start = time.perf_counter()

        for _ in range(100):
            _, comp_bs = binary_search(arr, target)

        bs_time = ((time.perf_counter() - start) / 100) * 1000

        results.append([
            size,
            is_time,
            bs_time,
            comp_is,
            comp_bs
        ])

        progress.progress((i + 1) / len(sizes))

    df = pd.DataFrame(
        results,
        columns=[
            "Size",
            "Interpolation Time (ms)",
            "Binary Time (ms)",
            "Interpolation Comparisons",
            "Binary Comparisons",
        ],
    )

    st.subheader("Performance Table")
    st.dataframe(df, use_container_width=True)

    # -----------------------------
    # Time Graph
    # -----------------------------
    st.subheader("Execution Time Comparison")

    fig, ax = plt.subplots(figsize=(8,5))

    ax.plot(
        df["Size"],
        df["Interpolation Time (ms)"],
        marker="o",
        linewidth=2,
        label="Interpolation Search"
    )

    ax.plot(
        df["Size"],
        df["Binary Time (ms)"],
        marker="s",
        linewidth=2,
        label="Binary Search"
    )

    ax.set_xlabel("Input Size")
    ax.set_ylabel("Execution Time (ms)")
    ax.set_title("Execution Time Comparison")
    ax.legend()

    st.pyplot(fig)

    # -----------------------------
    # Comparison Graph
    # -----------------------------
    st.subheader("Number of Comparisons")

    fig2, ax2 = plt.subplots(figsize=(8,5))

    ax2.plot(
        df["Size"],
        df["Interpolation Comparisons"],
        marker="o",
        linewidth=2,
        label="Interpolation Search"
    )

    ax2.plot(
        df["Size"],
        df["Binary Comparisons"],
        marker="s",
        linewidth=2,
        label="Binary Search"
    )

    ax2.set_xlabel("Input Size")
    ax2.set_ylabel("Comparisons")
    ax2.set_title("Comparison Count")
    ax2.legend()

    st.pyplot(fig2)