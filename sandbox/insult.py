def isInsult(string,responseModifier = None,responseBool=True):
        identified = False
        identified2 = False
        negation = False
        if responseModifier == 'cranky':
                for word in string:
                        if word == "shut":
                                identified = True
                        if identified == True:
                                if word == 'up':
                                        if responseBool == True:
                                                print "no YOU shut up! leave me alone! I'm not gonna help you! leave, now, or i will be forced to force you!"
                                        return True
                                identified = False
                for word in string:
                        if word == 'idiot':
                                if responseBool == True:
                                        print 'you are an idiot! go away!'
                                return True

def giveInsult(insultWhat,degreeOfOffense,personalityModifier,Imaginativeness):
        return "you big frick!"
