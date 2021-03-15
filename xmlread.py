import xml.etree.ElementTree as et

tree = et.ElementTree(file="menu.xml")

root = tree.getroot()

print ("根目錄 :",root.tag)
print ("-"*30)

for child in root :
    print ("tagV1 :", child.tag, "attribute :", child.attrib)
    for child2 in child :
        print ("\ttagV2 :", child2.tag, "attribute :", child2.attrib, "value :", child2.text)

print ("-"*30)
print ("根目錄項目數 :",len(root))
print ("-"*30)
print ("第一個選單項目數 :",len(root[0]))



