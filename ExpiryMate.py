import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write("Welcome to ExpiryMate, this app is here to help " +
        "you keep track of your food and the dates at which they expire.")

app = webapp2.WSGIApplication([('/', MainPage),
                               ],
                               debug=True)
