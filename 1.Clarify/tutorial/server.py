#coding='utf8'

import web
import json
import re
        
urls = (
    '/', 'index'
)
app = web.application(urls, globals())

pythonJobs =  json.load(open('items.json'))
pythonJobs.sort(key = lambda x:int( re.findall(r'\d+',x['salary'])[0]))

class index:        
    def GET(self):
        render = web.template.render('templates/')
        return render.list(pythonJobs)

if __name__ == "__main__":
    app.run()