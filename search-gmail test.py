from PyQt4.QtGui import *
from urllib import request
import urllib.parse
#import gmail
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
    global sidoName, sigunguName, day, order, pharmacyName

    sidoNameKor = input("시/도 입력: ")
    sidoName = urllib.parse.quote(sidoNameKor)

    sigunguNameKor = input("시/군/구 입력: ")
    sigunguName = urllib.parse.quote(sigunguNameKor)

    dayKor = input("영업 요일 입력(월/화/수/목/금/토/일/공휴일): ")
    if(dayKor=="월"):
        dayKor = "1"
    elif(dayKor == "화"):
        dayKor ="2"
    elif(dayKor == "수"):
        dayKor = "3"
    elif(dayKor == "목"):
        dayKor = "4"
    elif(dayKor == "금"):
        dayKor = "5"
    elif (dayKor == "토"):
        dayKor = "6"
    elif(dayKor == "일"):
        dayKor = "7"
    elif (dayKor == "공휴일"):
        dayKor = "8"
    day=urllib.parse.quote(dayKor)

    response_body = request.urlopen('http://apis.data.go.kr/B552657/ErmctInsttInfoInqireService/getParmacyListInfoInqire?'
                                    +ServiceKey+
                                    '&Q0='+sidoName+ '&Q1=' + sigunguName + '&QT='+day +'&pageNo=1&numOfRows=20').read()
    tree = ElementTree.fromstring(response_body)
    print(response_body)
    itemElements = tree.getiterator("item")
    print(itemElements)
    for item in itemElements:
        dutyName = item.find("dutyName")
        dutyAddr = item.find("dutyAddr")
        dutyTimeS = item.find("dutyTime"+day+"s")
        dutyTimeC = item.find("dutyTime"+day+"c")
        print("약국 이름: " + dutyName.text)
        print("약국 주소: " + dutyAddr.text)
        if (item.find("dutyTime" + day + "s") != None and item.find("dutyTime" + day + "c") != None):
            print("약국 영업 시간: " + dutyTimeS.text+"~" + dutyTimeC.text)

    print("---------------------")
    order = input("1. 인근 약국 찾기 2. 이메일: ")

    if(order == '1'):
        pharmacyName = input("약국 이름:")
        pharmacyName1 = pharmacyName
        pharmacyName = urllib.parse.quote(pharmacyName)

        response_body = request.urlopen(
            'http://apis.data.go.kr/B552657/ErmctInsttInfoInqireService/getParmacyListInfoInqire?'
            + ServiceKey +
            '&Q0=' + sidoName + '&Q1=' + sigunguName + '&ORD=ADDR&numOfRows=500').read()
        tree = ElementTree.fromstring(response_body)
        itemElements = tree.getiterator("item")
        count = 0
        bool = False
        for item in itemElements:
            if(pharmacyName1 == item.findtext("dutyName")):
                bool = True
            if(bool == 1 and pharmacyName1 != item.findtext("dutyName")):
                dutyName = item.find("dutyName")
                dutyAddr = item.find("dutyAddr")
                dutyTimeS = item.find("dutyTime" + day + "s")
                dutyTimeC = item.find("dutyTime" + day + "c")
                print("약국 이름: " + dutyName.text)
                print("약국 주소: " + dutyAddr.text)
                if(item.find("dutyTime" + day + "s") != None and item.find("dutyTime" + day + "c") != None):
                    print("약국 영업 시간: " + dutyTimeS.text + "~" + dutyTimeC.text)
                count+=1
            if(count > 10):
                bool = False
                break

    elif(order == '2'):
        print("22")



while(1):
    searchPharmacy()

