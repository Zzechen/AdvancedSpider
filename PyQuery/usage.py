# https://pythonhosted.org/pyquery/
from pyquery import PyQuery as pq

doc = pq(filename='hello.html')
print doc.html()
li = doc('li')
# always return PyQuery
print type(doc)
print type(li)
print li.text

for item in li.items():
    print item