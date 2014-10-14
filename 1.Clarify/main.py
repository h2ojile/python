#coding=utf8

''' 进行抓取
    的工作场所

    调用相应的 招聘网站实例
    传入 页数,关键词 返回相应页面内容流
    保存为文件
'''

'''获取每一页的内容, 存起来
这地方写错了. 突然发现 总页数必然是用 n 来得到的.
这里应该每对参数生成一个实例,把 页数赋值到上面的. 写错了.
'''

from jobs.Lagou import Lagou





python={'keyword':'python','city':'上海','total':9}

for n in range(1,python['total']+1):
    response=Lagou.getPage(python['keyword'],python['city'],n)
    f = file(python['keyword']+python['city']+str(n)+'.html','wb')
    f.write(response)
    f.close()
