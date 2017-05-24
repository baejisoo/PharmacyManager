from urllib import request
from xml.dom.minidom import *
from xml.etree import ElementTree

serviceKey = 'ServiceKey=1td22cJml3Qk4BuSNgwhWXUk2xtS8zrLx0n0OfwQHdcn5HvvOvAv9UOJ6qSztOTbtrI5ODfdxzXhgvC5NJWxvQ%3D%3D'

def print10():
    response_body = request.urlopen('http://apis.data.go.kr/B552657/ErmctInsttInfoInqireService/getParmacyBassInfoInqire?'
                                    'ServiceKey=1td22cJml3Qk4BuSNgwhWXUk2xtS8zrLx0n0OfwQHdcn5HvvOvAv9UOJ6qSztOTbtrI5ODfdxzXhgvC5NJWxvQ%3D%3D'
                                    '').read()
    tree = ElementTree.fromstring(response_body)
    print(response_body)
    itemElements = tree.getiterator("item")
    print(itemElements)
    for item in itemElements:
        dutyName = item.find("dutyName")
        print(dutyName.text)

print10()