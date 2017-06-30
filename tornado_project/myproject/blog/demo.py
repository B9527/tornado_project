import tornado.ioloop
import tornado.web


class MyHandle(tornado.web.RequestHandler):
    def get(self):
        self.write('hello world!')


class FirstHandle(tornado.web.RequestHandler):
    def get(self):
        self.write('first web!')


application = tornado.web.Application([
    (r"/hello/", MyHandle),
    (r"/first/", FirstHandle)
])

if __name__ == "__main__":
    application.listen(8000)
    tornado.ioloop.IOLoop.instance().start()
