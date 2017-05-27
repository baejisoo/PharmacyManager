import xml.etree.ElementTree as ET

# parse xml file
doc = ET.parse('약국+위치정보+조회.xml')

# get root node
root = doc.getroot()

for child in root.iter():
    print(child.tag)

for country in root.iter('dutyName'):
    print(country.tag)

