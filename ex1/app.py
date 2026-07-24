import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from algorithms import *

st.set_page_config(
    page_title="String Matching Dashboard",
    layout="wide"
)

st.title("🔍 Comparative Analysis of String Matching Algorithms")

st.write("Compare Naive, KMP and Rabin-Karp Algorithms")

text = st.text_area(
    "Enter Text",
    "AABAACAADAABAABA"
)

pattern = st.text_input(
    "Enter Pattern",
    "AABA"
)

if st.button("Run Comparison"):

    if len(pattern) == 0:

        st.error("Pattern cannot be empty")

    elif len(pattern) > len(text):

        st.error("Pattern cannot be longer than text")

    else:

        n_match, n_comp, n_time = naive_search(text, pattern)

        k_match, k_comp, k_time = kmp_search(text, pattern)

        r_match, r_comp, r_time = rabin_karp(text, pattern)

        df = pd.DataFrame({

            "Algorithm":[
                "Naive",
                "KMP",
                "Rabin-Karp"
            ],

            "Matches":[
                str(n_match),
                str(k_match),
                str(r_match)
            ],

            "Comparisons":[
                n_comp,
                k_comp,
                r_comp
            ],

            "Execution Time (ms)":[
                round(n_time,5),
                round(k_time,5),
                round(r_time,5)
            ]
        })

        st.subheader("Results")

        st.dataframe(df, use_container_width=True)

        col1, col2 = st.columns(2)

        with col1:

            fig, ax = plt.subplots()

            ax.bar(
                df["Algorithm"],
                df["Comparisons"]
            )

            ax.set_title("Character Comparisons")

            ax.set_ylabel("Comparisons")

            st.pyplot(fig)

        with col2:

            fig2, ax2 = plt.subplots()

            ax2.bar(
                df["Algorithm"],
                df["Execution Time (ms)"]
            )

            ax2.set_title("Execution Time")

            ax2.set_ylabel("Milliseconds")

            st.pyplot(fig2)

        st.subheader("Fastest Algorithm")

        fastest = df.loc[
            df["Execution Time (ms)"].idxmin()
        ]

        st.success(
            f"{fastest['Algorithm']} is the fastest."
        )

        st.subheader("Least Comparisons")

        least = df.loc[
            df["Comparisons"].idxmin()
        ]

        st.info(
            f"{least['Algorithm']} performed the least comparisons."
        )