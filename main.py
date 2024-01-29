import networkx as nx
import matplotlib.pyplot as plt
from problems import get_reductions, Reduction
import pyvis
import matplotlib


def main():
    npc_map = nx.DiGraph()

    reductions: list[Reduction] = get_reductions()
    for reduction in reductions:
        npc_map.add_edge(
            reduction.source, reduction.target, description=reduction.description)
    net = pyvis.network.Network(notebook=True, cdn_resources='remote', directed=True,
                                height="1000px", width="100%", bgcolor="#e8f1ff", font_color="#000c1f")
    net.force_atlas_2based()
    degree_cent = nx.katz_centrality(npc_map)
    closeness_cent = nx.closeness_centrality(npc_map)

    best_closeness = max(closeness_cent.values())
    worst_closeness = min(closeness_cent.values())

    max_size = 30
    min_size = 5

    max_centrality = max(degree_cent.values())
    min_centrality = min(degree_cent.values())

    net.add_node("Size", label="Size", title="Node size ~ Degree",
                 size=15, color="#348feb", physics=False, x=-1000, y=-300)
    # node that say that the color of the node is the weight value
    net.add_node("Color", label="Color", title="Node color ~ Closeness",
                 size=15, color="#348feb", physics=False, x=-1000, y=-200)

    for i, node in enumerate(npc_map.nodes):
        node_color_based_on_weight = matplotlib.colors.to_hex(plt.cm.Blues(
            (closeness_cent[node] - worst_closeness) / (best_closeness - worst_closeness), 1))
        net.add_node(node.name, label=f"{node.name}", title=f"{node.descirption} | Closeness={closeness_cent[node]:.2f} | Degree={degree_cent[node]:.2f}",
                     size=min_size + (max_size - min_size) * (degree_cent[node] - min_centrality) / (max_centrality - min_centrality), color=node_color_based_on_weight)

    for edge in npc_map.edges:
        net.add_edge(edge[0].name, edge[1].name,
                     title=npc_map.edges[edge]["description"])

    net.show("index.html")


if __name__ == "__main__":
    main()
