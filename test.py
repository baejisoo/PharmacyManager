import urllib.request

class GetData:

    key= '5pNTeplk5p7OZJvaN66WO8U%2FX%2BNfJvN8o%2F6ZrqREeCY7skab0O2HJgP2kqbjK%2BXth3O%2FmEa8x4pkFcWgToLs9g%3D%3D'
    url = "http://openapi2.e-gen.or.kr/openapi/service/rest/ErmctInsttInfoInqireService/getParmacyBassInfoInqire"

    def main(self):
        data = urllib.request.urlopen(self.url).read()
        #print(data)
        f = open("sample.xml", "wb")
        f.write(data)
        f.close()

getData=GetData()
getData.main()