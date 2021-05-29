# 專題作業二_維基百科爬蟲_ElementTree

import xml.etree.ElementTree as ET

# tree = ET.parse('D:/專題/hw02/zhwiki-latest-pages-articles.xml')  # dead program...
root = tree.getroot()

# links = root.findall(".//a")
for link in root.iter("a"):
    print(link.text)
