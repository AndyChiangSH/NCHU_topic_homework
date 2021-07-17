# 專題作業03-Pyvis graph

import networkx as nx
import matplotlib.pyplot as plt
import csv
from pyvis.network import Network
import numpy as np


if __name__ == '__main__':  # main

    names_path = r"D:/專題/data/hw03/charater_names.txt"

    with open(names_path, "r", encoding="utf-8") as file:
        lines = file.readlines()
        names = tuple([line[:-1] for line in lines])

    # print(names)

    NG = nx.Graph()
    # NG.add_nodes_from(names)    # 空的點也會出來
    # print(NG.nodes())
    # print(NG.number_of_nodes())

    # 開啟 CSV 檔案
    with open('graph.csv', newline='') as csvfile:
        # 讀取 CSV 檔案內容
        rows = csv.reader(csvfile)

        # 以迴圈輸出每一列
        for index, row in enumerate(rows):
            if index != 0:
                NG.add_edge(row[0], row[1], value=int(row[2]))

    # for (u, v, wt) in NG.edges.data('weight'):
    #     print(f"({u}, {v}, {wt})")

    NT = Network(height='700px', width='100%',
                 bgcolor='#222222', font_color='white')
    NT.barnes_hut(gravity=-100000, central_gravity=0.5, spring_length=500)
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
        neibor_dic = dict()
        for neibor in neibors:
            neibor_dic[neibor] = NG[node['id']][neibor]['value']

        # print(neibor_dic)
        sorted_neibor_dic = dict(
            sorted(neibor_dic.items(), key=lambda item: item[1], reverse=True))
        # print(sorted_neibor_dic)

        for neibor in sorted_neibor_dic:
            title_text += f"<br>{neibor}: {NG[node['id']][neibor]['value']}"

        node['title'] = title_text + "</span>"

    # NT.toggle_hide_nodes_on_drag(True)
    # NT.set_edge_smooth("dynamic")
    # NT.show_buttons(filter_=['physics'])
    NT.inherit_edge_colors(True)
    NT.show('network.html')
