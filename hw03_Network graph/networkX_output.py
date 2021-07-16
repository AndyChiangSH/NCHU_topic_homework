# 專題作業03-切割文章段落

import networkx as nx
import matplotlib.pyplot as plt
import csv


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

    names_path = r"D:/專題/data/hw03/charater_names.txt"

    with open(names_path, "r", encoding="utf-8") as file:
        lines = file.readlines()
        names = tuple([line[:-1] for line in lines])

    # print(names)

    NG = nx.Graph()
    NG.add_nodes_from(names)
    # print(NG.nodes())
    # print(NG.number_of_nodes())

    for i in range(1, 5):
        path = f"D:/專題/data/hw03/0{i}.txt"
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

    # 開啟輸出的 CSV 檔案
    with open(r'D:/專題/data/hw03/graph.csv', 'w', newline='') as csvfile:
        # 建立 CSV 檔寫入器
        writer = csv.writer(csvfile)

        # 寫入一列資料
        writer.writerow(['u', 'v', 'weight'])

        for (u, v, wt) in NG.edges.data('weight'):
            # print(f"({u}, {v}, {wt})")
            writer.writerow([u, v, wt])
