# 專題作業二_維基百科爬蟲

from bs4 import BeautifulSoup
import requests
import os


def wiki_search(keyword):
    url = f"https://zh.wikipedia.org/wiki/{keyword}"    # 維基百科頁面的關鍵字放在網址後面
    # 設定語言，繁中優先
    my_header = {"accept-language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7"}

    response = requests.get(url, headers=my_header)
    soup = BeautifulSoup(response.text, "html.parser")
    # print(soup.prettify())

    content_body = soup.find("div", id="bodyContent")
    first_class = content_body.find(
        "div", id="mw-content-text").find_all("div")[0].get("class")    # 抓取content text的第一個class

    if first_class[0] != "noarticletext":   # 如果該頁面存在

        links = content_body.select("p>a")  # 找出p底下的a

        links_set = set()

        for link in links:
            if link.get("rel") == None:  # 有rel通常是一些不相關的東西，所以把他們去除
                # print(link.text)
                links_set.add(link.text)    # 因為set有不重複之特性，所以把值存進set中

        print(f"共找到 {len(links_set)} 筆關鍵字")
        for i in links_set:
            print(i)

        if not os.path.exists("data"):  # 建資料夾
            os.mkdir("data")

        with open(f"data\\{keyword}.txt", "w", encoding="utf-8") as file:   # 寫檔，檔名為關鍵字
            for i in links_set:
                file.write(i+"\n")
    else:
        print("查無此頁")


# main
if __name__ == '__main__':
    # 輸入關鍵字，如果找的到則輸出連結，沒有則回應查無此頁
    keyword = input("請輸入搜尋關鍵字 = ")
    wiki_search(keyword)
