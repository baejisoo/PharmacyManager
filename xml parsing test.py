import xml.etree.ElementTree as etree

def main():
    tree = etree.parse('sample1.xml')
    root = tree.getroot()

    for a in root.findall('row'):



