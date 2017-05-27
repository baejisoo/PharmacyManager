import urllib.request

class GetData:

    url = 'http://apis.data.go.kr/B552657/ErmctInsttInfoInqireService/getParmacyBassInfoInqire?ServiceKey=1td22cJml3Qk4BuSNgwhWXUk2xtS8zrLx0n0OfwQHdcn5HvvOvAv9UOJ6qSztOTbtrI5ODfdxzXhgvC5NJWxvQ%3D%3D'

    def main(self):
        data = urllib.request.urlopen(self.url).read()
        #print(data)
        f = open("sample.xml", "wb")
        f.write(data)
        f.close()

getData=GetData()
getData.main()