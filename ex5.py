import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import random
import time

import algorithm


def app():

    st.header("📌 Divide and Conquer - Min-Max")

    st.markdown("""
This experiment compares the **Divide and Conquer** approach with the
**Naive Linear Search** approach for finding the minimum and maximum
elements in an array.
""")

    # -------------------------------------------------
    # User Input
    # -------------------------------------------------

    default_array = "3,1,7,4,9,2,8,5,6,0"

    array_text = st.text_input(
        "Enter Array (Comma Separated)",
        default_array
    )

    run = st.button(
        "Run Algorithm",
        key="minmax"
    )

    if run:

        try:

            arr = list(
                map(
                    int,
                    array_text.split(",")
                )
            )

        except:

            st.error(
                "Please enter valid integers separated by commas."
            )

            return

        if len(arr) == 0:

            st.error("Array cannot be empty.")

            return

        # ---------------------------------------------
        # Divide & Conquer
        # ---------------------------------------------

        algorithm.comparison_count = 0

        start = time.perf_counter()

        minimum, maximum = algorithm.min_max_dc(
            arr,
            0,
            len(arr) - 1
        )

        dc_time = (
            time.perf_counter() - start
        ) * 1000

        dc_comparisons = algorithm.comparison_count

        # ---------------------------------------------
        # Naive
        # ---------------------------------------------

        start = time.perf_counter()

        n_min, n_max, naive_comparisons = algorithm.min_max_naive(
            arr
        )

        naive_time = (
            time.perf_counter() - start
        ) * 1000

        # ---------------------------------------------
        # Metrics
        # ---------------------------------------------

        st.subheader("Results")

        c1, c2 = st.columns(2)

        with c1:

            st.metric(
                "Minimum",
                minimum
            )

            st.metric(
                "Maximum",
                maximum
            )

        with c2:

            st.metric(
                "Divide & Conquer Comparisons",
                dc_comparisons
            )

            st.metric(
                "Naive Comparisons",
                naive_comparisons
            )

        # ---------------------------------------------
        # Comparison Table
        # ---------------------------------------------

        df = pd.DataFrame({

            "Algorithm": [

                "Divide & Conquer",

                "Naive"

            ],

            "Minimum": [

                minimum,

                n_min

            ],

            "Maximum": [

                maximum,

                n_max

            ],

            "Comparisons": [

                dc_comparisons,

                naive_comparisons

            ],

            "Execution Time (ms)": [

                round(dc_time, 5),

                round(naive_time, 5)

            ]

        })

        st.subheader("Comparison Table")

        st.dataframe(
            df,
            use_container_width=True
        )

        # ---------------------------------------------
        # Charts
        # ---------------------------------------------

        col1, col2 = st.columns(2)

        with col1:

            fig1, ax1 = plt.subplots()

            ax1.bar(
                df["Algorithm"],
                df["Comparisons"]
            )

            ax1.set_title(
                "Comparison Count"
            )

            ax1.set_ylabel(
                "Comparisons"
            )

            st.pyplot(fig1)

        with col2:

            fig2, ax2 = plt.subplots()

            ax2.bar(
                df["Algorithm"],
                df["Execution Time (ms)"]
            )

            ax2.set_title(
                "Execution Time"
            )

            ax2.set_ylabel(
                "Milliseconds"
            )

            st.pyplot(fig2)

        st.success(
            "Algorithm executed successfully."
        )

    # =================================================
    # Performance Analysis
    # =================================================

    st.divider()

    st.subheader("Performance Analysis")

    if st.button(
        "Run Performance Analysis",
        key="performance_analysis"
    ):

        results = []

        for size in [

            10,
            100,
            1000,
            10000

        ]:

            arr = [

                random.randint(
                    1,
                    10000
                )

                for _ in range(size)

            ]

            # Divide & Conquer

            algorithm.comparison_count = 0

            start = time.perf_counter()

            algorithm.min_max_dc(
                arr,
                0,
                len(arr) - 1
            )

            dc_time = (
                time.perf_counter() - start
            ) * 1000

            dc_comp = algorithm.comparison_count

            # Naive

            start = time.perf_counter()

            algorithm.min_max_naive(arr)

            naive_time = (
                time.perf_counter() - start
            ) * 1000

            _, _, naive_comp = algorithm.min_max_naive(arr)

            theoretical = (

                (3 * size) // 2

            ) - 2

            results.append([

                size,

                dc_comp,

                naive_comp,

                theoretical,

                round(dc_time, 5),

                round(naive_time, 5)

            ])

        perf_df = pd.DataFrame(

            results,

            columns=[

                "Array Size",

                "DC Comparisons",

                "Naive Comparisons",

                "3n/2 - 2",

                "DC Time (ms)",

                "Naive Time (ms)"

            ]

        )

        st.dataframe(
            perf_df,
            use_container_width=True
        )

        # ---------------------------------------------
        # Charts
        # ---------------------------------------------

        c1, c2 = st.columns(2)

        with c1:

            fig3, ax3 = plt.subplots()

            ax3.plot(

                perf_df["Array Size"],

                perf_df["DC Comparisons"],

                marker="o",

                label="Divide & Conquer"

            )

            ax3.plot(

                perf_df["Array Size"],

                perf_df["Naive Comparisons"],

                marker="s",

                label="Naive"

            )

            ax3.set_title(
                "Comparison Count"
            )

            ax3.set_xlabel(
                "Array Size"
            )

            ax3.set_ylabel(
                "Comparisons"
            )

            ax3.legend()

            st.pyplot(fig3)

        with c2:

            fig4, ax4 = plt.subplots()

            ax4.plot(

                perf_df["Array Size"],

                perf_df["DC Time (ms)"],

                marker="o",

                label="Divide & Conquer"

            )

            ax4.plot(

                perf_df["Array Size"],

                perf_df["Naive Time (ms)"],

                marker="s",

                label="Naive"

            )

            ax4.set_title(
                "Execution Time"
            )

            ax4.set_xlabel(
                "Array Size"
            )

            ax4.set_ylabel(
                "Milliseconds"
            )

            ax4.legend()

            st.pyplot(fig4)

        st.success(
            "Performance analysis completed successfully."
        )