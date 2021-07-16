# 擷取超連結文字做成中文IK斷詞
def checkChinese(myStr):
    if len(myStr) == 0:  # 如果是空字串就設成false
        return False
    for char_ in myStr:  # 看是不是整個字串都是中文
        if not char_ >= u'\u4E00' and char_ <= u'\u9FFF':
            return False
    return True


chineseMark = set(
    "！？｡＂＃＄％＆＇（）＊＋，－／：；＜＝＞＠［＼］＾＿｀｛｜｝～｟｠｢｣､、〃》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟〰〾〿–—‘’‛“”„‟…‧﹏.")

fout = open('D:/專題/hw02/output.txt', 'w', encoding="utf-8")
mySet = set()
c = 1  # 記錄第幾行
myText = ""
with open("D:/專題/hw02/zhwiki-latest-pages-articles.xml", mode="r", encoding="utf-8") as file:  # 開啟檔案
    for line in file:  # 每次讀取一行
        if c % 1000000 == 0:  # 提醒一下程式有正常在跑
            print("掃描完成第"+(str(c))+"行!")
        length = len(line)
        i = 0
        scanningHyperLinkText = False
        while i < length:
            if scanningHyperLinkText == False:  # 開始超連結文字
                if(line[i] == '[' and line[i+1] == '['):
                    i += 2  # 跳過第2個[
                    scanningHyperLinkText = True
                    myText = ""
                    continue
            else:
                if(line[i] == ']' and line[i+1] == ']'):  # 文字結束
                    i += 2  # 跳過第2個]
                    scanningHyperLinkText = False
                    isChinese = checkChinese(myText)
                    if isChinese == True:  # 是中文就加到set
                        mySet.add(myText)
                    myText = ""
                    continue
                elif line[i] == ')' or line[i] == '）':  # 文字結束(有全形半行之分)
                    isChinese = checkChinese(myText)
                    if isChinese == True:  # 是中文就加到set
                        mySet.add(myText)
                    myText = ""
                elif line[i] == ':':  # 有出現':'就不是超連結文字
                    scanningHyperLinkText = False
                # 開始另外一個詞(有全形半行之分)
                elif line[i] == '|' or line[i] == '（' or line[i] == '（':
                    isChinese = checkChinese(myText)
                    if isChinese == True:  # 是中文就加到set
                        mySet.add(myText)
                    myText = ""
                else:  # 其他加到myText的情況
                    if line[i] not in chineseMark:
                        myText += line[i]
            i += 1
        c += 1

print(len(mySet))

for element in mySet:  # 寫入檔案
    fout.write(element + "\n")

fout.close()
