from urllib import request
from xml.dom.minidom import *
from xml.etree import ElementTree

serviceKey = 'serviceKey=%2FINbOZE%2BzCgNiixKdMsdarrLzI8E5HSyt%2B6YSNlGBUevwhNWO09GQ3DxEIMkJf5mUg7zMJCDJe8G3afJdFInlQ%3D%3D'


response = request.urlopen('http://apis.data.go.kr/B552657/ErmctInsttInfoInqireService/getParmacyListInfoInqire?'
                                'serviceKey=%2FINbOZE%2BzCgNiixKdMsdarrLzI8E5HSyt%2B6YSNlGBUevwhNWO09GQ3DxEIMkJf5mUg7zMJCDJe8G3afJdFInlQ%3D%3D'
                           'bgnde=20140601&endde=20170521&upkind=417000&numOfRows=10&pageSize=10'
                           ).read()
tree = ElementTree.fromstring(response)
    #print(response)
itemElements = tree.getiterator("item")
    #print(itemElements)
for item in itemElements:
    age = item.find("dutyName")
    print(age.text)