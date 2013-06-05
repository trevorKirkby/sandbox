import filesystem as fs
import insult
import speech
#above are specialized programs made for this program's functionality
#below are regular, universally importable packages
import time
import random
from termcolor import colored, cprint
import sys
import tty
import termios

class program(fs.Node):
        def __init__(self,name,permissions = 'x'):
                fs.Node.__init__(self,name,permissions)
        def isExc(self):
                return True


class path(fs.Directory):
        def __init__(self,name,look,permissions = 'rx'):
                fs.Directory.__init__(self,name,look,permissions)
                self.children = { }
                self.passing = None
                self.isProg = True
        def isExc(self):
                return True
        def isDir(self):
                return False
        def isGate(self):
                return True


class objHold(path):
        def __init__(self,name,look,permissions = 'rx'):
                path.__init__(self,name,look,permissions)
                self.children = { }
        def isHold(self):
                return True

class Person(program):
        def __init__(self,name,permissions = 'x'):
                program.__init__(self,name,permissions)
        def move(self,directory):
                self.parent.remove(self)
                directory.add(self)
        def isPerson(self):
                return True
        def say(self,text,mood='norm',enter=True):
                if mood == 'norm':
                        text = colored(text,'yellow',attrs=['bold'])
                if mood == 'angry':
                        text = colored(text,'red',attrs=['bold'])
                if mood == 'happy':
                        text = colored(text,'green',attrs=['bold'])
                if mood == 'scared':
                        text = colored(text,'magenta',attrs=['bold'])
                if mood == 'excited':
                        text = colored(text,'white',attrs=['bold'])
                if mood == 'sad':
                        text = colored(text,'grey',attrs=['bold'])
                fd = sys.stdin.fileno()
                oldSet = termios.tcgetattr(fd)
                tty.setraw(sys.stdin)
                for word in text:
		        randthing = random.random()
		        randVariable = float(randthing/7)
		        sys.stdout.write(word)
		        sys.stdout.flush()
		        time.sleep(randVariable)
                termios.tcsetattr(fd, termios.TCSADRAIN, oldSet)
                if enter == True:
                        print ' '
        def ask(self,question,mood='norm'):
                self.say(question,mood,enter=False)
                variable = raw_input(' : ',)
                return variable
                

'''
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
'''







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
                variable=text.split()
                for word in text:
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

class chest(objHold):
        def __init__(self):
                self.done=False
                objHold.__init__(self,'chest','You are currently squeezed inside of an antique wooden chest. There is not a lot to see.')
                self.children = { }
        def execute(self):
                if self.done==True:
                        print 'I thought i told you never to come back! get out!'
                        raise KeyboardInterrupt
                print "You don't get entry. Sorry. Actually, sorry about this revision, i'm not sorry. Anyway, I don't have any good reason to let you get what's inside this chest."
                time.sleep(5)
                print 'well? leave!'
                time.sleep(5)
                thing = raw_input("why are you still here?")
                if speech.isIn(thing,'let me in'):
                        print 'no. give me a good reason to.'
                elif speech.isIn(thing,"I'll go"):
                        print 'good.'
                        raise KeyboardInterrupt
                elif speech.isIn(thing,'help'):
                        print 'nope, no help'
                elif speech.isIn(thing,'idiot'):
                        print 'thats it!'
                        return False
                else:
                        print '"', thing, '"???!', 'Your not giving me any reason to actually care about letting you in! You cant, and even if you could you individually would probably fail to work out how! bye!'
                time.sleep(5)
                thing = raw_input("clearly your not leaving, so I'll make you a deal. I'll let you in provided you never come back. Deal? ")
                if thing == 'yes':
                        print 'good'
                        self.done = True
                        return True
                elif thing == 'deal':
                        print 'good'
                        self.done = True
                        return True
                elif thing == 'okay':
                        print 'good'
                        self.done = True
                        return True
                else:
                        print 'if you wont say yes to this than get lost!'
                        return False

class bob(Person):
        def __init__(self):
                Person.__init__(self,'bob')
        def execute(self):
                #say(text,mood=norm) ask(text,mood=norm) and move(node)
                self.say('hello, how are you. i am a program, yet i can move through directories, and talk, simulating a person.')
                self.say('I can also talk in various voices','angry')
                variableA = self.ask('i can also ask questions, easily. would you like me to move to directory ..? y/N')
                if variableA == 'y':
                        if self.parent.parent != None:
                                self.say('okay... hold on a sec.')
                                self.move((self.parent).parent)
                        else:
                                self.say('sorry, but i cant do that, because im in root directory.')
                else:
                        self.say('okay then. bye for now.')


#IC challenge

class ExecutePath(path):
        def __init__(self):
                path.__init__(self,'door','Blank, steel walled room. A sign reads: Well done! You have just mastered one basic action permitted in this system.')
        def execute(self):
                speech.say("Who are you! Whoever you are, your going to regret ever looking to get past this door! You are NOT getting in.",mood='angry')
                time.sleep(0.5)
                print '--Acess Granted--'
                time.sleep(0.2)
                speech.say("What?! No! Stupid program! You're not allowed in here! Go away! Wait, no! Come back! Face me!!!!",mood='angry')
                time.sleep(0.2)
                print 'Shutting down doorway program. Have a nice day.'
                time.sleep(0.2)
                speech.say("Stop!",mood='angry')
                return True

#SEE challenge
