# 專題作業03-取得角色名稱

from bs4 import BeautifulSoup
import requests

# 維基百科 <<射鵰英雄傳>> 頁面
url = "https://zh.wikipedia.org/wiki/%E5%B0%84%E9%B5%B0%E8%8B%B1%E9%9B%84%E5%82%B3"
my_header = {"accept-language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7"}

response = requests.get(url, headers=my_header)
soup = BeautifulSoup(response.text, "html.parser")
# print(soup.prettify())

# 找到底下電視劇角色的table
trs = soup.find("table", class_="wikitable").find_all("tr")

with open("charater_names.txt", "w") as file:
    # 第7行到最後一行是人物名稱
    for i in range(7, len(trs)):
        name = trs[i].find("td").text
        print(name)
        file.write(name+"\n")

print("PROGRAM END")
