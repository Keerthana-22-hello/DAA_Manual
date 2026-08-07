
import streamlit as st

import ex1
import ex2
import ex3
import ex4
import ex5
import ex6
# -------------------------------------------------
# Page Configuration
# -------------------------------------------------

st.set_page_config(
    page_title="DAA Laboratory Dashboard",
    page_icon="📘",
    layout="wide"
)

# -------------------------------------------------
# Header
# -------------------------------------------------

st.title("📘 Design and Analysis of Algorithms")
st.subheader("Interactive Laboratory Dashboard")

st.markdown(
"""
Welcome to the **DAA Laboratory Dashboard**.

This application demonstrates multiple Design and Analysis of Algorithms experiments with interactive visualization.

### Available Experiments

- 🔍 String Matching Algorithms
- 🌳 Minimum Spanning Tree (Prim & Kruskal)
- 🚦 Dijkstra Shortest Path
- 📌 Interpolation
- 📌 Divide and Conquer
- 📐 Matrix Chain Multiplication
"""
)

# -------------------------------------------------
# Sidebar
# -------------------------------------------------

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Choose Experiment",
    (
        "🏠 Home",
        "🔍 String Matching",
        "🌳 Minimum Spanning Tree",
        "🚦 Dijkstra Algorithm",
        "📌 Interpolation",
        "📌 Divide and Conquer",
        "📐 Matrix Chain Multiplication"
    )
)

# -------------------------------------------------
# Routing
# -------------------------------------------------

if page == "🏠 Home":

    st.info(
        "Select an experiment from the sidebar to begin."
    )

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(
        """
        ### 🔍 String Matching

        Compare

        - Naive Algorithm
        - Knuth-Morris-Pratt (KMP)
        - Rabin-Karp

        based on

        - Character Comparisons
        - Execution Time
        """
        )

        st.markdown(
        """
        ### 🌳 Minimum Spanning Tree

        Compare

        - Prim's Algorithm
        - Kruskal's Algorithm

        Generate the Minimum Spanning Tree and visualize it.
        """
        )

    with col2:

        st.markdown(
        """
        ### 🚦 Dijkstra

        Find

        - Shortest Path
        - Distance Table
        - Graph Visualization

        using Dijkstra's Algorithm.
        """
        )

        st.markdown(
        """
        ### 📌 Interpolation

        Find the interpolated value for a given set of data points using this.
        """
        )
        
        st.markdown(
        """
        ### 📌 Divide and Conquer

        Find the minimum and maximum element in an array using the Divide and Conquer technique.
        """
                )
        st.markdown(
        """
        ### 📐 Matrix Chain Multiplication

        Compute the minimum number of scalar
        multiplications using Dynamic Programming.

        Features

        - DP Cost Table
        - Split Table
        - Optimal Parenthesization
        - Performance Analysis
        """
        )

elif page == "🔍 String Matching":

    ex1.app()

elif page == "🌳 Minimum Spanning Tree":

    ex2.app()

elif page == "🚦 Dijkstra Algorithm":

    ex3.app()

elif page == "📌 Interpolation":

    ex4.app()

elif page == "📌 Divide and Conquer":

    ex5.app()
elif page == "📐 Matrix Chain Multiplication":
    
    ex6.app()