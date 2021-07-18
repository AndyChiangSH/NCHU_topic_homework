import networkx as nx
import matplotlib.pyplot as plt

# # 建立空的圖
# G = nx.Graph()

# # 新增節點
# G.add_node(1)
# G.add_nodes_from([2, 3, 4])

# # 新增邊
# G.add_edge(1, 2)
# G.add_edges_from([(3, 4), (1, 3)])

# # 顯示圖的資訊
# print(G.number_of_nodes())
# print(G.number_of_edges())

# print(list(G.nodes))
# print(list(G.edges))
# print(list(G.adj[4]))
# print(G.degree[4])

# # 移除節點or邊
# G.remove_node(4)
# G.remove_edge(1, 2)

# print(list(G.nodes))
# print(list(G.edges))

# print("Graph from constuctor")
# H = nx.DiGraph(G)
# print(list(H.nodes))
# print(list(H.edges))

# print("Graph from edges list constuctor")
# edgeslist = [(1, 2), (1, 3), (2, 4)]
# H = nx.Graph(edgeslist)
# print(list(H.nodes))
# print(list(H.edges))

# # 取得屬性值
# G = nx.Graph([(1, 2, {"color": "yellow"})])
# print(G[1])
# print(G[1][2])
# print(G.edges[1, 2])

# # 篩選屬性值
# WG = nx.Graph()
# WG.add_weighted_edges_from(
#     [(1, 2, 0.125), (1, 3, 0.75), (2, 4, 1.2), (3, 4, 0.375)])
# for (u, v, wt) in WG.edges.data('weight'):
#     if wt > 0.5:
#         print(f"({u}, {v}, {wt:.3})")

# # Graph屬性
# G = nx.Graph(day="Friday")
# print(G.graph)
# print(G.graph["day"])

# # Node屬性
# G.add_node(1, time="6:00pm")
# print(G.nodes[1])
# print(G.nodes[1]["time"])

# # Edge屬性
# G.add_edge(1, 2, weight=2.1)
# print(G[1][2])
# print(G[1][2]["weight"])

# # 有向圖(Direct Graph)
# DG = nx.DiGraph()
# DG.add_weighted_edges_from([(1, 2, 0.5), (3, 1, 0.75), (4, 1, 0.25)])
# print(DG.out_edges(1))
# print(DG.in_edges(1))
# print(DG.out_degree(1))
# print(DG.in_degree(1))
# print(list(DG.successors(1)))
# print(list(DG.predecessors(1)))

# 分析圖
# G = nx.Graph()
# G.add_edges_from([(1, 2), (1, 3)])
# G.add_node(4)
# print(list(nx.connected_components(G)))

# options = {
#     'node_color': 'blue',
#     'node_size': 200,
#     'width': 1,
# }
# G = nx.petersen_graph()
# nx.draw_shell(G, nlist=[range(5, 10), range(5)],
#               with_labels=True, font_weight='bold', **options)
# # plt.show()
# plt.savefig("fig1.png")

G = nx.Graph()
G.add_edge(1, 2, weight=1)
G[1][2]["weight"] += 1
G[1][2]["weight"] += 1
print(G[1][2]["weight"])
