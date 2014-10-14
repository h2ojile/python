#coding='utf8'

import web
import json
        
urls = (
    '/', 'index'
)
app = web.application(urls, globals())

pythonJobs =  json.load(open('items.json'))

class index:        
    def GET(self):
        render = web.template.render('templates/')
        return render.list(pythonJobs)

if __name__ == "__main__":
    app.run()