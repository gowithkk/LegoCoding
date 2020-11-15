import xml.etree.ElementTree as ET

tree = ET.parse('xmlexample.xml')
print(tree)

# get root element
root = tree.getroot()
print(root)

# get root element's name
print(root.tag)

# get root element's attributes
print(root.attrib)

# get sub-elements
for attribute in root:
    print(attribute.tag, attribute.attrib)

# return second value in first sub-element
print(root[0][1].text)

# get values with name 'neighbor' from all the elements
print(root.iter('neighbor'))
for neighbor in root.iter('neighbor'):
    print(neighbor.attrib)

# get value from all the sub-elements (first level)
for body in root.findall('body'):
    rank = body.find('from').text
    name = body.get('text')
    print(name, rank)

# modify XML files
for rank in root.iter('rank'):
    new_rank = int(rank.text) + 1
    # change value
    rank.text = str(new_rank)
    # set attribute update to yes
    rank.set('update', 'yes')

# write changes into a new file output.xml
tree.write('output.xml')