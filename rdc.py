import web
from cam import *

urls = (
	'/rdc/', 'index'
)

class index:
	def GET(self):
		res = str(checkChild()) + "\n"
		res += str(getTemp()) + "\n"
		res += str(getPixels()) + "\n"
		return res

if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()
