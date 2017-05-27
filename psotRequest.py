
from urllib import request
from urllib import urlencode
from xml.dom.minidom import *
from xml.etree import ElementTree

url = 'http://apis.data.go.kr/B552657/ErmctInsttInfoInqireService/getParmacyFullDown'
queryParams = '?' + urlencode({ quote_plus('ServiceKey') : '5pNTeplk5p7OZJvaN66WO8U%2FX%2BNfJvN8o%2F6ZrqREeCY7skab0O2HJgP2kqbjK%2BXth3O%2FmEa8x4pkFcWgToLs9g%3D%3D', quote_plus('ServiceKey') : '-', quote_plus('pageNo') : '1', quote_plus('numOfRows') : '10' })

request = Request(url + queryParams)
request.get_method = lambda: 'GET'
response_body = urlopen(request).read()
print(response_body)



