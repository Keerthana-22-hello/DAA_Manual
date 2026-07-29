import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import random
import time


# -------------------------------------------------
# Interpolation Search
# -------------------------------------------------

def interpolation_search(arr, target):

    low = 0
    high = len(arr) - 1

    comparisons = 0

    while (
        low <= high
        and arr[low] <= target <= arr[high]
    ):

        comparisons += 1

        if low == high:

            if arr[low] == target:
                return low, comparisons

            return -1, comparisons

        if arr[high] == arr[low]:
            break

        pos = low + int(
            (
                (target - arr[low])
                * (high - low)
            )
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


# -------------------------------------------------
# Binary Search
# -------------------------------------------------

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


# -------------------------------------------------
# Performance Analysis
# -------------------------------------------------

def performance():

    sizes = [
        1000,
        5000,
        10000,
        50000,
        100000
    ]

    records = []

    for size in sizes:

        arr = sorted(
            random.sample(
                range(size * 10),
                size
            )
        )

        target = random.choice(arr)

        start = time.perf_counter()

        for _ in range(100):

            idx1, comp1 = interpolation_search(
                arr,
                target
            )

        interpolation_time = (
            (time.perf_counter() - start)
            / 100
            * 1000
        )

        start = time.perf_counter()

        for _ in range(100):

            idx2, comp2 = binary_search(
                arr,
                target
            )

        binary_time = (
            (time.perf_counter() - start)
            / 100
            * 1000
        )

        records.append(

            [
                size,
                round(interpolation_time, 5),
                round(binary_time, 5),
                comp1,
                comp2
            ]

        )

    return pd.DataFrame(

        records,

        columns=[

            "Array Size",

            "Interpolation Time (ms)",

            "Binary Time (ms)",

            "Interpolation Comparisons",

            "Binary Comparisons"

        ]

    )


# -------------------------------------------------
# Streamlit App
# -------------------------------------------------

def app():

    st.header("📌 Interpolation Search Performance Analysis")

    st.write(
        "Compare Interpolation Search with Binary Search."
    )

    default_array = [
        2,
        5,
        10,
        15,
        23,
        35,
        48,
        60,
        75,
        90,
        105,
        120
    ]

    array_text = st.text_input(
        "Enter Sorted Array (comma separated)",
        ",".join(map(str, default_array))
    )

    target = st.number_input(
        "Target Value",
        value=35
    )

    if st.button(
        "Run Search",
        key="search_button"
    ):

        try:

            arr = list(
                map(
                    int,
                    array_text.split(",")
                )
            )

        except:

            st.error(
                "Please enter a valid sorted integer array."
            )

            return

        arr.sort()

        idx1, comp1 = interpolation_search(
            arr,
            target
        )

        idx2, comp2 = binary_search(
            arr,
            target
        )

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Interpolation Index",
                idx1
            )

            st.metric(
                "Comparisons",
                comp1
            )

        with col2:

            st.metric(
                "Binary Index",
                idx2
            )

            st.metric(
                "Comparisons",
                comp2
            )

        result = pd.DataFrame({

            "Algorithm": [

                "Interpolation Search",

                "Binary Search"

            ],

            "Found Index": [

                idx1,

                idx2

            ],

            "Comparisons": [

                comp1,

                comp2

            ]

        })

        st.subheader("Search Result")

        st.dataframe(
            result,
            use_container_width=True
        )

        st.subheader("Comparison Chart")

        fig, ax = plt.subplots(
            figsize=(6, 4)
        )

        ax.bar(

            result["Algorithm"],

            result["Comparisons"]

        )

        ax.set_ylabel(
            "Comparisons"
        )

        ax.set_title(
            "Comparison Count"
        )

        st.pyplot(fig)

    st.divider()

    st.subheader("Performance Analysis")

    if st.button(
        "Run Performance Analysis",
        key="performance"
    ):

        df = performance()

        st.dataframe(
            df,
            use_container_width=True
        )

        col1, col2 = st.columns(2)

        with col1:

            fig1, ax1 = plt.subplots(
                figsize=(7, 4)
            )

            ax1.plot(
                df["Array Size"],
                df["Interpolation Time (ms)"],
                marker="o",
                label="Interpolation"
            )

            ax1.plot(
                df["Array Size"],
                df["Binary Time (ms)"],
                marker="s",
                label="Binary"
            )

            ax1.set_xlabel("Array Size")
            ax1.set_ylabel("Time (ms)")
            ax1.set_title("Execution Time")
            ax1.legend()

            st.pyplot(fig1)

        with col2:

            fig2, ax2 = plt.subplots(
                figsize=(7, 4)
            )

            ax2.plot(
                df["Array Size"],
                df["Interpolation Comparisons"],
                marker="o",
                label="Interpolation"
            )

            ax2.plot(
                df["Array Size"],
                df["Binary Comparisons"],
                marker="s",
                label="Binary"
            )

            ax2.set_xlabel("Array Size")
            ax2.set_ylabel("Comparisons")
            ax2.set_title("Comparison Count")
            ax2.legend()

            st.pyplot(fig2)

        st.success(
            "Performance analysis completed successfully."
        )