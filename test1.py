import urllib.request


import http.client

def urlencode(string):
    print("URLEncoding:",urllib.quote(string))

url = 'http://apis.data.go.kr/B552657/ErmctInsttInfoInqireService/getParmacyFullDown'
queryParams = '?' + urllib.parse.urlencode({ urllib.parse.quote_plus('ServiceKey') : 'Lg8o2pi2x5AWT0RIJ5XkNewd%2BtSXe63rr5za624JyZiO1TiQpbdNmDhonlj1zFMucI35WMs0idy66DCXSgi%2FvA%3D%3D', urllib.parse.quote_plus('ServiceKey') : '-', urllib.parse.quote_plus('pageNo') : '1', urllib.parse.quote_plus('numOfRows') : '10' })

request = urllib.request.Request(url + queryParams)
request.get_method = lambda: 'GET'
response_body = urllib.request.urlopen(request).read()
print(response_body)



