import streamlit as st
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

from algorithm import (
    dijkstra,
    reconstruct_path
)


def app():

    st.header("🚦 Dijkstra's Shortest Path Algorithm")

    st.markdown(
        """
Find the shortest paths from a source vertex using **Dijkstra's Algorithm**.
"""
    )

    # -------------------------------------------------
    # Sidebar
    # -------------------------------------------------

    st.sidebar.header("Graph Input")

    num_vertices = st.sidebar.number_input(
        "Number of Vertices",
        min_value=2,
        value=6,
        step=1,
        key="dijkstra_vertices"
    )

    default_graph = """0 1 4
0 2 1
1 3 1
2 1 2
2 3 5
3 4 3
4 5 2"""

    edge_text = st.sidebar.text_area(
        "Edges (source destination weight)",
        value=default_graph,
        height=220,
        key="dijkstra_edges"
    )

    source = st.sidebar.number_input(
        "Source Vertex",
        min_value=0,
        max_value=num_vertices - 1,
        value=0,
        key="dijkstra_source"
    )

    run = st.sidebar.button(
        "Run Dijkstra",
        key="run_dijkstra"
    )

    # -------------------------------------------------
    # Build Graph
    # -------------------------------------------------

    graph = {i: [] for i in range(num_vertices)}

    try:

        for line in edge_text.strip().split("\n"):

            if line.strip():

                u, v, w = map(int, line.split())

                graph[u].append((v, w))

    except:

        st.error(
            "Invalid edge format.\n\nUse:\nsource destination weight"
        )

        return

    if not run:
        return

    # -------------------------------------------------
    # Execute Algorithm
    # -------------------------------------------------

    dist, prev = dijkstra(
        graph,
        source
    )

    # -------------------------------------------------
    # Input Graph
    # -------------------------------------------------

    st.subheader("Input Graph")

    input_edges = []

    for u in graph:

        for v, w in graph[u]:

            input_edges.append(
                [
                    u,
                    v,
                    w
                ]
            )

    input_df = pd.DataFrame(

        input_edges,

        columns=[
            "Source",
            "Destination",
            "Weight"
        ]

    )

    st.dataframe(
        input_df,
        use_container_width=True
    )

    # -------------------------------------------------
    # Result Table
    # -------------------------------------------------

    st.subheader("Shortest Paths")

    result = []

    for vertex in range(num_vertices):

        path = reconstruct_path(
            prev,
            source,
            vertex
        )

        if path:

            path_str = " → ".join(
                map(str, path)
            )

        else:

            path_str = "No Path"

        distance = (

            dist[vertex]

            if dist[vertex] != float("inf")

            else "INF"

        )

        result.append(

            [

                vertex,

                distance,

                path_str

            ]

        )

    result_df = pd.DataFrame(

        result,

        columns=[

            "Vertex",

            "Distance",

            "Shortest Path"

        ]

    )

    st.dataframe(
        result_df,
        use_container_width=True
    )

    # -------------------------------------------------
    # Metrics
    # -------------------------------------------------

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Source Vertex",
            source
        )

    with col2:

        reachable = sum(

            d != float("inf")

            for d in dist

        )

        st.metric(
            "Reachable Vertices",
            reachable
        )

    # -------------------------------------------------
    # Distance Chart
    # -------------------------------------------------

    st.subheader("Shortest Distance from Source")

    distances = [

        0 if d == float("inf") else d

        for d in dist

    ]

    fig, ax = plt.subplots(figsize=(8, 4))

    ax.bar(

        range(num_vertices),

        distances

    )

    ax.set_xlabel("Vertex")

    ax.set_ylabel("Distance")

    ax.set_title("Shortest Distance")

    st.pyplot(fig)

    # -------------------------------------------------
    # Graph Visualization
    # -------------------------------------------------

    st.subheader("Shortest Path Tree")

    G = nx.DiGraph()

    for u in graph:

        for v, w in graph[u]:

            G.add_edge(

                u,

                v,

                weight=w

            )

    pos = nx.spring_layout(

        G,

        seed=42

    )

    fig2, ax2 = plt.subplots(figsize=(8, 6))

    nx.draw_networkx_nodes(

        G,

        pos,

        node_size=800,

        ax=ax2

    )

    nx.draw_networkx_labels(

        G,

        pos,

        ax=ax2

    )

    nx.draw_networkx_edges(

        G,

        pos,

        arrows=True,

        ax=ax2

    )

    nx.draw_networkx_edge_labels(

        G,

        pos,

        edge_labels=nx.get_edge_attributes(
            G,
            "weight"
        ),

        ax=ax2

    )

    tree_edges = []

    for vertex in range(num_vertices):

        if prev[vertex] is not None:

            tree_edges.append(

                (

                    prev[vertex],

                    vertex

                )

            )

    nx.draw_networkx_edges(

        G,

        pos,

        edgelist=tree_edges,

        edge_color="red",

        width=3,

        arrows=True,

        ax=ax2

    )

    st.pyplot(fig2)

    # -------------------------------------------------
    # Summary
    # -------------------------------------------------

    st.success(
        "✅ Dijkstra Algorithm Executed Successfully."
    )