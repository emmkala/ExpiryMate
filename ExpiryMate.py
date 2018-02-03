import webapp2
foodLis = ["Apple","Blueberry","Orange"]
import urllib.request
import json
import csv



class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write('''
        <head>
        <style>
        body{
            background-color: rgb(0,255,0);
        }
        </style>
        </head>
        <h1>Welcome  to ExpiryMate!</h1>
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

    def createCSVHeader(fileName):
        with open(fileName, "w",newline="") as csvFile:
            csvFileWriter = csv.writer(csvFile)
            csvFileWriter.writerow(['Item','Room Temperature','Refrigerator','Freezer at 0°F'])

    #Appends a row of data about a post to the end of the csv file containing status/post information
    def appendToCSV(col_one,col_two,col_three,col_four):

        with open('FoodList.csv', "a",newline="",encoding='utf-8' ) as csvFile:
            csvFileWriter = csv.writer(csvFile)
            csvFileWriter.writerow([col_one,col_two,col_three,col_four])
        csvFile.close()

    def fillFoodList():
        createCSVHeader('FoodList.csv')
        data = []
        response = urllib.request.urlopen("https://food.unl.edu/food-storage-chart-cupboardpantry-refrigerator-and-freezer")
        line = response.readline()
        foodItem = []
        count = 1

        while len(line) != 0:
            textLine = line.decode('utf-8')
            #Check to see if the element is a food item
            if textLine[0:4] == "<td>" and textLine[4:11] != "<span c":
                print("")
                cleanWord = []
                #Taking the tags away from the elements
                for letter in textLine[4::]:
                    if letter != '<':
                        cleanWord.append(letter)
                    else:
                        break
                    data = ''.join(cleanWord)
                    if data == '&nbsp;':
                        data = ""
                foodItem.append(data)
                if len(foodItem) == 4:
                    appendToCSV(foodItem[0],foodItem[1],foodItem[2],foodItem[3])
                    foodItem = []
                count = count + 1
            line = response.readline()

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
