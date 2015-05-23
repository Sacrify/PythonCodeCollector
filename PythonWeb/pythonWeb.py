import web
import pdb

urls = (
  '/pythonGet', 'index',
  '/pythonPost', 'post',
)

class index:
    def GET(self):
        print "Hello, world!"

class post:
    def POST(self):
    	print web.data()
    	web.ctx.headers = [('Content-Type', 'text/plain;charset=UTF-8')]
    	web.ctx.headers.append(('Access-Control-Allow-Origin', '*'))
        pdb.set_trace()
        return "GuangMing is handsome! YuanWu is handsome, too!"


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
