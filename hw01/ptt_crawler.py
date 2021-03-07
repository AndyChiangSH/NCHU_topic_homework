# 專題作業一_PTT八卦版爬蟲

from bs4 import BeautifulSoup
import requests
import json

# 基本參數
url = "https://www.ptt.cc/bbs/Gossiping/index.html"
payload = {
    'from': '/bbs/Gossiping/index.html',
    'yes': 'yes'
}
data = {}
num = 0

# request抓取頁面HTML
rs = requests.session()
response = rs.post("https://www.ptt.cc/ask/over18", data=payload)

for i in range(2):
    # print(url)
    response = rs.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    # print(soup.prettify())

    # 找出title的連結
    links = soup.find_all("div", class_="title")
    for link in links:
        if link.a != None:

            article_data = {}
            page_url = "https://www.ptt.cc/"+link.a["href"]

            # 進入文章頁面
            response = rs.get(page_url)
            result = BeautifulSoup(response.text, "html.parser")
            # print(soup.prettify())

            # 找出作者、標題、時間、留言
            main_content = result.find("div", id="main-content")
            article_info = main_content.find_all(
                "span", class_="article-meta-value")
            author = article_info[0].string  # 作者
            title = article_info[2].string  # 標題
            time = article_info[3].string   # 時間

            # contents = main_content.string

            # print(author)
            # print(title)
            # print(time)
            article_data["author"] = author
            article_data["title"] = title
            article_data["time"] = time

            # 將整段文字內容抓出來
            all_text = main_content.text
            # 以--切割，抓最後一個--前的所有內容
            pre_texts = all_text.split("--")[:-1]
            # 將前面的所有內容合併成一個
            one_text = "--".join(pre_texts)
            # 以\n切割，第一行標題不要
            texts = one_text.split("\n")[1:]
            # 將每列分行
            content = "\n".join(texts)

            # print(content)
            article_data["content"] = content

            # 一種留言一個列表
            comment_dic = {}
            push_dic = {}
            arrow_dic = {}
            shu_dic = {}

            # 抓出所有留言
            comments = main_content.find_all("div", class_="push")
            for index, comment in enumerate(comments):
                push_tag = comment.find(
                    "span", class_="push-tag").string   # 分類標籤
                push_userid = comment.find(
                    "span", class_="push-userid").string  # 使用者ID
                push_content = comment.find(
                    "span", class_="push-content").string   # 留言內容
                push_time = comment.find(
                    "span", class_="push-ipdatetime").string   # 留言時間

                # print(push_tag, push_userid, push_content, push_time)

                if push_tag == "推 ":
                    dict1 = {"push_userid": push_userid,
                             "push_content": push_content, "push_time": push_time}
                    push_dic[index] = dict1
                if push_tag == "→ ":
                    dict1 = {"push_userid": push_userid,
                             "push_content": push_content, "push_time": push_time}
                    arrow_dic[index] = dict1
                if push_tag == "噓 ":
                    dict1 = {"push_userid": push_userid,
                             "push_content": push_content, "push_time": push_time}
                    shu_dic[index] = dict1

            # print(push_dic)
            # print(arrow_dic)
            # print(shu_dic)
            # print("--------")
            comment_dic["推"] = push_dic
            comment_dic["→"] = arrow_dic
            comment_dic["噓"] = shu_dic
            article_data["comment"] = comment_dic

            # print(article_data)
            data[num] = article_data
            num += 1
            print("第 "+str(num)+" 篇文章完成!")

    url = "https://www.ptt.cc/"+soup.find("a", string="‹ 上頁")["href"]

# print(data)
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f)
