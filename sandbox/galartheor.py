import executables as ex
import time
from termcolor import cprint, colored
import sys
import insult

class gProg(ex.program):
        def __init__(self,name):
                ex.program.__init__(self,name)
                #the below variables were be slowly integrated into working programs. this program group meant to represent a large computerized entity will not be added into the program, which can be changed as it is played, until it is completely complete and fully integrated with helpful methods to easily build this AI
                self.activated = False
                self.anger = 0
                self.pleased = 0
                self.thoughtful = 0
                self.excited = 0
                self.worried = 0
                self.humor = 0
                self.paranoia = 0
                self.emotionList = [self.anger,self.pleased,self.thoughtful,self.excited,self.worried,self.humor,self.paranoia]
                self.plotLocation = 1
                self.functionalityLevel = [False,False,False,False,False,False,False,False]
                self.intellect = 450
                #out of 1,000
                self.memory = 700
                self.persons = ['default','megalomaniac','uberDrama','stupid/borderlineStoned','genius','hyperAngry','spazzy','passiveAgressive','theta']
                self.personalityBubble = self.persons[0]
                self.STIPM = None
                #remember- add a taunt instances program to give pre-typed taunts according to performance on the fly and according to mood, and an autotaunt piped through autoprint that gives a taunt depending on mood(some taunts are just your dumb some are more amusing)
        def wordByWordPrint(self,text1,waitTime):
                text = text1.split()
                for word in text:
		        randthing = random.choice(range(waitTime)) + 1
		        randVariable = randthing/5
		        print word,
		        sys.stdout.flush()
		        time.sleep(randVariable)
        def gprint(self,text,adj='standard'):
                if adj == 'standard':
                        return colored(text, 'red', 'on_white', attrs=['dark','underline'])
                if adj == 'pleased':
                        return colored(text, 'blue', 'on_cyan', attrs=['bold'])
                if adj == 'excited':
                        return colored(text, 'yellow', 'on_blue', attrs=['dark','bold','underline'])
                if adj == 'angry':
                        return colored(text, 'red', attrs=['bold','underline'])
                if adj == 'quiet':
                        return colored(text, 'blue', 'on_white', attrs=['dark','underline'])
                if adj == 'confused':
                        return colored(text, 'cyan', 'on_white', attrs=['dark'])
                if adj == 'annoyed':
                        return colored(text, 'yellow', 'on_yellow', attrs=['bold','dark','underline'])
                if adj == 'sarcastic':
                        return colored(text, 'white', 'on_yellow', attrs=['bold','underline'])
                if adj == 'dramatic':
                        return colored(text, 'green', 'on_red', attrs=['bold','underline'])
                if adj == 'amused':
                        return colored(text, 'green', 'on_grey', attrs=['dark','bold','underline'])
                if adj == 'warning':
                        return colored(text, 'red', 'on_yellow', attrs=['dark','bold'])
                if adj == 'insane':
                        return colored(text, 'magenta', 'on_yellow', attrs=['bold','underline'])
        def dprint(self,text):
                if anger > 40:
                        marker = True
                        for number in self.emotionList:
                                if self.anger < number:
                                        marker = False
                        if marker == True:
                                gprint(self,text,'angry')
                else:
                        gprint(self,text)
        def autoprint(self,text,timewait=5):
                self.wordByWordPrint(self.dprint(),timewait)
        def remember(self,variable):
                self.STIPM = variable
                #short term inter program memory

class samplePrinter(gProg):
        def __init__(self):
                gProg.__init__(self,'samplePrinter')
        def execute(self):
                self.autoprint('hello, this is a high level collection of functions to print text')
                self.autoprint('it will be used to create a collection of AI programs that share some core feature, for example color coded voice tones and on the fly insults. this is the standard speech settings')
                self.wordByWordPrint(self.gprint('this is pleased voice. I am very pleased','pleased'))
                self.wordByWordPrint(self.gprint('this is excited voice. I am very excited','excited'))
                self.wordByWordPrint(self.gprint('this is angry voice. I am very angry','angry'))
                self.wordByWordPrint(self.gprint('theres also quiet','quiet'))
                self.wordByWordPrint(self.gprint('and confused','confused'))
                self.wordByWordPrint(self.gprint('and annoyed','annoyed'))
                self.wordByWordPrint(self.gprint('and sarcastic','sarcastic'))
                self.wordByWordPrint(self.gprint('and dramatic','dramatic'))
                self.wordByWordPrint(self.gprint('and amused','amused'))
                self.wordByWordPrint(self.gprint('and in critical condition','warning'))
                self.wordByWordPrint(self.gprint('and insane','insane'))
                self.autoprint("have an on-the-fly insult, too")
                self.autoprint(insult.giveInsult(None,None,None,None))
                self.autoprint('you may also notice executables are extremely cleaned up and ful;y functional, and that the ps1 is waaay cooler. That is about it.')
