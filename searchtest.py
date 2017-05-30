from urllib import request
from xml.dom.minidom import *
from xml.etree import ElementTree





serviceKey = 'Lg8o2pi2x5AWT0RIJ5XkNewd%2BtSXe63rr5za624JyZiO1TiQpbdNmDhonlj1zFMucI35WMs0idy66DCXSgi%2FvA%3D%3D'

response = request.urlopen('http://apis.data.go.kr/B552657/ErmctInsttInfoInqireService/getParmacyListInfoInqire?'
                            'serviceKey=Lg8o2pi2x5AWT0RIJ5XkNewd%2BtSXe63rr5za624JyZiO1TiQpbdNmDhonlj1zFMucI35WMs0idy66DCXSgi%2FvA%3D%3D'
                           '&Q0=%EC%84%9C%EC%9A%B8%ED%8A%B9%EB%B3%84%EC%8B%9C'
                           '&Q1=%EC%96%91%EC%B2%9C%EA%B5%AC'
                           '&pageNo=1&numOfRows=10').read()
tree = ElementTree.fromstring(response)
    # print(response)
itemElements = tree.getiterator("item")
    # print(itemElements)
for item in itemElements:
    age = item.findtext("dutyAddr")
    print(item.findtext("dutyName"))
    print(age)
