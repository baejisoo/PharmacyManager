from urllib import request
from xml.dom.minidom import *
from xml.etree import ElementTree

serviceKey = 'Lg8o2pi2x5AWT0RIJ5XkNewd%2BtSXe63rr5za624JyZiO1TiQpbdNmDhonlj1zFMucI35WMs0idy66DCXSgi%2FvA%3D%3D'


response = request.urlopen('http://apis.data.go.kr/B552657/ErmctInsttInfoInqireService/getParmacyFullDown?'
                                'serviceKey=Lg8o2pi2x5AWT0RIJ5XkNewd%2BtSXe63rr5za624JyZiO1TiQpbdNmDhonlj1zFMucI35WMs0idy66DCXSgi%2FvA%3D%3D'
                                '&numOfRows=1000&pageSize=1').read()
tree = ElementTree.fromstring(response)
    #print(response)
itemElements = tree.getiterator("item")
    #print(itemElements)
for item in itemElements:
    age = item.find("dutyName")




