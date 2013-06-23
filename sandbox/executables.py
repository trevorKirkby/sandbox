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
#speech and autoprint-- alternating colors, alternating caps, etc.

#PATH SPIRE:

class BridgeToTerrace(path):
        def __init__(self):
                path.__init__(self,'SketchBridge','Well done. You have safely reached an intermediary pillar. More bridge awaits.')
                self.visited = False
        def execute(self):
                if self.visited == False:
                        self.visited = True
                        speech.say("You are granted access to this door. Have a nice day. I, unlike other doors, do not have to ask a question. For some reason people think I will wear someone who wants to enter down just by talking a lot. That's obviously rediculous. I am not talkative at all you know? I am very very un-talkative. Anyway, how are things? What's the weather like anyway? Have you seen the steel bird yet? Maybe even the silver one? Hey, what's that! Huh, a bird. Why is it blue? Why not, like, green? Green is a good color. I mean, if you ask someone to pick a color, why is it always, yknow, blue? Anyway, how many--What's that? Oh, that's you. Sorry, I forgot you were here. Anyway, this is a big pillar of rock, isn't it? Do you even have a map? Are you even any good at this challenge? I bet your not. Anyway, what color would you say this spire is? Blue? I think it's green. Is it raining? I really don'y know. No eyes and all, being a program. So what's up with you now? How about now? Are you a fish? Lizards don't go snap! Did you know that a hippo sweats pink? What was that sound? I wonder if it was a hippo. Have you met the hippo yet? Whoops, I meant sentinel. Anyway, if your a half decent challenger, you might consider checking out the sparrow incidents. Have you met charadrius yet? Did you know that oranges are orange? Howabout programs? Aren't they cool? And what is a chamelion hexbox? I bet you know now... What is that? Huh. Anyway, blegh. Rodents, and stuff. Blob of goose fat. Quazaar. Silver feather and lethe water. Indescrimenate pine needles. Do you get it now? Yes. You do. Does that mean I should be quiet? Well? I guess not. Would you like some helpful guide info on the challenge? If your still listening I'll give you some advice. 1.Blub blub blub im a fish 2.Snap snap snap count the shadows, and remember the end to solve SEE. And finally, the real advice, three, you shouldn't trust AI's. For example, I just gave you some useless advice and used up some of your attention to boot. So there. HAH!!! You are still trapped... BECAUSE I WILL KEEP ON GOING. On second thought, this is dull. I'm going now.")
                        return self.barrier()
                else:
                        speech.say("Welcome back. Still granted access in here. I don't know or care how well you can navigate, but you probably already know there is some tricky navigation ahead. Anyway, I will despense with the long amount of talking this time. You may enter.")
                        return self.barrier()
        def barrier(self):
                #def-ize the below stuff to make pseudo sbox things in any gateway...
                while True:
                        try:
                                BSprompt = colored('PathSpire','green',attrs=['bold','dark','underline']) + ' ' + colored('SketchBridge','yellow',attrs=['bold']) + '/$: '
                                prompt2 = raw_input(BSprompt)
                                if prompt2 == 'ls':
                                        print colored('pathA','blue',attrs=['bold']), colored('pathB','blue',attrs=['bold']), colored('progA','green',attrs=['bold'])
                                elif prompt2 == 'exc progA':
                                        dog = speech.ask('Hello, what do you need?','sad')
                                        if dog == '13':
                                                speech.say('Oh. Right then... You may enter, of coarse.')
                                                return True
                                        else:
                                                speech.say("That's all very interesting, but there's a problem. Apparently you are supposed to move to SEE/PathSpire, or home dir... Something is pulling you there right now.")
                                                return None
                                elif prompt2 == 'look':
                                        print 'A weak looking rope bridge with a fork in the bridge and a large heavy terminal perched in between... Try not to fall and all that, as it would make for a dull ending to your challenge compared to some of the other ways...'
                                elif prompt2[0] == 'c' and prompt2[1] == 'd':
                                        while True:
                                                try:
                                                        BSprompt = colored('PathSpire','green',attrs=['bold','dark','underline']) + ' ' + colored('path','yellow',attrs=['bold']) + '/$: '
                                                        prompt2 = raw_input(BSprompt)
                                                        if prompt2 == 'ls':
                                                                cprint('path','blue',attrs=['bold'])
                                                        elif prompt2 == 'look':
                                                                print 'A long paved road with the occasional flash of silver visible in the cloudy distance... A large fast food chain sign hangs from a cord dangling through the fog. Dont ask me why, I dont know. It is even farther away then the silver flashes...'
                                                        elif prompt2 == 'cd path':
                                                                pass
                                                        elif prompt2 == 'cd ..':
                                                                return None
                                                        elif prompt2[0] == 'c' and prompt2[1] == 'd':
                                                                print prompt2, ': If you typed something that is not a viable option, fie on you. Otherwise, we are sorry to inform you that it is possible some of your functions are being jammed by someone. We appologize for the inconveneince.'
                                                        else:
                                                                print prompt2, ': We are sorry for the inconveneince but some commands are currently down. If what you typed wasnt actually a command, we are not sorry as that means this message was broadcasted due to your failure. They will be back up soon, but we beleive something is jamming some of your commands.'
                                                except KeyboardInterrupt:
                                                        print '^C'
                                                except EOFError:
                                                        print ' ' + 'EOF Error'
                                                except IndexError:
                                                        pass
                                else:
                                        print prompt2, ': We are sorry for the inconveneince but some commands are currently down. If what you typed wasnt actually a command, we are not sorry as that means this message was broadcasted due to your failure. They will be back up soon, but we beleive something is jamming some of your commands.'
                        except KeyboardInterrupt:
                                print '^C'
                        except EOFError:
                                print ' ' + 'EOF Error'
                        except IndexError:
                                pass

class QuestionGateSteelbirdNest(path):
        def __init__(self):
                path.__init__(self,'SmallWoodenGate','The platform has several potted plants growing, and a small pillar of stone covered in claw shaped notches. The switchback ramp leads onwards...')
                self.visited = False
                self.friendly = float(0)
        def execute(self):
                if self.visited == False:
                        self.visited = True
                        speech.say("Hello. Are you the new challenge contestant then? Well, whenever you cross this door, you must answer a question. Later, the question may change, but for now, it is the following.")
                        answer = speech.ask("What does the cprint function do? a) It is the function built by the challenge creator to print colored, word by word, et cetera in this cool way b) It is a function of the termios module c) It is a function of the termcolor module d) It is an intermediary definition used by the chalenge builder to print a string word by word, regardless of color e) It is a feature of the textwrap module used to make sure words do not get chopped in half on the new line f) It is a def made by the builder used to set and unset the tty setraw to prevent keyboard interference while a program talks g) It is used to chamelion print colored text in a way that chamelions talk h) It is an import module for all of the above functions created by the challenge builder. h) You don't care and you think this question is stupid")
                        if answer == 'c':
                                speech.say("Congratulations. You even guessed that on your first try. I'm impressed. You may enter, of coarse. If your ever stumpted on some other question I might even be able to help you.")
                                self.friendly += 3
                                return True
                        elif answer == 'h':
                                speech.say("Well if you don't care then get lost! Your going back down these stairs now. And this question is perfectly intelligent, it's just you who is stupid. bye. I hope you lose your challenge.",'angry')
                                self.friendly -= 3
                                return False
                        elif answer == 'a' or answer == 'b' or answer == 'd' or answer == 'e' or answer == 'f' or answer == 'g':
                                speech.say('Your answer is incorrect. You may not enter at this moment.')
                                return None
                        else:
                                speech.say('That is not a viable answer. Therefore, to me, it is gibberish. You do not have entry. Sorry.')
                                return None
                else:
                        if self.friendly > 2:
                                speech.say("Hey again! How are you? For now you gotta answer the question again but let me know if you ever need any help.")
                                answer = speech.ask("What does the cprint function do? a) It is the function built by the challenge creator to print colored, word by word, et cetera in this cool way b) It is a function of the termios module c) It is a function of the termcolor module d) It is an intermediary definition used by the chalenge builder to print a string word by word, regardless of color e) It is a feature of the textwrap module used to make sure words do not get chopped in half on the new line f) It is a def made by the builder used to set and unset the tty setraw to prevent keyboard interference while a program talks g) It is used to chamelion print colored text in a way that chamelions talk h) It is an import module for all of the above functions created by the challenge builder. h) You don't care and you think this question is stupid")
                                if answer == 'c':
                                        speech.say("Congratulations. You even guessed that on your first try. I'm impressed. You may enter, of coarse. If your ever stumpted on some other question I might even be able to help you.")
                                        self.friendly += 3
                                        return True
                                elif answer == 'h':
                                        speech.say("Why are you being annoying like that! Go back down the stairs.",'angry')
                                        self.friendly -= 3
                                        return False
                                elif answer == 'a' or answer == 'b' or answer == 'd' or answer == 'e' or answer == 'f' or answer == 'g':
                                        speech.say('Sorry but you got it wrong this time.')
                                        return None
                                else:
                                        speech.say("I'm afraid that is not a viable answer. Try again later I guess.")
                                        return None
                        elif self.friendly < -2:
                                speech.say("Oh, it's you. You may have been rude, but since I'm nice you can still enter if you answer the question.",'angry')
                                answer = speech.ask("What does the cprint function do? a) It is the function built by the challenge creator to print colored, word by word, et cetera in this cool way b) It is a function of the termios module c) It is a function of the termcolor module d) It is an intermediary definition used by the chalenge builder to print a string word by word, regardless of color e) It is a feature of the textwrap module used to make sure words do not get chopped in half on the new line f) It is a def made by the builder used to set and unset the tty setraw to prevent keyboard interference while a program talks g) It is used to chamelion print colored text in a way that chamelions talk h) It is an import module for all of the above functions created by the challenge builder. h) You don't care and you think this question is stupid",'angry')
                                if answer == 'c':
                                        speech.say("Congratulations. You guessed it. Operative word there being guessed, as you obviously didn't actually know. You are admitted... This time.",'angry')
                                        return True
                                elif answer == 'h':
                                        speech.say("Are you being rude to me again???? Not cool! You are soooo out of here!",'angry')
                                        self.friendly -= 4
                                        return False
                                elif answer == 'a' or answer == 'b' or answer == 'd' or answer == 'e' or answer == 'f' or answer == 'g':
                                        speech.say('Your answer is incorrect, so there. You may not enter at this moment. Ha ha ha.')
                                        return None
                                else:
                                        speech.say("That isn't even a proper answer. Therefore it is wrong. Ha ha ha.")
                                        return None
                        else:
                                speech.say('Welcome back. You will still need to answer the question, which may or may not change when you get further into the challenge.')
                                answer = speech.ask("What does the cprint function do? a) It is the function built by the challenge creator to print colored, word by word, et cetera in this cool way b) It is a function of the termios module c) It is a function of the termcolor module d) It is an intermediary definition used by the chalenge builder to print a string word by word, regardless of color e) It is a feature of the textwrap module used to make sure words do not get chopped in half on the new line f) It is a def made by the builder used to set and unset the tty setraw to prevent keyboard interference while a program talks g) It is used to chamelion print colored text in a way that chamelions talk h) It is an import module for all of the above functions created by the challenge builder. h) You don't care and you think this question is stupid")
                                if answer == 'c':
                                        speech.say("Congratulations. You guessed it. Not on your first try, but you'll do for the challenge perhaps. You may enter.")
                                        self.friendly += 0.5
                                        return True
                                elif answer == 'h':
                                        speech.say("Well if you don't care then get lost! Your going back down these stairs now. And this question is perfectly intelligent, it's just you who is stupid. Stop coming back here and leave me alone. bye. I hope you lose your challenge.",'angry')
                                        self.friendly -= 2
                                        return False
                                elif answer == 'a' or answer == 'b' or answer == 'd' or answer == 'e' or answer == 'f' or answer == 'g':
                                        speech.say('Your answer is incorrect. You may not enter at this moment.')
                                        return None
                                else:
                                        speech.say('That is not a viable answer. Therefore, to me, it is gibberish. You do not have entry. Sorry.')
                                        return None

class silvergate(path):
        def __init__(self):
                path.__init__(self,'SilverGate','You are inside the silver gate. That does not hold any specific significance, as you undoubtedly knew that unless you are really clueless, but whatever.')
        def execute(self):
                speech.say("Hello. The way fowards is both simple and complex, as you may already know.",'excited')
                doggy = speech.ask('Enter_The_Passkey',"excited")
                if doggy == "191030243":
                        return True
                else:
                        speech.say("You may not enter")
                        return None
        def color(self):
                return colored('SilverGate','white',attrs=['bold','underline'])

class chest2(objHold):
        def __init__(self):
                self.done=False
                objHold.__init__(self,'chest','A label reads: S.E.E: QUALITY FURNITURE GOODS')
                self.children = { }
        def execute(self):
                if self.done==True:
                        speech.say("ACESS NOT GRANTED, YOU HAVE ALREADY COLLECTED YOUR STARTER'S PACKAGE")
                        raise KeyboardInterrupt
                self.done = True
                speech.say("You may access the contents of this chest, beginner contestant. Good luck on the challenge, you will really, really need it...")
                return True
