import requests
import json
import time
from datetime import datetime
from FileReadingAndParsing import *




##Just keeping as an example how to do a post
#r = requests.post(webhook_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})



##Just having fun with infinite loops and posting
def loopHook():
    i = 0
    while True:
      i=i +1
      num = str(i)
      print(num)
      message = "Bon bah on test hein itération numéro " + num
      ##print (message)

      data = {
    
      "username": "Mon Bot à moi",
      "avatar_url": "https://i.imgur.com/p5xqgq3.png",
      "content": message,
      "embeds": [
        {
          "footer": {
          "text": "Ceci est un footer.",
          "icon_url": "https://vignette.wikia.nocookie.net/spiderriders/images/d/dd/Discord.png/revision/latest?cb=20171218232913"},
          "thumbnail": {
          "url": "http://ec.europa.eu/eurostat/cache/infographs/youthday2016/img/embed.png"},
          "title": "Ceci est un titre !",
          "description": "Ceci est une description.\n\n[Ceci est un lien cliquable.](url.com)\n\n:web: Cette icone est un emoji.",
          "color": 16777215
  }
 ]
}
      

      r2 = requests.post(webhook_url2, data=json.dumps(data), headers={'Content-Type': 'application/json'})
      print("loop numéro " + num)
      time.sleep(10)



##Post a default message
def singletest():
   message = "Comment fait-on descendre un gothique d'un arbre?\n||On coupe la corde||\n@lesilexquifaidufeeee "
   data = {
      
      "username": "Mon Bot à moi",
      "avatar_url": "https://i.imgur.com/p5xqgq3.png",
      "content": message,
      
}
   r2 = requests.post(webhook_url2, data=json.dumps(data), headers={'Content-Type': 'application/json'})
   print("test unitaire effectué")
   return 0



##Post the message, and got a default message explicitly stating that you forgot that data
def PostAMessage(message =None):
   if message == None:
      message = "Vu que jsuis stupide j'ai oublié de dire quel message je voulais envoyer :skull:"
   data = {
      
      "username": "Mon Bot à moi",
      "avatar_url": "https://i.imgur.com/p5xqgq3.png",
      "content": message,
      
}
   r2 = requests.post(webhook_url2, data=json.dumps(data), headers={'Content-Type': 'application/json'})
   print("test unitaire effectué")
   return 0


##Just Checking the code did run without any issue when it comes to import or something and printing the hour to let us know (can be transformed into a log function quite easily)
print("well the code did run")
time.sleep(0)
print("d'ailleurs il est actuellement:")
hour = datetime.now()
print(hour)
onlyhourandmin = hour.strftime("%H:%M")
onlyhour= hour.strftime("%H")
print(onlyhourandmin)
print(onlyhour)
webhooks = []



##Import configs informations such as differents webhooks
OpenAndParseConfig(webhooks)
webhook_url2 = webhooks[0]

##singletest() function used to print a simple message with no configuration, good to verify that your listener is active


##Getting the jokes stored in "Jokes.txt" and importing them in JokesRepo that will contain each jokes in a different element
JokesRepo = []
ManualParsingOfJokes("Jokes.txt",JokesRepo)
##ReadJokesInOrder(JokesRepo)
ReadmeAJoke(JokesRepo)
message = FormatARandomJoke(JokesRepo)
PostAMessage(message)


