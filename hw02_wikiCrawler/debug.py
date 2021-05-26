# 專題作業二_維基百科爬蟲

from bs4 import BeautifulSoup
import requests
import os


def wiki_search(url):
    # 設定語言，繁中優先
    my_header = {"accept-language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7"}

    response = requests.get(url, headers=my_header)
    soup = BeautifulSoup(response.text, "html.parser")
    # print(soup.prettify())

    content_body = soup.find("div", id="bodyContent")
    first_class = content_body.find(
        "div", id="mw-content-text").find_all("div")[0].get("class")    # 抓取content text的第一個class

    if first_class[0] != "noarticletext":   # 如果該頁面存在

        contents = content_body.find_all(["p", "li"])  # 找出所有的p和li

        for content in contents:

            links = content.find_all("a")   # 找出底下的a

            for link in links:
                # 有rel通常是一些不相關的東西，所以把他們去除
                if link.get("rel") == None:
                    if link.get("href") != None:
                        if link.get("href")[0] != "#":
                            # print(link.text)
                            # 因為set有不重複之特性，所以把值存進set中
                            links_set.add(link.text)

        # print(f"共找到 {len(links_set)} 筆關鍵字")
        # for i in links_set:
        #     print(i)
    else:
        print("查無此頁")


# main
if __name__ == '__main__':
    print("---PROGRAM START---")
    keyword = input("Enter the keyword: ")

    links_set = set()

    my_header = {"accept-language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7"}
    page_url = f"https://zh.wikipedia.org/wiki/{keyword}"
    # print(page_url)

    wiki_search(page_url)

    with open(f"D:/專題/hw02/debug.txt", "w", encoding="utf-8") as file:   # 寫檔
        for i in links_set:
            print(i)
            file.write(i+"\n")

    print("---PROGRAM END---")
