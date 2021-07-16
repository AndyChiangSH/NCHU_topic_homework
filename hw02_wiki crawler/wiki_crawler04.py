from xml.etree.ElementTree import iterparse
from collections import Counter


def parse_and_remove(filename, path):

    path_parts = path.split('/')
    doc = iterparse(filename, ('start', 'end'))
    # Skip the root element
    next(doc)
    tag_stack = []
    elem_stack = []
    for event, elem in doc:
        if event == 'start':
            tag_stack.append(elem.tag)
            elem_stack.append(elem)
        elif event == 'end':
            if tag_stack == path_parts:
                yield elem
                elem_stack[-2].remove(elem)
                try:
                    tag_stack.pop()
                    elem_stack.pop()
                except IndexError:
                    pass


path = "D:/專題/hw02/zhwiki-latest-pages-articles.xml"
# path = "D:/專題/hw02/wiki-one-page.xml"

potholes_by_zip = Counter()
data = parse_and_remove(path, 'row/row')

for pothole in data:
    potholes_by_zip[pothole.findall('page//a')] = 1

for zipcode, num in potholes_by_zip.most_common():
    print(zipcode, num)
