# 專題作業03-計算人物間關係並產出json檔

import networkx as nx
import matplotlib.pyplot as plt
import csv
import json


def names_in_paragraph(paragraph):  # 尋找段落中出現的人名
    # print(paragraph)
    appear_names = list()
    for name in names:
        if name in paragraph:
            appear_names.append(name)

    for i in range(len(appear_names)):
        first_name = appear_names[i]
        for j in range(i+1, len(appear_names)):
            second_name = appear_names[j]
            # print(f"[{first_name}, {second_name}]")
            if NG.has_edge(first_name, second_name):
                NG[first_name][second_name]["weight"] += 1
            else:
                NG.add_edge(first_name, second_name, weight=1)


if __name__ == '__main__':  # main

    names_path = r"src/charater_names.txt"
    json_path = r"data/graph_data.json"

    with open(names_path, "r", encoding="utf-8") as file:
        lines = file.readlines()
        names = tuple([line[:-1] for line in lines])

    # print(names)

    NG = nx.Graph()
    NG.add_nodes_from(names)
    # print(NG.nodes())
    # print(NG.number_of_nodes())

    for i in range(1, 5):
        path = f"src/0{i}.txt"
        print(f"Read {path} now...")

        with open(path, "r", encoding="utf-8") as file:
            paragraph = ""
            isParagraph = False
            while True:
                c = file.read(1)
                # print(f"c = {c}")
                if c == "":  # 讀到EOF
                    break
                if isParagraph:
                    if c == "\n":   # 如果是換行，轉換成非paragraph模式(空白行模式)
                        isParagraph = False
                        names_in_paragraph(paragraph)
                        paragraph = ""
                    else:
                        paragraph += c
                else:
                    if c != "\n" and c != "\u3000":  # 如果不是換行或全形空白，轉換成paragraph模式
                        isParagraph = True
                        paragraph += c

    # 產生nodes list
    nodes = list()
    for node in NG.nodes:
        adj = NG.degree[node]
        if adj > 40:
            color = '#ff4a4a'   # red
        elif adj > 30:
            color = '#ffad3b'   # orange
        elif adj > 20:
            color = '#fff82b'   # yellow
        elif adj > 10:
            color = '#4fff52'   # green
        elif adj > 0:
            color = '#66a3ff'   # blue
        val = adj

        if adj != 0:
            nodes.append({"id": node, "color": color, "value": val})

    # print(nodes)
    sorted_nodes = sorted(nodes, key=lambda k: k['value'], reverse=True)
    # print(sorted_nodes)

    # 產生links list
    links = list()

    for (u, v, wt) in NG.edges.data('weight'):
        # print(f"({u}, {v}, {wt})")
        links.append({"source": u, "target": v, "value": wt})

    # print(links)
    sorted_links = sorted(links, key=lambda k: k['value'], reverse=True)
    # print(sorted_links)

    # 合併nodes和links
    json_data = {"nodes": sorted_nodes, "links": sorted_links}

    # 匯出JSON檔
    with open(json_path, 'w', encoding='utf-8') as file:
        json.dump(json_data, file)

    print("JSON file complete")
