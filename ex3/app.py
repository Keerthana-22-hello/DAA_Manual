import streamlit as st
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

from algorithm import kruskal, prim, build_adj


# -------------------------------------------------
# Page Configuration
# -------------------------------------------------
st.set_page_config(
    page_title="Minimum Spanning Tree Visualizer",
    layout="wide"
)

st.title("🌳 Minimum Spanning Tree (MST)")
st.subheader("Kruskal's Algorithm vs Prim's Algorithm")


st.markdown(
"""
This dashboard demonstrates the working of

- Kruskal's Algorithm
- Prim's Algorithm

and compares the generated Minimum Spanning Trees.
"""
)

# -------------------------------------------------
# Default Graph
# -------------------------------------------------

default_edges = """7 0 1
5 0 3
8 1 2
9 1 3
7 1 4
5 2 4
15 3 4
6 3 5
8 4 5
9 4 6
11 5 6"""

st.sidebar.header("Graph Input")

nodes = st.sidebar.number_input(
    "Number of Vertices",
    min_value=2,
    value=7
)

edge_text = st.sidebar.text_area(
    "Edges (weight u v)",
    default_edges,
    height=250
)

run = st.sidebar.button("Generate MST")


# -------------------------------------------------
# Parse Edges
# -------------------------------------------------

edges = []

for line in edge_text.strip().split("\n"):

    if line.strip():

        w, u, v = map(int, line.split())

        edges.append((w, u, v))


adj = build_adj(edges)

if run:

    kruskal_mst, kruskal_cost = kruskal(nodes, edges.copy())

    prim_mst, prim_cost = prim(nodes, adj)

    # ---------------------------------------------
    # Cost Metrics
    # ---------------------------------------------

    c1, c2 = st.columns(2)

    with c1:
        st.metric(
            "Kruskal MST Cost",
            kruskal_cost
        )

    with c2:
        st.metric(
            "Prim MST Cost",
            prim_cost
        )

    # ---------------------------------------------
    # Tables
    # ---------------------------------------------

    st.header("Minimum Spanning Tree Edges")

    left, right = st.columns(2)

    with left:

        st.subheader("Kruskal")

        df1 = pd.DataFrame(
            kruskal_mst,
            columns=["Source", "Destination", "Weight"]
        )

        st.dataframe(df1, use_container_width=True)

    with right:

        st.subheader("Prim")

        df2 = pd.DataFrame(
            prim_mst,
            columns=["Source", "Destination", "Weight"]
        )

        st.dataframe(df2, use_container_width=True)

    # ---------------------------------------------
    # Graph Visualization
    # ---------------------------------------------

    st.header("Graph Visualization")

    G = nx.Graph()

    for w, u, v in edges:
        G.add_edge(u, v, weight=w)

    pos = nx.spring_layout(G, seed=42)

    fig, ax = plt.subplots(figsize=(8,6))

    nx.draw_networkx_nodes(
        G,
        pos,
        node_size=700,
        ax=ax
    )

    nx.draw_networkx_labels(
        G,
        pos,
        ax=ax
    )

    nx.draw_networkx_edges(
        G,
        pos,
        edge_color="lightgray",
        width=2,
        ax=ax
    )

    edge_labels = nx.get_edge_attributes(G, "weight")

    nx.draw_networkx_edge_labels(
        G,
        pos,
        edge_labels=edge_labels,
        ax=ax
    )

    mst_edges = [(u, v) for u, v, w in kruskal_mst]

    nx.draw_networkx_edges(
        G,
        pos,
        edgelist=mst_edges,
        width=4,
        edge_color="red",
        ax=ax
    )

    st.pyplot(fig)

    # ---------------------------------------------
    # Comparison
    # ---------------------------------------------

    st.header("Comparison")

    comparison = pd.DataFrame({

        "Algorithm": ["Kruskal", "Prim"],

        "Total Cost": [
            kruskal_cost,
            prim_cost
        ],

        "Edges in MST": [
            len(kruskal_mst),
            len(prim_mst)
        ]
    })

    st.dataframe(
        comparison,
        use_container_width=True
    )

    if kruskal_cost == prim_cost:

        st.success(
            "✅ Both algorithms generated the same Minimum Spanning Tree cost."
        )

    else:

        st.error(
            "The generated MST costs are different."
        )