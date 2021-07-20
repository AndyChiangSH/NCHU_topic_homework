from pyvis.network import Network

net = Network()

nodes = ["a", "b", "c", "d"]
net.add_nodes(nodes)
print(net.get_node("c"))

net.add_edge("a", "b")
net.add_edge("b", "c", 5)
