import speech as sp

def isInsult(text,responseModifier = 'random',responseBool=True):
        identified = False
        identified2 = False
        negation = False
        string = text.split()
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
        elif responseModifier == 'other':
                if sp.isIn(string,'your dumb'):
                        if responseBool == True:
                                print 'no you are dumb'
                        return True
        else:
                print 'Error: Insults Module: isInsult Function: Specify a response modifier'

def giveInsult(insultWhat,degreeOfOffense,personalityModifier,Imaginativeness):
        return "you big frick!"
        #insultsLists-
