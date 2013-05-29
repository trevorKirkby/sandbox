import filesystem as fs
import insult
import time

class program(fs.Node):
        def __init__(self,name):
                fs.Node.__init__(self,name)
        def isDir(self):
                return False
        def isExc(self):
                return True


class path(fs.Directory):
        def __init__(self,name,look):
                fs.Directory.__init__(self,name,look)
                self.children = { }
                self.passing = None
                self.isProg = True
        def isDir(self):
                return False
        def isExc(self):
                return True
        #later dispense with all these isExc stuff and just give every class a self.type = 'file' or 'program' or 'directory'. That simple.

class doorway(path):
        #locks is a string of 'PassCode','KeyObj','Qst','Persuade',or 'none'. default = 'none', is a list so can be more barriers though
        #sent config variable may be 1,2,3,4,5,or 6. Random additions puts this at either 1,2,3,4,5,6,7,8,or 9. factoring in aditions, this should still form a spectrum, with three distinct areas.
        def __init__(self,name,look=None,basePersonality='indifferent',formMod=4,locks=['none'],extraSpeakBool=False):
                #this way if you don't call anything, and fail to enter any text feilds, the format will use the conversation module to fill in a very, very drab, basic door. The more unique attention it gets, the better it is, even if it's just a personality modifier and one unique phrasing. But a fully defined door, which isn't very hard to make, can be very good
                path.__init__(self,name,look)
                for item in locks:
                        if item == 'PassCode':
                                self.request = None
                                self.code = None
                                #initialize proper structuring to support this
                if extraSpeakBool == True:
                        #used when conversations with a door actually have plot significance
                        self.DefTriggerProg = True
                self.person = basePersonality
                #the below are enterable in specific strings that are likely to be said by the AI
                self.greet = None
                self.entry = None
                self.reject = None
                self.insult = None
                self.neutralSpeak = None
                self.compliment = None
                self.angry = None
                self.pleased = None
                self.indifferent = None
                self.ifTriggerDef = False
                self.config = formMod + random.choice(range(4))
                if self.config > 5:
                        print 'on the upper side of config spectrum'
                if self.config == 1:
                        print 'lower extreme of config spectrum'










#below are specific programs

class rootAI(program):
        def __init__(self):
                program.__init__(self,'rootAI')
                #here is also a good place to make remembered variables, or pickled variables, stored in self.variable
                self.temper = 1
        def execute(self):
                variable = raw_input("what d'ya want?!: ")
                if insult.isInsult(variable,'cranky') == True:
                        self.temper = self.temper + 5
                if variable == 'the answer':
                        print 'fine then! solve. that is all im telling you.'
                if variable == 'hello':
                        print 'hello! goodbye! howabout leaving now.'
                if variable == 'what do you want?':
                        print 'YOU TO GO AWAY!'
                        self.temper = self.temper + 3
                if variable == 'is it christmas?':
                        print 'NO!!!!!!'
                        self.temper = self.temper + 1
                if self.temper > 8:
                        print "that's it! i'm forcing you to leave! then shutting down!"
                        return False
                #if/for boundary
                for word in variable:
                        if word == 'information':
                                print "i do have some information you might want but you gotta ask for the correct information in the first place. I won't help you unless you get it right."
                thing = raw_input("k bye then! leave and don't come back! ")
                return None

class gateway(path):
        def __init__(self):
                path.__init__(self,'gateway','there is actually nothing in here! so far there is no objective in the challenge.')
        def execute(self):
                print 'hello. here is a standardized question in which you will give the correct solution to earn passage: '
                time.sleep(1)
                variable2 = raw_input("what is the correct answer? : ")
                if variable2 == 'solve':
                        return True
                else:
                        print 'WRONG!!!'
                        return None
