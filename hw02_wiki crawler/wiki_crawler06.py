# 專題作業二_維基百科爬蟲

def isChinese(word):    # 檢查是否為中文字
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
with open('D:/專題/hw02/myOutput.txt', 'w', encoding="utf-8") as fout:  # 開啟輸出檔案
    with open("D:/專題/hw02/zhwiki-latest-pages-articles.xml", "r", encoding="utf-8") as fin:  # 開啟輸入檔案
        for line in fin:
            if l % 1000000 == 0:    # 顯示進度，總共為178000000多行
                print(f"Line {l} complete!")

            length = len(line)
            isHyperLink = False
            i = 0
            while i < length:
                if isHyperLink == False:
                    if line[i] == '[' and line[i+1] == '[':  # 超連結文字開頭
                        i += 2
                        isHyperLink = True
                        link_text = ""
                        continue
                else:
                    if line[i] == "]" and line[i+1] == "]":  # 超連結文字結束
                        i += 2
                        isHyperLink = False
                        # 每出現一個字時，檢查有沒有在set中，如果沒有則寫進檔案
                        if isChinese(link_text) and not link_text in link_set:
                            fout.write(link_text+"\n")
                            link_set.add(link_text)
                        link_text = ""
                        continue
                    elif line[i] == ')' or line[i] == '）':  # 超連結文字結束(分全半形)
                        # 每出現一個字時，檢查有沒有在set中，如果沒有則寫進檔案
                        if isChinese(link_text) and not link_text in link_set:
                            fout.write(link_text+"\n")
                            link_set.add(link_text)
                        link_text = ""
                    elif line[i] == ':':    # 出現冒號就不是超連結文字
                        isHyperLink = False
                    elif line[i] == '|' or line[i] == '（' or line[i] == '（':  # 新的超連結文字開頭
                        # 每出現一個字時，檢查有沒有在set中，如果沒有則寫進檔案
                        if isChinese(link_text) and not link_text in link_set:
                            fout.write(link_text+"\n")
                            link_set.add(link_text)
                        link_text = ""
                    else:   # 其他讀取超連結文字的情況
                        if line[i] not in chineseMark:
                            link_text += line[i]
                i += 1
            l += 1

print(f"total word = {len(link_set)}")  # 全部的文字，總共有3950730個
print("---PROGRAM END---")
