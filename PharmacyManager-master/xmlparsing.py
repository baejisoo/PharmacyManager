import xml.etree.ElementTree as ET

# parse xml file
doc = ET.parse('sample.xml')

# get root node
root = doc.getroot()


for pharmacy in root.iter("item"):
    print(pharmacy.findtext("dutyName"))
    print( pharmacy.findtext("dutyAddr"))


