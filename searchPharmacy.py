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
    global sidoName, sigunguName

    sidoNameKor = input("시/도 입력: ")
    sidoName = urllib.parse.quote(sidoNameKor)
    response_body = request.urlopen('http://apis.data.go.kr/B552657/ErmctInsttInfoInqireService/getParmacyListInfoInqire?'
                                    +ServiceKey+
                                    '&Q0='+sidoName+'&QT=1&pageNo=1&numOfRows=10').read()
    tree = ElementTree.fromstring(response_body)
    print(response_body)
    itemElements = tree.getiterator("item")
    print(itemElements)
    for item in itemElements:
        dutyName = item.find("dutyName")
        dutyAddr = item.find("dutyAddr")
        print(dutyName.text)
        print(dutyAddr.text)

    sigunguNameKor = input("시/군/구 입력: ")
    sigunguName = urllib.parse.quote(sigunguNameKor)
    response_body = request.urlopen(
        'http://apis.data.go.kr/B552657/ErmctInsttInfoInqireService/getParmacyListInfoInqire?'
        + ServiceKey +
        '&Q0=' + sidoName + '&Q1=' + sigunguName + '&QT=1&pageNo=1&numOfRows=10').read()
    tree = ElementTree.fromstring(response_body)
    print(response_body)
    itemElements = tree.getiterator("item")
    print(itemElements)
    for item in itemElements:
        dutyName = item.find("dutyName")
        dutyAddr = item.find("dutyAddr")
        print(dutyName.text)
        print(dutyAddr.text)


searchPharmacy()

def searchShelter():
    global sido_num, sigungu_num

    print("==========보호소 검색==========")
    sido = input("시/도를 입력하세요: ")

    url_sido = 'http://openapi.animal.go.kr/openapi/service/rest/abandonmentPublicSrvc/sido?' + ServiceKey
    response = request.urlopen(url_sido).read()
    #print(response)

    tree = ElementTree.fromstring(response)
    itemElements = tree.getiterator("item")
    for item in itemElements:
        name = item.find('orgdownNm')
        sido_name = name.text
        if sido_name == sido:
            ret = item.find("orgCd")
            sido_num = ret.text
            #print(sido_num)

    sigungu = input("시/군/구를 입력하세요: ")
    url_sigungu = 'http://openapi.animal.go.kr/openapi/service/rest/abandonmentPublicSrvc/sigungu?'+ServiceKey+'&upr_cd=' + sido_num
    response = request.urlopen(url_sigungu).read()
    #print(response)
    tree = ElementTree.fromstring(response)
    itemElements = tree.getiterator("item")
    for item in itemElements:
        name = item.find('orgdownNm')
        sigungu_name = name.text
        if sigungu_name == sigungu:
            ret = item.find("orgCd")
            sigungu_num = ret.text
            #print(sido_num)

    url_shelter = 'http://openapi.animal.go.kr/openapi/service/rest/abandonmentPublicSrvc/shelter?'+ServiceKey+'&upr_cd='+sido_num+'&org_cd='+sigungu_num
    response = request.urlopen(url_shelter).read()
    #print(response)
    tree = ElementTree.fromstring(response)
    itemElements = tree.getiterator("item")
    print('보호소 목록: ')
    for item in itemElements:
        name = item.find('careNm')
        print(name.text)
