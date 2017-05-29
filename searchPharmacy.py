from urllib import request
import urllib.parse
from xml.dom.minidom import *
from xml.etree import ElementTree

ServiceKey = 'ServiceKey=1td22cJml3Qk4BuSNgwhWXUk2xtS8zrLx0n0OfwQHdcn5HvvOvAv9UOJ6qSztOTbtrI5ODfdxzXhgvC5NJWxvQ%3D%3D'

def printPharmacy():
    response_body = request.urlopen('http://apis.data.go.kr/B552657/ErmctInsttInfoInqireService/getParmacyFullDown?'
                                    'ServiceKey=1td22cJml3Qk4BuSNgwhWXUk2xtS8zrLx0n0OfwQHdcn5HvvOvAv9UOJ6qSztOTbtrI5ODfdxzXhgvC5NJWxvQ%3D%3D'
                                    '&pageNo=1&numOfRows=50').read()
    tree = ElementTree.fromstring(response_body)
    print(response_body)
    itemElements = tree.getiterator("item")
    print(itemElements)
    for item in itemElements:
        dutyName = item.find("dutyName")
        print(dutyName.text)


def searchPharmacy():
    global sidoName, sigunguName, order, pharmacyName

    sidoNameKor = input("시/도 입력: ")
    sidoName = urllib.parse.quote(sidoNameKor)

    sigunguNameKor = input("시/군/구 입력: ")
    sigunguName = urllib.parse.quote(sigunguNameKor)

    response_body = request.urlopen('http://apis.data.go.kr/B552657/ErmctInsttInfoInqireService/getParmacyListInfoInqire?'
                                    +ServiceKey+
<<<<<<< HEAD
                                    '&Q0='+sidoName+ '&Q1=' + sigunguName + '&pageNo=1&numOfRows=10').read()
=======
                                    '&Q0='+sidoName+ '&Q1=' + sigunguName + '&QT=1&pageNo=1&numOfRows=10').read()
>>>>>>> origin/master
    tree = ElementTree.fromstring(response_body)
    print(response_body)
    itemElements = tree.getiterator("item")
    print(itemElements)
    for item in itemElements:
        dutyName = item.find("dutyName")
        dutyAddr = item.find("dutyAddr")
        print(item.findtext("postCdn1"))
        print(item.findtext("postCdn2"))
        print(dutyName.text)
        print(dutyAddr.text)

    print("---------------------")
    order = input("1. 인근 약국 찾기 2. 나가기: ")

    if(order == '1'):
        pharmacyName = input("약국 이름:")
        pharmacyName1 = pharmacyName
        pharmacyName = urllib.parse.quote(pharmacyName)

<<<<<<< HEAD
        response_body = request.urlopen(
            'http://apis.data.go.kr/B552657/ErmctInsttInfoInqireService/getParmacyListInfoInqire?'
            + ServiceKey +
            '&Q0=' + sidoName + '&Q1=' + sigunguName  + '&QN=' + pharmacyName+ '&pageNo=1&numOfRows=10').read()
        tree = ElementTree.fromstring(response_body)
        itemElements = tree.getiterator("item")
        for item in itemElements:
            post1 = int(item.findtext("postCdn1"))
            post2 = int(item.findtext("postCdn2"))
            post2 = post2 // 10
            break

        response_body = request.urlopen(
            'http://apis.data.go.kr/B552657/ErmctInsttInfoInqireService/getParmacyListInfoInqire?'
            + ServiceKey +
            '&Q0=' + sidoName + '&Q1=' + sigunguName + '&ORD=ADDR&numOfRows=1000').read()
        tree = ElementTree.fromstring(response_body)
        itemElements = tree.getiterator("item")
        count = 0
        for item in itemElements:
            post1_1 = int(item.findtext("postCdn1"))
            post2_2 = int(item.findtext("postCdn2"))
            post2_2 = post2_2 // 10
            if(post1 == post1_1 and post2 == post2_2 and pharmacyName1 != item.findtext("dutyName")):
                dutyName = item.find("dutyName")
                dutyAddr = item.find("dutyAddr")
                print(dutyName.text)
                print(dutyAddr.text)
                count+=1
            if(count > 10):
                break




=======
>>>>>>> origin/master
searchPharmacy()
