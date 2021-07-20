# 專題作業03-2D network graph with pyvis graph

import networkx as nx
import json
from pyvis.network import Network


if __name__ == '__main__':  # main

    names_path = r"../src/charater_names.txt"
    json_path = r"../data/graph_data.json"
    output_path = r"../result/website/2D_network.html"

    with open(names_path, "r", encoding="utf-8") as file:
        lines = file.readlines()
        names = tuple([line[:-1] for line in lines])

    NG = nx.Graph()
    # NG.add_nodes_from(names)    # 空的點也會出來

    # 讀取JSON檔
    with open(json_path, "r") as file:
        data = json.load(file)
        edges = data["links"]
        for edge in edges:
            edge_title = f"<span style='font-size: 8px'>{edge['source']} - {edge['target']}: {edge['value']}</span>"
            NG.add_edge(edge['source'], edge['target'],
                        value=int(edge['value']), title=edge_title)

    # for (u, v, wt) in NG.edges.data('weight'):
    #     print(f"({u}, {v}, {wt})")

    NT = Network(height='700px', width='100%',
                 bgcolor='#222222', font_color='white')
    NT.barnes_hut(gravity=-100000, central_gravity=0.5, spring_length=1000)
    NT.from_nx(NG)

    neighbor_map = NT.get_adj_list()
    for node in NT.nodes:
        neibors = neighbor_map[node['id']]
        adj = len(neibors)
        # print(f"{node['id']}: {adj}")
        if adj > 40:
            node['color'] = '#ff4a4a'   # red
        elif adj > 30:
            node['color'] = '#ffad3b'   # orange
        elif adj > 20:
            node['color'] = '#fff82b'   # yellow
        elif adj > 10:
            node['color'] = '#4fff52'   # green
        else:
            node['color'] = '#66a3ff'   # blue
        node['size'] = adj/2+5
        title_text = f"<span style='font-size: 8px'>{node['id']} has {adj} neighbors"
        node['title'] = title_text

    # NT.toggle_hide_nodes_on_drag(True)
    # NT.set_edge_smooth("discrete")
    # NT.show_buttons(filter_=['physics'])
    NT.inherit_edge_colors(True)
    NT.save_graph(output_path)
    # NT.show(output_path)

    print("2D network complete!")
