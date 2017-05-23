import urllib.parse
import urllib.request

url = 'http://apis.data.go.kr/B552657/ErmctInsttInfoInqireService/getParmacyFullDown'
queryParams = '?' + urllib.parse.urlencode({ urllib.parse.quote('ServiceKey') : '5pNTeplk5p7OZJvaN66WO8U%2FX%2BNfJvN8o%2F6ZrqREeCY7skab0O2HJgP2kqbjK%2BXth3O%2FmEa8x4pkFcWgToLs9g%3D%3D', urllib.parse.quote('ServiceKey') : '-', urllib.parse.quote('pageNo') : '1', urllib.parse.quote('numOfRows') : '10' })

sample = urllib.request(url + queryParams)
sample.get_method = lambda: 'GET'
response_body = urllib.request.urlopen(sample).read()
print (response_body)
