
print("Hi there. How are you feeling?")

feelingStuff = {'good': ['good', 'happy', 'estatic', 'amazing', 'awesome', 'hopeful', 'optimistic', 'rosy', 'sanguine', 'animated', 'chirpy', 'jaunty', 'lilting', 'lively', 'perky', 'sprightful', 'sprightly', 'vivacious', 'carefree', 'careless', 'cavalier', 'devil-may-care', 'easygoing', 'happy-go-lucky', 'insouciant', 'lighthearted', 'unconcerned boon', 'gleeful', 'jocund', 'jolly', 'jovial', 'merry', 'mirthful', 'blissful', 'delighted', 'glad', 'gratified', 'happy', 'joyful', 'joyous', 'pleased', 'satisfied', 'tickled', 'beaming', 'grinning', 'laughing', 'smiling', 'great', 'perfect', 'grateful'], 'bad': ['sorrowful', 'ugly', 'awful','unhappy', 'miserable', 'mournful', 'upset', 'depressed', 'heartbroken', 'somber', 'sombre', 'blue', 'dejected', 'demoralised', 'demoralized', 'desolate', 'despondent', 'disconsolate', 'disheartened', 'dispirited', 'distressed', 'down', 'forlorn', 'glum', 'hurt', 'melancholy', 'pessimistic', 'sullen', 'troubled', 'wistful', 'bereaved', 'bitter', 'cheerless', 'doleful', 'downcast', 'down in dumps', 'down in mouth', 'gloomy', 'grief-stricken', 'grieved', 'hapless', 'heartsick', 'heavyhearted', 'in doldrums', 'in grief', 'in the dumps', 'joyless', 'low', 'low-spirited', 'lugubrious', 'moody', 'morbid', 'sad', 'bad', 'horrible', 'hopeless', 'useless', 'crumpled'], 'neutral':['normal', 'fine', 'decent', ' ']}

def goodStuff():
    queryGood = input()
    if queryGood == "yes":
        queryGood = input("Alright. Tell me about it.\n")
def badStuff():
    print(" ")
def neuStuff():
    print(" ")

def helpCode():
    query = input()
    for i in range(0, len(feelingStuff['good'])):
        if query == feelingStuff['good'][i]:
            print("That's really good. Want to talk about why?")
            return goodStuff()
        elif i == len(feelingStuff['good']) - 1:
            print("I didn't quite get that. Please type a different adjective")
            helpCode()
        else:
            for j in range(0, len(feelingStuff['bad'])):
                if query == feelingStuff['bad'][j]:
                    print("That's not good. Want to talk about it?")
                    return badStuff()
                elif j == len(feelingStuff['bad']) - 1:
                    pass
                else:
                    for k in range(0, len(feelingStuff['neutral'])):
                        if query == feelingStuff['neutral'][k]:
                            print("Why?")
                            return neuStuff()
                        elif k == len(feelingStuff['neutral']) - 1:
                            pass
                        else:
                            pass

if __name__ == "__main__" :
    helpCode()