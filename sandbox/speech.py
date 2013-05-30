import insult as ins

def aprint():
        #like autoprint but less specified, takes more input on colors, timing, etc.
        pass
def ask(question):
        #asks a question and returns answer easily
        variable = raw_input(question)
        return variable
def respond(qname,say,reply,returnBool=True,reverseBool=False):
        if reverseBool == False:
                if qname == say:
                        if returnBool == True:
                                return reply
                        elif returnBool == False:
                                print reply
                        else:
                                print 'Error: Speech: Reply Function: Specify a True or False return boolean'
                                raise KeyboardInterrupt
        elif reverseBool == True:
                if qname != say:
                        if returnBool == True:
                                return reply
                        elif returnBool == False:
                                print reply
                        else:
                                print 'Error: Speech: Reply Function: Specify a True or False return boolean'
                                raise KeyboardInterrupt
        else:
                print 'Error: Speech: Reply Function: Specify a True or False reverse boolean'
                raise KeyboardInterrupt
#so an example would be:
#questionName = ask('how are you?')
#reply(questionName,'not very well','cheer up!')

def isIn(qname,say):
        said = qname.split()
        identify = say.split()
        index = range(len(said))
        index2 = range(len(identify))
        found = False
        for word in said:
                for part in identify:
                        if part == word and index == index2:
                                index2 = index2 + 1
                                index = index + 1
        if index2 == len(identify):
                found = True
        return found

def reply(qname,say,reply,returnBool=True,reverseBool=False,directedAt='me'):
        #after dinner incorporate negatoried and directed at, for example if told to find if the word idiot is directed at self, will not trigger in these times because of this: your not an idiot,  or he is an idiot, also paralell synonyms, such as your and idiot and your stupid, and basic speech formatting, such as your an idiot and you are an idiot
        found = isIn(qname,say)
        if reverseBool == False:
                if found == True:
                        if returnBool == True:
                                return reply
                        elif returnBool == False:
                                print reply
                        else:
                                print 'Error: Speech: Reply Function: Specify a True or False return boolean'
                                raise KeyboardInterrupt
        elif reverseBool == True:
                if found == False:
                        if returnBool == True:
                                return reply
                        elif returnBool == False:
                                print reply
                        else:
                                print 'Error: Speech: Reply Function: Specify a True or False return boolean'
                                raise KeyboardInterrupt
        else:
                print 'Error: Speech: Reply Function: Specify a True or False reverse boolean'
                raise KeyboardInterrupt

def greet(personality,returnBool=False):
        if returnBool == True:
                return 'hello!'
        elif returnBool == False:
                print 'hello!'
        else:
                print 'Error: Speech: Greet Function: Specify a True or False return boolean'
def talk(program):
        #eventually, able to use self.variables to actually cobble togethor speech, and manage all other methods. You could tell it to say insult, you could tell it to ask questions with some auto responses for non reply instances and insults and other broad categories, you could just tell it to say something according to how it feels. Basically, with good self.variables and maybe a few individual phrasing modifiers, you could make an on-the-fly speech AI. This would even tell if its a program that needs to be persuaded, and it will factor in basic shared personality traits in classes.
        pass
