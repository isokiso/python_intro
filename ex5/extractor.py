import sys
import re
import json



#open a given file
with open(sys.argv[1], "r", encoding="utf-8") as f:
    str1 = f.read()

#get author name
dic1 = {}
pattern = "\<h1 class=\"author\">(.*)</h1>"
m = re.search(pattern, str1)
dic1.update(author=m.group(1))

#get text
pattern = "<p pno=[0-9]+>(.*?)</p>"
m = re.findall(pattern, str1)
m = [s.replace('<br>', '\n') for s in m]
l = ''.join(m)
dic1.update(text=l)

#dump dic1
with open('out.json', "w", encoding="utf-8") as f2:
    json.dump(dic1, f2)
