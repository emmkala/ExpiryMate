from Item import Item

class User():
    basket = []

    def __init__(userName):
        this.userName = userName

    #From loaded dictionary to object    
    def fileToObject(foodDict):
        for item in foodDict:
            basket.append(newFoodItem(item,foodDict[item]['days']))

    def addItem(name,days):
        basket.append(newFooditem(name,days))
            
    #Creates new object via food class 
    def newFoodItem(name,daysLeft):
        newItem = Item(name,daysLeft)
        return newItem
                          
    #Delet by loop return none
    def deleteItem(name):
       for item in basket:
            if item.getName() == name:
                basket.remove(item)

    def getTime(name):
        for item in basket:
            if item.getName() == name:
                return item.getExpire()
        return None

    
                      

    #Returns 2D list in form [[name,days],etc.] for ease of write to file
    def basketToList():
        saveBasket = []

        for item in this.basket:
            saveItem = []
            saveItem[0] = item.getName()
            saveItem[1] = item.getExpire()
            saveBasket.append(saveItem)

        return saveBasket
        
