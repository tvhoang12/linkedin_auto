from lxml import etree

tree = etree.parse("xpath_config.xml")
root = tree.getroot()

xpath = {elem.tag : elem.text for elem in root}

globals().update(xpath)