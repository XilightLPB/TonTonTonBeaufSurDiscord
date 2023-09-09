import os
import time
import random


##os.remove("test.txt")
##time.sleep(5)
##f = open("test.txt", "w")

JokesRepo = []

def ManualParsingOfJokes(path2file, JokesRepo):
    f = open(path2file)
    i = 0
    for x in f:
       i+=1
       #print(x+ str(i%3)) 
       if (i%3 == 1):
           TheJoke= x
       if (i%3 == 2):
           TheAnswer = x
       if (i%3 == 0):
           ##print("The joke was: " + TheJoke)
           ##print("The Answer was:" + TheAnswer)
           JokesRepo.append((TheJoke, TheAnswer))
    f.close()
    
    



def ReadJokesInOrder(JokesRepo):
    lim = len(JokesRepo)
    for i in range(lim):
        (Joke,Answer) = JokesRepo[i]
        print(Joke)
        print(Answer) 

def ReadmeAJoke(JokesRepo):
    i = random.randint(0,(len(JokesRepo)-1))
    print("Jokes number: " + str(i+1))
    (Jokes, Answer) = JokesRepo[i]
    print(Jokes)
    print(Answer)




ManualParsingOfJokes("test.txt",JokesRepo)
##ReadJokesInOrder(JokesRepo)
ReadmeAJoke(JokesRepo)