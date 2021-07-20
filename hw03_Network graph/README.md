# hw03_Network graph

hw03 - 射鵰英雄傳人物關係圖

###### tags: `專題`

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FAndyChiangSH%2FNCHU_topic_homework%2Ftree%2Fmaster%2Fhw03_Network%2520graph&count_bg=%233754FF&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=%E7%80%8F%E8%A6%BD%E4%BA%BA%E6%95%B8&edge_flat=false)](https://hits.seeyoufarm.com)

## Website
[網頁連結](https://andychiangsh.github.io/NCHU_topic_homework/hw03_Network%20graph/result/website/main.html)

![](https://i.imgur.com/6xcminM.png)

![](https://i.imgur.com/Or0f29Z.png)


* 切換2D和3D視角
* 可放大縮小、旋轉、拖曳圖上的點
* 節點的Degree越大，圓點就越大。
* 邊的Weight越大，線條就越粗。
* 可切換nodes和edges的資料
* 可調整數字滑桿設定顯示前N筆資料(從大排到小)

## Usage
1. Clone或下載hw03_Network graph資料夾。
2. 進入main資料夾。
3. 執行 `character_name.py`，自動爬下射鵰英雄傳的人物清單 `src/charater_names_new.txt`，手動刪除或加入其他人物並另存為`src/charater_names.txt`。
4. 執行 `json_generator.py`，將小說中的人物繪製成關係圖，如果兩個人出現在相同段落，則兩個人中間的邊權重+1。最後匯出成JSON格式 `graph_data.json`。
5. 執行 `2D_network.py`，輸入 `graph_data.json` 並繪製成2D網路圖，輸出為 `2D_network.html`。
6. `3D_network.html`，3D網路圖是用JavaScript在load `main.html` 的時候繪製，這部分不需要使用者操作。
7. 開啟 `result/website/main.html`，就可以看到網頁的畫面了。

## Document
### main：主執行程序
* `2D_network.py`：輸入json檔並繪製2D網路圖。
* `character_name.py`：自動爬取射鵰英雄傳的人物名稱清單。
* `csv_generator.py`：計算人物間關係的權重，並以csv格式輸出人物關係圖資料(非必要)。
* `json_generator.py`：計算人物間關係的權重，並以json格式輸出人物關係圖資料。

### src：來源資料
* `01~04.txt`：對應到射鵰英雄傳的第一部到第四部，可以全部合在同一份txt檔中，也可以置換成其他部小說。
* `charater_names.txt`：計算人物間關係時讀取的人物名稱清單。
* `charater_names_new.txt`：爬蟲自動產生的清單。

### data：關係圖資料
* `graph_data.csv`：執行`csv_generator.py`後輸出的資料。
* `graph_data.json`：執行`json_generator.py`後輸出的資料。

### result：顯示結果
#### website：前端展示用網頁
* `main.html`：主展示用網頁。
* `2D_network.html`：2D人物關係圖。
* `3D_network.html`：3D人物關係圖。

##### css：放一些網頁需要的css library
##### js：放一些需要的js library
##### font：書法字體
##### resource：網頁icon

### others：其餘在開發過程中的東西


## Reference
* Novel Soruce：[好讀 - 金庸《射鵰英雄傳》](http://www.haodoo.net/?M=book&P=55#!)
* Charater List：[維基百科 - 射鵰英雄傳](https://zh.wikipedia.org/wiki/%E5%B0%84%E9%B5%B0%E8%8B%B1%E9%9B%84%E5%82%B3)
* Python Graph：[NetworkX](https://networkx.org/documentation/stable/index.html)
* 2D Network Rendering：[pyvis](https://pyvis.readthedocs.io/en/latest/index.html)
* 3D Network Rendering：[3d-force-graph](https://vasturiano.github.io/3d-force-graph/)
* jQuery：[jQuery](https://jquery.com/)
* Slider：[jQuery Slider](https://jqueryui.com/slider/)
* Bootstrap：[Bootstrap](https://getbootstrap.com/)
* 書法字體：[王漢宗 48 套自由字型](https://briian.com/290/)

---

2021/07/20 made by Andy Chiang