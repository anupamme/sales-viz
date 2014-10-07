import cgi
import webapp2
from unidecode import unidecode

class MainPage(webapp2.RequestHandler):

    def get(self):
        html = open('draw3.html', 'r').read()
        self.response.headers['Content-Type'] = 'text/html'
    	self.response.write(html)
        
application = webapp2.WSGIApplication([
    ('/', MainPage)], debug=True)