import pymongo

mClient = None
db = None
guilds = None

perPage = 5

def init():
    global mClient
    global guilds
    global db

    mClient = pymongo.MongoClient("mongodb://localhost:27017/")
    
    db = mClient["bedibot"]

    guilds = db["guilds"]

def insertQuote(guildId: int, quote: str, quotedPerson: str):
    doc = {
        'quote': quote,
        'name': quotedPerson.upper()
    }
    coll = db["a" + str(guildId) + ".quotes"]
    try:
        coll.insert_one(doc)
        return True
    except:
        return False

def deleteQuote(guildId, quote, quotedPerson):
    coll = db["a"+guildId + ".quotes"]
    coll.delete_one({"quote": quote, "name": quotedPerson})
    
def findQuotes(guildId, quotedPerson, page):

   skip = perPage * (page - 1)
   quotes = []
   coll = db["a"+guildId+".quotes"]
   filter = {
       "name": {"$regex" : "^.*"+quotedPerson+".*$"}
   }
   pipeline = [
       {"$match": filter},
       {"$limit": perPage},
       {"$skip": skip}
   ]
   try:
       return list(coll.aggregate(pipeline))
   except:
       return None





#init()
#insertQuote("758817188710449183","this is a quote4","Aadi")
#nsertQuote("758817188710449183","this is a quote1","Aadi")
#insertQuote("758817188710449183","this is a quote2","Aadi")
#insertQuote("758817188710449183","this is a quote3","Aadi")
#deleteQuote("758817188710449183","this is a quote3","Aadi")

#quotes = findQuotes("758817188710449183","Aadi",4)
#for quote in quotes:
 #   print(quote)