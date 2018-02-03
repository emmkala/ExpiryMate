import webapp2
foodLis = ["Apple","Blueberry","Orange"]
class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write('''
        <header>
        <h1>Welcome  to ExpiryMate!</h1>
        </header>
        ''')
        self.response.write("<p>This app is here to help " +
        "you keep track of your food and the dates at which they expire." +
        " You are able to add new foods and remove current ones as they "+
        "are eaten.</p>")
        self.response.write('''
            <form action="/add" method=post>
            <input type=text name=food>
            <input type=submit value="Add to Expiry List">
            </form>
        ''')
class ExpiryList(webapp2.RequestHandler):
    def post(self):
        self.response.write(
            '<h2>Your latest food addition is:</h2> %s' % self.request.get('food')
        )
        foodLis.append(self.request.get('food'))
        self.response.write(foodLis)
app = webapp2.WSGIApplication([('/', MainPage),
                               ('/add', ExpiryList),
                               ],
                               debug=True)
