import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from algorithms import (
    naive_search,
    kmp_search,
    rabin_karp
)


def app():

    st.header("🔍 Comparative Analysis of String Matching Algorithms")

    st.write(
        "Compare Naive, KMP and Rabin-Karp Algorithms."
    )

    text = st.text_area(
        "Enter Text",
        "AABAACAADAABAABA",
        key="text_input"
    )

    pattern = st.text_input(
        "Enter Pattern",
        "AABA",
        key="pattern_input"
    )

    if st.button(
        "Run Comparison",
        key="run_string_matching"
    ):

        if len(pattern) == 0:

            st.error("Pattern cannot be empty.")
            return

        if len(pattern) > len(text):

            st.error("Pattern cannot be longer than the text.")
            return

        # -----------------------------------------
        # Execute Algorithms
        # -----------------------------------------

        n_match, n_comp, n_time = naive_search(
            text,
            pattern
        )

        k_match, k_comp, k_time = kmp_search(
            text,
            pattern
      )

        r_match, r_comp, r_time = rabin_karp(
            text,
            pattern,
        )

        # -----------------------------------------
        # Result Table
        # -----------------------------------------

        df = pd.DataFrame({

            "Algorithm": [
                "Naive",
                "KMP",
                "Rabin-Karp"
            ],

            "Matches": [
                str(n_match),
                str(k_match),
                str(r_match)
            ],

            "Comparisons": [
                n_comp,
                k_comp,
                r_comp
            ],              

            "Execution Time (ms)": [
                round(n_time, 5),
                round(k_time, 5),
                round(r_time, 5)
            ]
        })

        st.subheader("Results")

        st.dataframe(
            df,
            use_container_width=True
        )

        # -----------------------------------------
        # Metrics
        # -----------------------------------------

        col1, col2 = st.columns(2)

        fastest = df.loc[
            df["Execution Time (ms)"].idxmin()
        ]

        least = df.loc[
            df["Comparisons"].idxmin()
        ]

        with col1:

            st.metric(
                "⚡ Fastest Algorithm",
                fastest["Algorithm"]
            )

        with col2:

            st.metric(
                "✅ Least Comparisons",
                least["Algorithm"]
            )

        # -----------------------------------------
        # Charts
        # -----------------------------------------

        left, right = st.columns(2)

        with left:

            fig1, ax1 = plt.subplots(
                figsize=(6, 4)
            )

            ax1.bar(
                df["Algorithm"],
                df["Comparisons"]
            )

            ax1.set_title(
                "Character Comparisons"
            )

            ax1.set_ylabel(
                "Comparisons"
            )

            st.pyplot(fig1)

        with right:

            fig2, ax2 = plt.subplots(
                figsize=(6, 4)
            )

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

        # -----------------------------------------
        # Individual Results
        # -----------------------------------------

        st.subheader("Algorithm Details")

        tabs = st.tabs([
            "Naive",
            "KMP",
            "Rabin-Karp"
        ])

        with tabs[0]:

            st.write(
                f"**Matches Found:** {n_match}"
            )

            st.write(
                f"**Character Comparisons:** {n_comp}"
            )

            st.write(
                f"**Execution Time:** {round(n_time,5)} ms"
            )

        with tabs[1]:

            st.write(
                f"**Matches Found:** {k_match}"
            )

            st.write(
                f"**Character Comparisons:** {k_comp}"
            )

            st.write(
                f"**Execution Time:** {round(k_time,5)} ms"
            )

        with tabs[2]:

            st.write(
                f"**Matches Found:** {r_match}"
            )

            st.write(
                f"**Character Comparisons:** {r_comp}"
            )

            st.write(
                f"**Execution Time:** {round(r_time,5)} ms"
            )

        st.success("Comparison completed successfully.")