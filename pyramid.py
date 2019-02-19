from xml.etree import ElementTree as ET

xml = '<cube color="blue"><cube color="red"><cube color="green"><cube color="blue"><cube color="red">' \
      '<cube color="red"></cube></cube></cube></cube></cube><cube color="blue"><cube color="green"></cube>' \
      '</cube><cube color="blue"></cube></cube>' #input()
values ={'red': 0,
         'green': 0,
         'blue': 0
        }

root = ET.fromstring(xml)
depth = 0
while True:
    level = '.' + '/*' * depth
    getter = root.findall(level)
    if len(getter) == 0:
        break
    for el in getter:
        values[el.get('color')] += 1 + depth
        print(el.get('color'), depth)
    depth += 1


print(values['red'], values['green'], values['blue'])