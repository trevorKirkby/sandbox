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
        def wordByWordPrint(self,text1,waitTime):
                text = text1.split()
                for word in text:
		        randthing = random.choice(range(waitTime)) + 1
		        randVariable = randthing/5
		        print word,
		        print " ",
		        sys.stdout.flush()
		        time.sleep(randVariable)
        def gprint(self,text,adj='standard'):
                if adj == 'standard':
                        return colored(text, 'red', 'on_yellow', attrs=['dark','underline'])
                if adj == 'pleased':
                        return colored(text, 'red', 'on_yellow', attrs=['dark','underline'])
                if adj == 'excited':
                        return colored(text, 'red', 'on_yellow', attrs=['dark','underline'])
                if adj == 'angry':
                        return colored(text, 'red', 'on_yellow', attrs=['dark','underline'])
                if adj == 'quiet':
                        return colored(text, 'red', 'on_yellow', attrs=['dark','underline'])
                if adj == 'annoyed':
                        return colored(text, 'red', 'on_yellow', attrs=['dark','underline'])
                if adj == 'sarcastic':
                        return colored(text, 'red', 'on_yellow', attrs=['dark','underline'])
                if adj == 'dramatic':
                        return colored(text, 'red', 'on_yellow', attrs=['dark','underline'])
                if adj == 'amused':
                        return colored(text, 'red', 'on_yellow', attrs=['dark','underline'])
                if adj == 'warning':
                        return colored(text, 'red', 'on_yellow', attrs=['dark','underline'])
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
        def autoprint(self,text,timewait):
                self.wordByWordPrint(self.dprint(),timewait)
        def remember(self,variable):
                self.STIPM = variable
                #short term inter program memory
