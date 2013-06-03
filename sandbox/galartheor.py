import executables as ex
import time
from termcolor import cprint, colored
import sys
import insult
import math
import random
import speech as s

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
                self.comments = {}
                self.commentsLocation = 0
                #remember- add a taunt instances program to give pre-typed taunts according to performance on the fly and according to mood, and an autotaunt piped through autoprint that gives a taunt depending on mood(some taunts are just your dumb some are more amusing)
        def wordByWordPrint(self,text,waitTime=2):
                for word in text:
		        randthing = random.random()
		        randVariable = float(randthing/waitTime)
		        sys.stdout.write(word)
		        sys.stdout.flush()
		        time.sleep(randVariable)
        def gprint(self,text,adj='standard',nobreakage=True):
                if nobreakage == True:
                        words = text.split()
                        newText = []
                        for word in words:
                                word = word + ' '
                                if adj == 'standard':
                                        newText.append(colored(word, 'red', 'on_white', attrs=['dark','underline']))
                                elif adj == 'pleased':
                                        newText.append(colored(word, 'blue', 'on_cyan', attrs=['bold']))
                                elif adj == 'excited':
                                        newText.append(colored(word, 'yellow', 'on_blue', attrs=['dark','bold','underline']))
                                elif adj == 'angry':
                                        newText.append(colored(word, 'red', attrs=['bold','underline']))
                                elif adj == 'quiet':
                                        newText.append(colored(word, 'blue', 'on_white', attrs=['dark','underline']))
                                elif adj == 'confused':
                                        newText.append(colored(word, 'cyan', 'on_white', attrs=['dark']))
                                elif adj == 'annoyed':
                                        newText.append(colored(word, 'yellow', attrs=['underline']))
                                elif adj == 'sarcastic':
                                        newText.append(colored(word, 'white', 'on_yellow', attrs=['bold','underline']))
                                elif adj == 'dramatic':
                                        newText.append(colored(word, 'green', 'on_red', attrs=['bold','underline']))
                                elif adj == 'amused':
                                        newText.append(colored(word, 'green', 'on_grey', attrs=['dark','bold','underline']))
                                elif adj == 'warning':
                                        newText.append(colored(word, 'red', 'on_yellow', attrs=['dark','bold']))
                                elif adj == 'insane':
                                        newText.append(colored(word, 'magenta', 'on_yellow', attrs=['bold','underline']))
                                else:
                                        print 'Error: Galartheor: gprint: Bad Adjective'
                                        raise KeyboardInterrupt
                        return newText
                else:
                        if True:
                                if adj == 'standard':
                                        text = (colored(text, 'red', 'on_white', attrs=['dark','underline']))
                                if adj == 'pleased':
                                        text = (colored(text, 'blue', 'on_cyan', attrs=['bold']))
                                if adj == 'excited':
                                        text = (colored(text, 'yellow', 'on_blue', attrs=['dark','bold','underline']))
                                if adj == 'angry':
                                        text = (colored(text, 'red', attrs=['bold','underline']))
                                if adj == 'quiet':
                                        text = (colored(text, 'blue', 'on_white', attrs=['dark','underline']))
                                if adj == 'confused':
                                        text = (colored(text, 'cyan', 'on_white', attrs=['dark']))
                                if adj == 'annoyed':
                                        text = (colored(text, 'yellow', 'on_yellow', attrs=['bold','dark','underline']))
                                if adj == 'sarcastic':
                                        text = (colored(text, 'white', 'on_yellow', attrs=['bold','underline']))
                                if adj == 'dramatic':
                                        text = (colored(text, 'green', 'on_red', attrs=['bold','underline']))
                                if adj == 'amused':
                                        text = (colored(text, 'green', 'on_grey', attrs=['dark','bold','underline']))
                                if adj == 'warning':
                                        text = (colored(text, 'red', 'on_yellow', attrs=['dark','bold']))
                                if adj == 'insane':
                                        text = (colored(text, 'magenta', 'on_yellow', attrs=['bold','underline']))
                                return text
        def dprint(self,text,rejoin=False):
                if self.anger > 40:
                        marker = True
                        for number in self.emotionList:
                                if self.anger < number:
                                        marker = False
                        if marker == True:
                                if rejoin == False:
                                        return self.gprint(str(text),'angry')
                                if rejoin == True:
                                      return self.gprint(str(text),'angry',False)  
                else:
                        if rejoin == True:
                                return self.gprint(str(text),False)
                        if rejoin == False:
                                return self.gprint(text,'standard')
        def autoprint(self,text,timewait=3,dprint=True):
                if dprint == True:
                        return self.wordByWordPrint(self.dprint(text),timewait)
                else:
                        return self.wordByWordPrint(self.gprint(text,adj=dprint),timewait)
        def remember(self,variable):
                self.STIPM = variable
                #short term inter program memory
        def greply(feild,hear,reply,timewait,voice='standard'):
                self.autoprint(s.reply(feild,hear,reply),timewait,voice)

class samplePrinter(gProg):
        def __init__(self):
                gProg.__init__(self,'samplePrinter')
        def execute(self):
                self.autoprint('hello, this is a high level collection of functions to print text and to share a group of variables and personalities and create methods to be able to sythesize decisions and speech to some degree')
                print ' '
                self.autoprint('it will be used to create a collection of AI programs that share some core feature, for example color coded voice tones and on the fly verbal abuse. this is the standard speech settings')
                print ' '
                self.wordByWordPrint(self.gprint('this is pleased voice. I am very pleased',adj='pleased'))
                print " "
                self.wordByWordPrint(self.gprint('this is excited voice. I am very excited',adj='excited'))
                print " "
                self.wordByWordPrint(self.gprint('this is angry voice. I am very angry',adj='angry'))
                print " "
                self.wordByWordPrint(self.gprint('theres also quiet',adj='quiet'))
                print " "
                self.wordByWordPrint(self.gprint('and confused',adj='confused'))
                print " "
                self.wordByWordPrint(self.gprint('and annoyed',adj='annoyed'))
                print " "
                self.wordByWordPrint(self.gprint('and sarcastic',adj='sarcastic'))
                print " "
                self.wordByWordPrint(self.gprint('and dramatic',adj='dramatic'))
                print " "
                self.wordByWordPrint(self.gprint('and amused',adj='amused'))
                print " "
                self.wordByWordPrint(self.gprint('and in critical condition',adj='warning'))
                print " "
                self.wordByWordPrint(self.gprint('and insane',adj='insane'))
                print " "
                self.autoprint("have an on-the-fly insult, too")
                print " "
                self.autoprint(insult.giveInsult(None,None,None,None))
                print " "
                self.autoprint('you may also notice executables are extremely cleaned up and fully functional, and that the ps1 is waaay cooler. That is about it.')
                print ""

class program(gProg):
        def __init__(self):
                gProg.__init__(self,'program')
        def execute(self):
                question = s.ask(self.gprint('Pleased to meet you. What is it? : ','standard',False))
                self.autoprint(s.reply(question,'how are you?',"I am well, thank you"),3,'standard')
                self.autoprint(s.reply(question,'Information',"If you want information, you need to start at the root of the challenge..."),3,'amused')
                self.autoprint(s.reply(question,'what do you mean',"When I say, 'hello, pleased to meet you, what is it?', I actually mean theres a giant amphibian about to stick its finger up your nose. It should be obvious."),3,'sarcastic')
                self.autoprint(s.reply(question,'who are you',"Now why would I tell you that?"),3,'amused')
                self.autoprint(s.reply(question,'shut up',"Now what is the logic in that? You activated me in the first place. Don't be silly."),3,'standard')
                self.autoprint(s.reply(question,'help',"No. Why should I help you?"),3,'annoyed')
                self.autoprint(s.reply(question,'idiot',"That wasn't very civil. You would be the idiot to continue talking that way..."),3,'angry')
                self.greply(question,'dumb',"I am a very sophisticated program. I am not 'dumb'.",3,'annoyed')
                self.greply(question,'where',"I am not telling you where anything is. You are supposed to explore",3,'standard')
                self.greply(question,'what',"I have no good reason to answer your question.",3,'standard')
                self.greply(question,'how',"There is no logical cause for you to ask a question involving how. I will not answer this.",3,'annoyed')
                self.greply(question,'who',"I am not going to answer that question.",3,'standard')
                self.greply(question,'when',"what are you asking that for? when? no.",3,'standard')
                #self.greply(question,'',"",3,'')
                #self.greply(question,'',"",3,'')
                #self.greply(question,'',"",3,'')
                #self.greply(question,'',"",3,'')
                #self.greply(question,'',"",3,'')
                #self.greply(question,'',"",3,'')
                #self.greply(question,'',"",3,'')
                question2 = s.ask(self.gprint("Anyway, good weather, isn't it? : ",'standard',False))
                self.greply(question,'not',"it's not good weather? well I wouldn't know, being a program without that data and all, but that's sounding awfully pessimistic to me.",3,'standard')
                self.greply(question,'indeed',"actually I don't know the weather but I'm sure it's very good",3,'quiet')
                self.greply(question,'yes',"well anyway, bye then. nice chatting with you.",3,'')
                #self.greply(question,'sunny',"",3,'')
                #self.greply(question,'rainy',"",3,'')
                #self.greply(question,'night',"",3,'')
                #self.greply(question,'daytime',"",3,'')
                #self.greply(question,'information',"",3,'')
                #self.greply(question,'help',"",3,'')
