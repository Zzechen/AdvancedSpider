import requests
import json

baidu = 'http://www.baidu.com'
mockGet = 'https://demo5407759.mockable.io/login'
mockPost = 'https://demo5407759.mockable.io/post'
orgPost = 'http://httpbin.org/post'

# normal get method
r = requests.get(mockGet)
print r.status_code
print r.text
print r.cookies
print r.json()

# get json
# print r.json()

# get with params,headers
valus ={'key1':'value1','key2':'value2'}
headers = {'content-type':'application/json'}
r = requests.get(baidu,params=valus,headers = headers)
# http://www.baidu.com/?key2=value2&key1=value1
print r.url


# normal post
# data is the formData
r = requests.post(mockPost,data=valus)
print r.text

# json
r = requests.post(mockPost,data= json.dumps(valus))
print r.text

# post a file
file = {'file':open('a.txt','rb')}
r = requests.post(baidu,files = file)
print r.text

# set timeout
requests.get(baidu,timeout= 10)

# verify ssl ,12306 verify failed....
# r = requests.get('https://kyfw.12306.cn/otn/', verify=True)
# print r.text

# api:http://docs.python-requests.org/en/master/api/

