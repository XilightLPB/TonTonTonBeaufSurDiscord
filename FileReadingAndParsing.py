import os
import time
import random




JokesRepo = []
webhooksurl = []


##Get the jokes from path2file and store them in JokesRepo
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
    
    


##Ised to test that JokesRepo Is initialized correctly
def ReadJokesInOrder(JokesRepo):
    lim = len(JokesRepo)
    for i in range(lim):
        (Joke,Answer) = JokesRepo[i]
        print(Joke)
        print(Answer) 


##Used to test I still knew how to generate a random int lmao
def ReadmeAJoke(JokesRepo):
    i = random.randint(0,(len(JokesRepo)-1))
    print("Jokes number: " + str(i+1))
    (Jokes, Answer) = JokesRepo[i]
    print(Jokes)
    print(Answer)


##Format a joke to hide the answer using the spoiler beacon "||"
def FormatARandomJoke(JokesRepo):
    i = random.randint(0,(len(JokesRepo)-1))
    (res, Answer) = JokesRepo[i]
    res = res + "||" + Answer.strip() + "||"
    #print(res)
    return res


##Extract datas from the Config file
def OpenAndParseConfig(webhooks,username):
    f = open("config.txt")
    step = 1
    for x in f:
        stripped = x.strip()
        if step == 1:
            if stripped != "NEXT":
                webhooks.append(stripped)
                ##print(stripped)
            else:
                step = 2
                ##print("Anyway moving on (that's a spearshot ref)")
        elif step == 2:
            if stripped != "NEXT":
                username = stripped
                print("username is supposed to be:")
                print(stripped)
                return username
            else:
                step = 3
                ##print("Anyway moving on (that's a spearshot ref) step number 2")


    f.close()


##ManualParsingOfJokes("test.txt",JokesRepo)
##ReadJokesInOrder(JokesRepo)
##ReadmeAJoke(JokesRepo)
##FormatARandomJoke(JokesRepo)