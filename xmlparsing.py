from xml.etree import ElementTree

root = ElementTree.fromstring("item")
total = root.find("dutyName").find("dutyAddr")
print (total.text)

