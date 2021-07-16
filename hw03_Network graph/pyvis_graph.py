# 專題作業03-Pyvis graph

import networkx as nx
import matplotlib.pyplot as plt
import csv
from pyvis.network import Network


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
        print(f"{node['id']} neighbor:")
        print(neighbor_map[node['id']])
        node['value'] = len(neighbor_map[node['id']])

    # NT.show_buttons(filter_=['physics'])
    NT.show('network.html')