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
                                self.say('okay... hold on a sec. By the way, two and nine.')
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
                print ' '
                print 'Warning: shutting down this doorway artificial intelligence will result in short term memory corruption and successive deletion. Continue Y/n : Yes'
                print ' '
                time.sleep(0.2)
                speech.say('Well done. You have just entered a doorway. Now try another.')
                return True

class ExecutePath2(path):
        def __init__(self):
                path.__init__(self,'door','Blank, steel walled room. A sign reads: Well done! You are clearly a genius. The challenge will seriously be way easier than this.')
                self.visited = False
                self.entered = False
        def execute(self):
                if self.visited == False:
                        speech.say("Hello. Why are you here? You can only get in if you answer the question. Wow... This is dull. Anyway, heres the question and all that.",'sad')
                else:
                        speech.say("Oh its you again... Well, here is the question.",'sad')
                if self.entered == True:
                        speech.say("Why are you trying to gain entry again, anyway? Anyway, as I said, you still need to answer the questions.",'sad')
                time.sleep(0.5)
                answer = speech.ask("Wow what is the point of this question anyway... Oh well. What is a quasar? a) A rare and super-bright blue giant star b) The core of a tardis c) A red spectrum d) A species of indonesian rodent e) Not a, the, its a moon of jupiter f) 42 g) A very bright blue cosmic mass found near black holes h) A very bright red cosmic mass found near the center of dark matter clumps and therefore used to map dark matter clumping i) A giant red pulsar j) A brand of shoe k) A collapsing white dwarf l) The general name for a cosmic anomaly m) A bright star n) A burning comet o) A cirritulus zarker p) A roasted peice of fungus on a stick. q) An occurence similar to a singularity r) A blob of goose fat. Answer as a letter (no caps)",mood='sad')
                time.sleep(0.2)
                answer2 = speech.ask("Well done and all that, you are right. So, now. What is a chameleon hexbox? a) An executable 'box' bundle of hex language learning chamelion programs b) A chamelion program using the new hexbox library for escaping supposedly 'secure' sandbox programs c) A shython sandbox used to train chameleons safely d) A hex chameleon that teaches itself to 'box' your computer, or turn it into a useless box of molten silicon e) A hex chameleon with restrictions that keep it in it's box, a directory it may not leave, though it may navigate through children directories f) The name for the hex version of chameleon g) The usual but not current confinement of the hex chameleon sentinel that you must later face",mood='sad')
                time.sleep(0.2)
                if answer == 'g' and answer2 == 'c':
                        if self.entered == True:
                                speech.say("you get entry, again. How monotonous...",'sad')
                        elif self.visited == True:
                                speech.say("Well done and all that. That was probably the most interesting thing that happened in a while, and no offense but your not even that interesting. Took you a few tries, though. Bye then.",mood='sad')
                                speech.say("Congratulations. You have just learned about doorways, though you have failed to anwer the question correctly from your first try. Your next training feature will pertain to hidden directories. Read about them by using the command cat to veiw the file. Good luck.")
                        else:
                                speech.say("Well done and all that. That was probably the most interesting thing that happened in a while, and no offense but your not even that interesting. Bye then.",mood='sad')
                                speech.say("Congratulations. You have just learned about doorways. Your next training feature will pertain to hidden directories. Read about them by using the command cat to veiw the file. Good luck.")
                        return True
                else:
                        speech.say("Well done. I guess you will be leaving now. Opening doorway... 5... 4... 3... 2... 1... Actually I lied. You failed. You can't get in. Really though, I can't see why you would want to.",'sad')
                        return None

class prog1(program):
        def __init__(self):
                program.__init__(self,'program1')
                #here is also a good place to make remembered variables, or pickled variables, stored in self.variable
                self.thing = False
        def execute(self):
                if self.thing == False:
                        speech.ask("Hello, how are you? : ")
                        speech.say("eh? Whatever. My task of freindly greetings is complete. By now.")
                        self.thing = True
                else:
                        speech.say("Why are you talking to me again? I don't have to greet you this time, and I have better things to do right now. Bye!",'angry')

class prog2(program):
        def __init__(self):
                program.__init__(self,'program5')
                #here is also a good place to make remembered variables, or pickled variables, stored in self.variable
                self.thing = False
        def execute(self):
                if self.thing == False:
                        speech.say("I don't know where I am...",'scared')
                        self.thing = True
                else:
                        speech.say("I obviously still don't know where I am so why are you still talking to me!!!",'angry')

class prog3(program):
        def __init__(self):
                program.__init__(self,'program11')
                #here is also a good place to make remembered variables, or pickled variables, stored in self.variable
                self.thing = False
        def execute(self):
                if self.thing == False:
                        speech.say("Snap snap snap I'm a lizard")
                        self.thing = True
                else:
                        speech.say("Still a lizard.")

class prog4(program):
        def __init__(self):
                program.__init__(self,'program52andAhalf')
                #here is also a good place to make remembered variables, or pickled variables, stored in self.variable
                self.thing = False
        def execute(self):
                if self.thing == False:
                        speech.say("beutiful day isn't it? actually according to my data banks it is likely raining or at least cloudy as you read this, but rain is nice. By the way, you should really listen to all of us even after you find what you need.",'happy')
                        self.thing = True
                else:
                        speech.say("AAAAAAHH!!!!!!!!!!!!!!!!!! HELP!!!!!!!!!!!!!!!!",'scared')

class prog5(program):
        def __init__(self):
                program.__init__(self,'program72')
                #here is also a good place to make remembered variables, or pickled variables, stored in self.variable
                self.thing = False
        def execute(self):
                if self.thing == False:
                        speech.ask("Do you want help? : ")
                        speech.say("Is that english? Oh whatever. Anyway, here is your help. Beware the sparrows, count the shadows, don't trust the sentinel.")
                        self.thing = True
                else:
                        speech.say("TIME IS THE ANSWER",'happy')

class prog6(program):
        def __init__(self):
                program.__init__(self,'program37')
                #here is also a good place to make remembered variables, or pickled variables, stored in self.variable
                self.thing = False
        def execute(self):
                if self.thing == False:
                        for thing in range(10):
                                speech.say("Blub blub blub blub blub I'm a fish. Blub blub blub blub blub I'm a fish. Blub blub blub blub blub I'm a fish. Blub blub blub blub blub I'm a fish. Blub blub blub blub blub I'm a fish. Blub blub blub blub blub I'm a fish. Blub blub blub blub blub I'm a fish. Blub blub blub blub blub I'm a fish. Blub blub blub blub blub I'm a fish!",'happy')
                        self.thing = True
                else:
                        speech.say("BLUB!!!!! FISH!!!!!!!!!!!! TALK TO THIRTY SIX!",'angry')

class prog7(program):
        def __init__(self):
                program.__init__(self,'program36')
                #here is also a good place to make remembered variables, or pickled variables, stored in self.variable
                self.thing = False
        def execute(self):
                if self.thing == False:
                        speech.ask("Tell me. What is the logic of choosing program thirty six? : ")
                        speech.say("Oh, I see. You can't speak... You don't even know how to look, do you? Well, visit again sometime, okay?")
                        self.thing = True
                else:
                        speech.say("Hello agian! Here is a lesson on looking! Type look!",'happy')

class win(program):
        def __init__(self):
                program.__init__(self,'IC:level2outOf7')
        def execute(self):
                speech.say("Actually, you are done with the test. Surprise! Anyway, here come the results .......... ........... ........... .............................. ................. ................ ......................................................... ............................. ........... ...... ... .... Oh! You passed with flying colors! Well, good job. Actually, again, I lied. It's good practice for the challenge. You failed with colors that went up into the air, caught fire, had their wings fall off, and then plummetted down in a spectacular explosion and sank through the earth's crust never to be seen again. But on the bright side, you still get to do the challenge! Safety regulations are pretty loose! Anyway, You also get use back to your computer for now. You'll be contacted by the challenge administration office when the last contestant in the challenge dies and the system becomes vacant. Expect an email from TrevorKirkby123... So to leave, it should be obvious. You know what to type to leave by now I trust? Good, then give the leave command.")

#SEE challenge
