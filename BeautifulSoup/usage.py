from bs4 import BeautifulSoup
import requests

baidu = 'http://www.baidu.com'
res = requests.get(baidu)
html = res.text
# from text
# soup = BeautifulSoup(html)
# from stream
soup = BeautifulSoup(open('baidu.html','rb'),'html5lib')

# format html and print
print soup.prettify()

# in soup,there is a Tree,including tag,navigableString,BeautifulSoup,Comment

# get tag ,like title,a,p,head
print soup.title
# get the name/attrs for a tag
print soup.a.name
print soup.a.attrs

# NavigableString:content for a tag
print type(soup.title.string)

# .content:get all child node of a tag--> a list
print soup.head.contents[1]

# .children:get a iterator for child of a tag --> use for
print soup.head.children
for child in soup.head.children:
    print child

# .descendants:get all node for a tag
for child in soup.descendants:
    print child

# find
# some method start with 'find_',

# select ,like css
# 1. by name of tag,
soup.select('a')
# 2. by class
soup.select('.className')
# 3.by id
soup.select('#id')
# and some combination

# more info :https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html
