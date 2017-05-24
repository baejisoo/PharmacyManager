import urllib.parse
import urllib.request

url = 'http://apis.data.go.kr/B552657/ErmctInsttInfoInqireService/getParmacyFullDown'
queryParams = '?' + urllib.parse.urlencode({ urllib.parse.quote('ServiceKey') : '1td22cJml3Qk4BuSNgwhWXUk2xtS8zrLx0n0OfwQHdcn5HvvOvAv9UOJ6qSztOTbtrI5ODfdxzXhgvC5NJWxvQ%3D%3D', urllib.parse.quote('ServiceKey') : '1td22cJml3Qk4BuSNgwhWXUk2xtS8zrLx0n0OfwQHdcn5HvvOvAv9UOJ6qSztOTbtrI5ODfdxzXhgvC5NJWxvQ%3D%3D', urllib.parse.quote('pageNo') : '1', urllib.parse.quote('numOfRows') : '10' })

sample = urllib.request(url + queryParams)
sample.get_method = lambda: 'GET'
response_body = urllib.request.urlopen(sample).read()
print (response_body)


