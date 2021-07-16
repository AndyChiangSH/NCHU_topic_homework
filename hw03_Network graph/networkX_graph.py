# 專題作業03-NetworkX graph

import networkx as nx
import matplotlib.pyplot as plt
import csv


if __name__ == '__main__':  # main

    names_path = r"D:/專題/data/hw03/charater_names.txt"

    with open(names_path, "r", encoding="utf-8") as file:
        lines = file.readlines()
        names = tuple([line[:-1] for line in lines])

    # print(names)

    NG = nx.Graph()
    NG.add_nodes_from(names)    # 空的點也會出來
    # print(NG.nodes())
    # print(NG.number_of_nodes())

    # 開啟 CSV 檔案
    with open('graph.csv', newline='') as csvfile:
        # 讀取 CSV 檔案內容
        rows = csv.reader(csvfile)

        # 以迴圈輸出每一列
        for index, row in enumerate(rows):
            if index != 0:
                NG.add_edge(row[0], row[1], weight=int(row[2]))

    for (u, v, wt) in NG.edges.data('weight'):
        print(f"({u}, {v}, {wt})")

    options = {
        'node_size': 50,
        'width': 0.2,
    }
    nx.draw_circular(NG, **options)
    # nx.draw_random(NG, **options)
    plt.show()
