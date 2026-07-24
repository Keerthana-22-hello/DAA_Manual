import streamlit as st
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

from algorithm import dijkstra, reconstruct_path


# ------------------------------------------------
# Page Configuration
# ------------------------------------------------

st.set_page_config(
    page_title="Dijkstra Algorithm Visualizer",
    page_icon="🚦",
    layout="wide"
)

st.title("🚦 Dijkstra's Shortest Path Algorithm")
st.markdown(
    "Find the shortest paths from a source vertex using **Dijkstra's Algorithm**."
)

# ------------------------------------------------
# Sidebar
# ------------------------------------------------

st.sidebar.header("Graph Input")

num_vertices = st.sidebar.number_input(
    "Number of Vertices",
    min_value=2,
    value=6,
    step=1
)

default_graph = """0 1 4
0 2 1
1 3 1
2 1 2
2 3 5
3 4 3
4 5 2"""

edge_text = st.sidebar.text_area(
    "Edges (u v weight)",
    value=default_graph,
    height=220
)

source = st.sidebar.number_input(
    "Source Vertex",
    min_value=0,
    max_value=num_vertices - 1,
    value=0
)

run = st.sidebar.button(
    "▶ Run Dijkstra",
    use_container_width=True
)

# ------------------------------------------------
# Build Graph
# ------------------------------------------------

graph = {i: [] for i in range(num_vertices)}

try:

    for line in edge_text.strip().split("\n"):

        if line.strip():

            u, v, w = map(int, line.split())

            graph[u].append((v, w))

except:

    st.error("Invalid edge format.\nPlease use:\n\nu v weight")
    st.stop()

# ------------------------------------------------
# Execute
# ------------------------------------------------

if run:

    dist, prev = dijkstra(graph, source)

    # --------------------------------------------
    # Input Graph Table
    # --------------------------------------------

    st.subheader("Input Graph")

    input_data = []

    for u in graph:
        for v, w in graph[u]:
            input_data.append([u, v, w])

    input_df = pd.DataFrame(
        input_data,
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

    # --------------------------------------------
    # Shortest Path Table
    # --------------------------------------------

    st.subheader("Shortest Paths")

    result = []

    for vertex in range(num_vertices):

        path = reconstruct_path(
            prev,
            source,
            vertex
        )

        if path:
            path_str = " → ".join(map(str, path))
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

    df = pd.DataFrame(
        result,
        columns=[
            "Vertex",
            "Distance",
            "Shortest Path"
        ]
    )

    st.dataframe(
        df,
        use_container_width=True
    )

    # --------------------------------------------
    # Metrics
    # --------------------------------------------

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

    # --------------------------------------------
    # Distance Chart
    # --------------------------------------------

    st.subheader("Shortest Distance from Source")

    fig, ax = plt.subplots(figsize=(8, 4))

    distances = [
        0 if d == float("inf") else d
        for d in dist
    ]

    ax.bar(
        range(num_vertices),
        distances
    )

    ax.set_xlabel("Vertex")
    ax.set_ylabel("Distance")
    ax.set_title("Shortest Distance")

    st.pyplot(fig)

    # --------------------------------------------
    # Graph Visualization
    # --------------------------------------------

    st.subheader("Graph Visualization")

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

    edge_labels = nx.get_edge_attributes(
        G,
        "weight"
    )

    nx.draw_networkx_edge_labels(
        G,
        pos,
        edge_labels=edge_labels,
        ax=ax2
    )

    # Highlight Shortest Path Tree
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

    st.success("✅ Dijkstra Algorithm Executed Successfully.")