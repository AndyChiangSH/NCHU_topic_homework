# 專題作業03-切割文章段落

#
def names_in_paragraph(paragraph):
    # print(paragraph)
    appear_names = list()
    for name in names:
        if name in paragraph:
            appear_names.append(name)

    print(appear_names)


if __name__ == '__main__':  # main

    path = r"D:/專題/data/hw03/test.txt"
    names_path = r"D:/專題/data/hw03/charater_names.txt"

    with open(names_path, "r", encoding="utf-8") as file:
        lines = file.readlines()
        names = tuple([line[:-1] for line in lines])

    # print(names)

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
