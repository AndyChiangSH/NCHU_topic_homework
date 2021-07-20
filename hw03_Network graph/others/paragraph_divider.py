# 專題作業03-切割文章段落

path = r"../src/test.txt"
paragraphs = list()


with open(path, "r", encoding="utf-8") as file:
    line = ""
    isParagraph = False
    while True:
        c = file.read(1)
        # print(f"c = {c}")
        if c == "":  # 讀到EOF
            break
        if isParagraph:
            if c == "\n":   # 如果是換行，轉換成非paragraph模式(空白行模式)
                isParagraph = False
                paragraphs.append(line)
                line = ""
            else:
                line += c
        else:
            if c != "\n" and c != "\u3000":  # 如果不是換行或全形空白，轉換成paragraph模式
                isParagraph = True
                line += c


# print(paragraphs)
for p in paragraphs:
    print("p = "+p)
