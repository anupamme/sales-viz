import cgi
import webapp2

class Shopify(webapp2.RequestHandler):

    def get(self):
        html = open('shopify2.html', 'r').read()
        self.response.headers['Content-Type'] = 'text/html'
    	self.response.write(html)
        
class CSVUpload(webapp2.RequestHandler):

    def get(self):
        html = open('data5.html', 'r').read()
        self.response.headers['Content-Type'] = 'text/html'
    	self.response.write(html)
        
class MainPage(webapp2.RequestHandler):

    def get(self):
        html = open('draw4.html', 'r').read()
        self.response.headers['Content-Type'] = 'text/html'
    	self.response.write(html)

application = webapp2.WSGIApplication([
    ('/', MainPage), ('/shopify', Shopify), ('/csvupload', CSVUpload)], debug=True)