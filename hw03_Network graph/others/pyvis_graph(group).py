# 專題作業03-Pyvis graph

import networkx as nx
import matplotlib.pyplot as plt
import csv
from pyvis.network import Network
import numpy as np


if __name__ == '__main__':  # main

    names_path = r"../src/charater_names.txt"
    csv_path = r"../data/graph_data.csv"

    with open(names_path, "r", encoding="utf-8") as file:
        lines = file.readlines()
        names = tuple([line[:-1] for line in lines])

    # print(names)

    NG = nx.Graph()
    # NG.add_nodes_from(names)    # 空的點也會出來
    # print(NG.nodes())
    # print(NG.number_of_nodes())

    # 開啟 CSV 檔案
    with open(csv_path, newline='') as csvfile:
        # 讀取 CSV 檔案內容
        rows = csv.reader(csvfile)

        # 以迴圈輸出每一列
        for index, row in enumerate(rows):
            if index != 0:
                edge_title = f"<span style='font-size: 8px'>{row[0]} - {row[1]}: {row[2]}</span>"
                NG.add_edge(row[0], row[1], value=int(
                    row[2]), title=edge_title)

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
            node['group'] = '1'   # red
        elif adj > 30:
            node['group'] = '2'   # orange
        elif adj > 20:
            node['group'] = '3'   # yellow
        elif adj > 10:
            node['group'] = '4'   # green
        else:
            node['group'] = '5'   # blue
        node['size'] = adj/2+5
        title_text = f"<span style='font-size: 8px'>{node['id']} has {adj} neighbors"
        node['title'] = title_text

    # NT.toggle_hide_nodes_on_drag(True)
    # NT.set_edge_smooth("discrete")
    # NT.show_buttons(filter_=['physics'])
    NT.inherit_edge_colors(True)
    NT.save_graph('network.html')
    NT.show('network.html')
