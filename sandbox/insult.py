def isInsult(string,responseModifier = None):
        identified = False
        identified2 = False
        negation = False
        if responseModifier == 'cranky':
                for word in string:
                        if word == "shut":
                                identified = True
                        if identified == True:
                                if word == 'up':
                                        print "no YOU shut up! leave me alone! I'm not gonna help you! leave, now, or i will be forced to force you!"
                                        return True
                                identified = False
                for word in string:
                        if word == 'idiot':
                                print 'you are an idiot! go away!'
                                return True
