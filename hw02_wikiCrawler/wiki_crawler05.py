# 專題作業二_維基百科爬蟲

def isChinese(word):
    if len(word) == 0:
        return False
    for char in word:
        if not (char >= u"\u4E00" and char <= u"\u9FFF"):
            return False

    return True


chineseMark = "！？｡＂＃＄％＆＇（）＊＋，－／：；＜＝＞＠［＼］＾＿｀｛｜｝～｟｠｢｣､、〃》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟〰〾〿–—‘’‛“”„‟…‧﹏."

link_set = set()
l = 1
link_text = ""

print("---PROGRAM START---")
with open("D:/專題/hw02/zhwiki-latest-pages-articles.xml", "r", encoding="utf-8") as fin:  # 開啟檔案
    for line in fin:
        if l % 1000000 == 0:
            print("掃描完成第"+(str(l))+"行!")
        length = len(line)
        isHyperLink = False
        i = 0
        while i < length:
            if isHyperLink == False:
                if line[i] == '[' and line[i+1] == '[':
                    i += 2
                    isHyperLink = True
                    link_text = ""
                    continue
            else:
                if line[i] == "]" and line[i+1] == "]":
                    i += 2
                    isHyperLink = False
                    if isChinese(link_text):
                        link_set.add(link_text)
                    link_text = ""
                    continue
                elif line[i] == ')' or line[i] == '）':
                    if isChinese(link_text):
                        link_set.add(link_text)
                    link_text = ""
                elif line[i] == ':':
                    isHyperLink = False
                elif line[i] == '|' or line[i] == '（' or line[i] == '（':
                    if isChinese(link_text):
                        link_set.add(link_text)
                    link_text = ""
                else:
                    if line[i] not in chineseMark:
                        link_text += line[i]
            i += 1
        l += 1

with open('D:/專題/hw02/myOutput.txt', 'w', encoding="utf-8") as fout:  # 程式結束後，在一口氣存檔
    for link in link_set:
        fout.write(link+"\n")

print(f"total word = {len(link_set)}")
print("---PROGRAM END---")
