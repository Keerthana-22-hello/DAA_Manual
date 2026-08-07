import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import random
import time

import algorithm


def app():

    st.header("📌 Matrix Chain Multiplication using Dynamic Programming")

    st.markdown("""
This experiment demonstrates the **Matrix Chain Multiplication**
problem using **Dynamic Programming**.

The objective is to determine the most efficient way to multiply
a sequence of matrices by minimizing the total number of scalar
multiplications.

Unlike ordinary multiplication, the order of multiplication
significantly affects the computational cost.
""")

    # -----------------------------------------------------
    # User Input
    # -----------------------------------------------------

    default_dims = "10,30,5,60,10"

    dims_text = st.text_input(
        "Enter Matrix Dimensions (Comma Separated)",
        default_dims
    )

    run = st.button(
        "Run Algorithm",
        key="matrix_chain"
    )

    if run:

        try:

            dims = list(
                map(
                    int,
                    dims_text.split(",")
                )
            )

        except:

            st.error(
                "Please enter valid integer dimensions separated by commas."
            )
            return

        if len(dims) < 3:

            st.error(
                "At least two matrices are required."
            )
            return

        if min(dims) <= 0:

            st.error(
                "Dimensions must be positive integers."
            )
            return

        # ---------------------------------------------
        # Matrix Preview
        # ---------------------------------------------

        st.subheader("Matrix Sequence")

        matrix_data = []

        for i in range(len(dims) - 1):

            matrix_data.append({

                "Matrix": f"A{i+1}",
                "Rows": dims[i],
                "Columns": dims[i+1]

            })

        matrix_df = pd.DataFrame(matrix_data)

        st.dataframe(
            matrix_df,
            use_container_width=True
        )

        # ---------------------------------------------
        # Run Algorithm
        # ---------------------------------------------

        start = time.perf_counter()

        m, s = algorithm.matrix_chain_order(dims)

        execution_time = (
            time.perf_counter() - start
        ) * 1000

        n = len(dims) - 1

        minimum_cost = m[1][n]

        parenthesization = algorithm.print_optimal_parens(
            s,
            1,
            n
        )

        # ---------------------------------------------
        # Metrics
        # ---------------------------------------------

        st.subheader("Results")

        c1, c2, c3 = st.columns(3)

        with c1:

            st.metric(
                "Matrices",
                n
            )

        with c2:

            st.metric(
                "Minimum Cost",
                minimum_cost
            )

        with c3:

            st.metric(
                "Execution Time (ms)",
                round(execution_time, 5)
            )

        st.success(
            f"Optimal Parenthesization : {parenthesization}"
        )

        # ---------------------------------------------
        # Cost Table
        # ---------------------------------------------

        cost_table = []

        for i in range(1, n + 1):

            row = {}

            row["Matrix"] = f"A{i}"

            for j in range(1, n + 1):

                if j < i:

                    row[f"A{j}"] = "---"

                else:

                    row[f"A{j}"] = m[i][j]

            cost_table.append(row)

        cost_df = pd.DataFrame(cost_table)

        st.subheader("DP Cost Table")

        st.dataframe(
            cost_df,
            use_container_width=True
        )

        # ---------------------------------------------
        # Split Table
        # ---------------------------------------------

        split_table = []

        for i in range(1, n + 1):

            row = {}

            row["Matrix"] = f"A{i}"

            for j in range(1, n + 1):

                if j <= i:

                    row[f"A{j}"] = "-"

                else:

                    row[f"A{j}"] = s[i][j]

            split_table.append(row)

        split_df = pd.DataFrame(split_table)

        st.subheader("Split Table")

        st.dataframe(
            split_df,
            use_container_width=True
        )

        # ---------------------------------------------
        # Summary Table
        # ---------------------------------------------

        summary_df = pd.DataFrame({

            "Metric": [

                "Number of Matrices",

                "Minimum Cost",

                "Execution Time (ms)",

                "Time Complexity",

                "Space Complexity"

            ],

            "Value": [

                n,

                minimum_cost,

                round(execution_time, 5),

                "O(n³)",

                "O(n²)"

            ]

        })

        st.subheader("Summary")

        st.dataframe(
            summary_df,
            use_container_width=True
        )

        # ---------------------------------------------
        # Charts
        # ---------------------------------------------

        col1, col2 = st.columns(2)

        with col1:

            fig1, ax1 = plt.subplots()

            ax1.bar(

                ["Matrices", "DP Cells"],

                [

                    n,

                    n * n

                ]

            )

            ax1.set_title(
                "Problem Size"
            )

            ax1.set_ylabel(
                "Count"
            )

            st.pyplot(fig1)

        with col2:

            fig2, ax2 = plt.subplots()

            ax2.bar(

                ["Execution Time"],

                [

                    execution_time

                ]

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

    # ==================================================
    # Performance Analysis
    # ==================================================

    st.divider()

    st.subheader("Performance Analysis")

    if st.button(

        "Run Performance Analysis",

        key="matrix_chain_analysis"

    ):

        results = []

        sizes = [

            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10

        ]

        for size in sizes:

            dims = [

                random.randint(
                    5,
                    50
                )

                for _ in range(size + 1)

            ]

            start = time.perf_counter()

            m, s = algorithm.matrix_chain_order(
                dims
            )

            execution = (

                time.perf_counter() - start

            ) * 1000

            cells = size * size

            results.append([

                size,

                cells,

                round(execution, 5),

                m[1][size]

            ])
                    # ---------------------------------------------
        # Performance DataFrame
        # ---------------------------------------------

        perf_df = pd.DataFrame(

            results,

            columns=[

                "Matrices",

                "DP Cells",

                "Execution Time (ms)",

                "Minimum Cost"

            ]

        )

        st.dataframe(
            perf_df,
            use_container_width=True
        )

        # ---------------------------------------------
        # Performance Charts
        # ---------------------------------------------

        c1, c2 = st.columns(2)

        with c1:

            fig3, ax3 = plt.subplots()

            ax3.plot(

                perf_df["Matrices"],

                perf_df["Execution Time (ms)"],

                marker="o",

                linewidth=2

            )

            ax3.set_title(
                "Execution Time vs Number of Matrices"
            )

            ax3.set_xlabel(
                "Number of Matrices"
            )

            ax3.set_ylabel(
                "Execution Time (ms)"
            )

            ax3.grid(True)

            st.pyplot(fig3)

        with c2:

            fig4, ax4 = plt.subplots()

            ax4.plot(

                perf_df["Matrices"],

                perf_df["DP Cells"],

                marker="s",

                linewidth=2

            )

            ax4.set_title(
                "DP Table Size"
            )

            ax4.set_xlabel(
                "Number of Matrices"
            )

            ax4.set_ylabel(
                "DP Cells"
            )

            ax4.grid(True)

            st.pyplot(fig4)

        # ---------------------------------------------
        # Additional Charts
        # ---------------------------------------------

        c3, c4 = st.columns(2)

        with c3:

            fig5, ax5 = plt.subplots()

            ax5.bar(

                perf_df["Matrices"].astype(str),

                perf_df["Minimum Cost"]

            )

            ax5.set_title(
                "Minimum Multiplication Cost"
            )

            ax5.set_xlabel(
                "Matrices"
            )

            ax5.set_ylabel(
                "Cost"
            )

            st.pyplot(fig5)

        with c4:

            theoretical = [

                n ** 3

                for n in perf_df["Matrices"]

            ]

            fig6, ax6 = plt.subplots()

            ax6.plot(

                perf_df["Matrices"],

                theoretical,

                marker="^",

                linewidth=2,

                label="O(n³)"

            )

            ax6.legend()

            ax6.set_title(
                "Theoretical Growth"
            )

            ax6.set_xlabel(
                "Number of Matrices"
            )

            ax6.set_ylabel(
                "Relative Operations"
            )

            ax6.grid(True)

            st.pyplot(fig6)

        # ---------------------------------------------
        # Complexity Information
        # ---------------------------------------------

        st.subheader("Algorithm Complexity")

        complexity_df = pd.DataFrame({

            "Property": [

                "Technique",

                "Time Complexity",

                "Space Complexity",

                "Problem Type",

                "Approach"

            ],

            "Value": [

                "Dynamic Programming",

                "O(n³)",

                "O(n²)",

                "Optimization",

                "Bottom-Up DP"

            ]

        })

        st.dataframe(

            complexity_df,

            use_container_width=True

        )

        # ---------------------------------------------
        # Inference
        # ---------------------------------------------

        st.subheader("Inference")

        st.markdown("""

- Dynamic Programming eliminates repeated computations by storing intermediate results.

- The DP table requires **O(n²)** memory.

- The algorithm evaluates every possible split point, leading to **O(n³)** time complexity.

- Matrix multiplication order affects only the computation cost, **not the final result**.

- The optimal parenthesization minimizes the total number of scalar multiplications.

- As the number of matrices increases, execution time and DP table size grow rapidly.

- Matrix Chain Multiplication is one of the classical Dynamic Programming optimization problems.

""")

        st.success(
            "Performance analysis completed successfully."
        )