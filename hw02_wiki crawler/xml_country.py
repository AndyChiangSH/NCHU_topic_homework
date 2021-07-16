import xml.etree.ElementTree as ET

tree = ET.parse('D:/專題/hw02/country.xml')
root = tree.getroot()

# print(root)

# print(root[0][1].text)

# for child in root:
#     print(child.tag, child.attrib)

# for neighbor in root.iter('neighbor'):
# print(neighbor.attrib)

# for country in root.findall('country'):
#     rank = country.find('rank').text
#     name = country.get('name')
#     print(name, rank)

# for rank in root.iter("rank"):
#     new_rank = int(rank.text)
#     rank.text = str(new_rank+1)
#     rank.attrib["update"] = "yes"
#     tree.write("D:/專題/hw02/new.xml", encoding="UTF-8")

# elms = root.findall(".")
# elms = root.findall("./country/neighbor")
# elms = root.findall(".//year/..[@name='Singapore']")
# elms = root.findall(".//*[@name='Singapore']/year")
elms = root.findall(".//neighbor[2]")

for elm in elms:
    print(elm.attrib)
