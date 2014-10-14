#coding=utf8

''' 从存下来的html中 正则 抓出 内容.文件不多, os.listdir估计就够了.
'''

import os
import re
import json

path = 'tmp/files'

urls = []
for filename in os.listdir(path):
    print filename
    f = file(path+'/'+filename)
    fileContent = f.read()
    f.close()
    match = re.findall(r'http://.*?source=search', fileContent)
    urls+=match

    
urls=list(set(urls))

f = file('allUrl.json','wb')
json.dump(urls, f, indent=4, sort_keys=True, separators=(',',':'))
f.close()
