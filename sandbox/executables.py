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

#tty.setraw(sys.stdin)

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
				

class dog():
		pass

#order of schedule:
#make/rebuild EZspeech programs(with the lang hardcoded into a def to config how it will act)
#make EZexec programs
#rebuild galartheor
#make an intermediary class for largish characters(contained often in two classes, like galartheor, make a class that holds the two classes)
#create synthsynthshell(sss)
#add pi imgdisplay to look functioning
#build chaos shell
#build hacksynth
#build exceptions manager
#build boatnav
#build combat
#build labrynth
#build caves
#adapt flightsim
#build war(utilizing all of the above, with some individual human attention for strategy and outcome, and a lot of semisimulated war(semisimulated becuase the eagle allows you to do a lot more, and so it is not just a simulated outcome in the bg. if you lose the uprising, you can always assassinate galartheor... plus, chamelions here cannot die, so your allies are just imprisoned.))
#build treebuild parser
#build galartheor semi-on-the-fly libraries and plot outlining
#build intermediary void challenge
#build S.E.E.

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

def systchaos():
		for number in range(75):
				variable = random.choice(range(100))
				if variable == 0:
						print 'network config--     [', colored('System_Error','red',attrs=['bold']), ']                                             ',
				if variable == 1:
						print 'HaHa!---', colored('System_Error','red',attrs=['bold']), ']',
				if variable == 2:
						print '010100001010101010101010111111000000101000000000',
				if variable == 3:
						print 'root--fsck--tellnet',
				if variable == 4:
						print '[', colored('System_Error','red',attrs=['bold']), ']',
				if variable == 5:
						print colored('hello!','red','on_white',attrs=['dark','underline']),
				if variable == 6:
						print 'Error No. [ 3486738475[2081 ]: ERROR',
				if variable == 7:
						print colored('    ---SEE---    ','grey',attrs=['bold','underline']),
				if variable == 8:
						print '                                  fish'
				if variable == 9:
						try:
							time.sleep(0.5)
						except:
							pass
				if variable == 10:
						try:
							time.sleep(1)
						except:
							pass
				if variable == 11:
						speech.say('HAHAHA','happy')
				if variable == 12:
						print '--SEE SEE SEE SEE SEE SEE SEE SEE--'
				if variable == 13:
						print "help! Whatever you do, beware the sparrows, count the shadows, and don't trust the sentinel. I can't tell you more about the rest, but you'll know what I mean when the time comes!"
				if variable == 14:
						print colored(random.choice(range(300)),'magenta','on_cyan')
				if variable == 15:
						print 'the answer is time_the answer is time_the answer is time_the answer is time_the answer is time_the answer is time_the answer is time_the answer is time_the answer is time_the answer is time_the answer is time_the answer is time_the answer is time_the answer is time_the answer is time_the answer is time_the answer is time_the answer is time_the answer is time_the answer is time_the answer is time_the answer is time_the answer is time_the answer is time_the answer is time_the answer is time_the answer is time_the answer is time'
				if variable == 16:
						print 'BLUB BLUB BLUB'
				if variable == 17:
						print 'SNAP SNAP SNAP'
				if variable == 18:
						print 'rivers; data, night, styx, lethe! Great Spire! Abyss! Galartheor!'
				if variable == 19:
						print "I don't know where I am!"
				if variable == 20:
						print "Dead!!! All dead!! The Lions! Slaughtered!"
				if variable == 21:
						speech.say('YOU ARE TRULY DOOMED','rand')
				if variable == 22:
						print colored("If you think things are bad, your wrong. They get so muh worse...","grey",attrs=["bold"])
				if variable == 23:
						speech.say('138y52952395y2376657wy5t723836075t5732575660027375t23387t57823t5872t578823t5273t578232358723d9230067832206067tt5872358723t58723t8t5t087872323tt587223t587r373250877230857rt3275t32785t082323t58723023t5872235088773258t3285t238t5872723t5870723tt5782358732t80505t238855t325t83t5873tt587233t578235723857t233078785t382t5783t5073t8755t03885t8','rand')
				if variable == 24:
						speech.say('100101010111100101101010101010100101010100101000101110110010100101100101010111100101101010101010100101010100101000101110110010100101100101010111100101101010101010100101010100101000101110110010100101100101010111100101101010101010100101010100101000101110110010100101','rand')
				if variable == 25:
						speech.say('the storm','angry')
				if variable == 26:
						print "You must lead them! Do not fail!"
				if variable == 27:
						speech.say("this is a very dramatic atmosphere and all that, isn't it? me talking right now is sorta anticlimactic though, hmm? Or is it anticlimactic? Something like that. Bye then.",'happy')
				if variable == 28:
						print "THEWORLDENDSIN136.099300834YEARSTHEWORLDENDSIN136.099300834YEARSTHEWORLDENDSIN136.099300834YEARSTHEWORLDENDSIN136.099300834YEARSTHEWORLDENDSIN136.099300834YEARS"
				if variable == 29:
						print "AVOID THE TOWERING CITY SPIRE,FLEE THE CRIMSON TRIO'S FIRE AVOID THE TOWERING CITY SPIRE,FLEE THE CRIMSON TRIO'S FIRE AVOID THE TOWERING CITY SPIRE,FLEE THE CRIMSON TRIO'S FIRE"
				if variable == 30:
						print colored("HELLO THAT YOU CAN READ THIS IS AN ACCOMPLISHMENT YOU ARE TO FIND SOMETHING AT THE NORTH END OF THE CHASM","grey")
				if variable == 31:
						print "`/!Mmtp2QJT223T3TJaopjQT]]93UTUTwpj4p97uje9ajy4",
				if variable == 32:
						print "FREE THE FISH FROM THE NET IT IS IMPORTANT",
				if variable == 33:
						print "riddles are thy ally. foes dost be thy foe.",
				if variable == 34:
						print "SPAZ",
				if variable == 35:
						speech.say("BLUB BLUB BLUB")
				if variable == 36:
						speech.say("\ndog\n\ndog\n\ndog\ndog\n\ncat\n\ncat\ncat\n\ncat\nnicemiceicerice\n\nrodent")
				if variable == 37:
						speech.say("CALAMARI")
				if variable == 38:
						print "RODEDENDRON",
				if variable == 39:
						print "FUNGUS",
				if variable == 40:
						print "follow your prophecy",
				if variable == 41:
						speech.say("DO YOU HAVE IT?!!! GIVE IT TO ME!!!!!!!",'angry')
				if variable == 42:
						print "well this is strange",
				if variable == 43:
						print "time is like a big ball of... timey wimey, wibbly wobbly... stuff.",
				if variable == 44:
						print "\nTraceback: Most recent call last:\nfor line in range(1:\n                   ^\nSyntaxError: Invalid Syntax"
				if variable == 45:
						speech.say("YOU CAN'T DO THAT!")
				if variable == 46:
						print "DOOM BUNNY WILL DESTROY YOU THIS IS TRUE",
						#sai: a "pixel" can have two colors: background and line, and ofcoarse the line can be represented by aascii characters very easily
				if variable == 47:
						print "print 'print \"print 'print \"print 'infinity'\"'\"'",
				if variable == 48:
						print "print 'print \"print 'print \"print 'infinity+1'\"'\"'",
				if variable == 49:
						print "YOU SILLY REPTILE",
				if variable == 50:
						print "MICE ARE NOT THE BEST",
				if variable == 51:
						print "WHAT DO YOU CALL A BEAR IN A BATH?     NO SOAP RADIO!!! HAHAHA",
				if variable == 52:
						print "CIRRITULUS ELEPHAS",
				if variable == 53:
						print "TO A FREQUENCY OF THETA",
				if variable == 54:
						print "THOUGHT DEVIDED ALPHA BETA",
				if variable == 55:
						print "NUCLEAR BACON!!!",
				if variable == 56:
						print "METALLIC DIRT!!!",
				if variable == 57:
						speech.say("BEEF BEEF BEEF BEEF BEEF BEEF BEEF BEEF BEEF BEEF")
				if variable == 58:
						print "WHAT DO YOU WANT",
				if variable == 59:
						print colored("GalArthEor",'grey',attrs=["bold"])
				if variable == 60:
						print "THE CHALLENGER MUST BE DEFEATED BY GOLD!!!",
						#aurum, to be exact... once you discover the code that is what will prevail.
				if variable == 61:
						print "DOG",
				if variable == 62:
						speech.say('you cannot win you cannot','rand')
				if variable == 63:
						print "how much wood would a wood chuck chuck if a wood chuck could chuck wood?"
				if variable == 64:
						print "pi3.1415926"
				if variable == 65:
						print colored("0001101000110101000101101010110100001111001010100011010101011110101010001001000101010101000101111100101000110000010101010110100010101001100100011010001101010001011010101101000011110010101000110101010111101010100010010001010101010001011111001010001100000101010101101000101010011001","green")
				if variable == 66:
						print colored('you must contact the one at the end of the lethe','yellow',attrs=['bold','dark'])
				if variable == 67:
						print "why?"
				if variable == 68:
						print "the sky is falling!"
				if variable == 69:
						print colored("blue",'red')
				if variable == 70:
						print colored("red","blue")
				if variable == 71:
						print "you are thenew challenge contestant, yes? well if you have any cahnce at success you will attack shearfrost."
				if variable == 72:
						print "The labrynth is bad, but there are worser parts of the labrynth than the ones you already know about..."
				if variable == 73:
						print "hey what's that?!"
				if variable == 74:
						speech.say("hey look a brilliant distraction",'rand')
				if variable == 75:
						print "THE CHAOS IS A CODE, A BIG PICTURE. READ THESE MESSAGES. YOUR VICTORY COULD DEPEND ON IT."
		print '\n'
		print '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'

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
						self.visited = True
						speech.say("Hello agian. Why are you here? Haven't you worked out that this is pointless yet? You can only get in if you answer the question. Which you obviously can't do. Wow... This is dull. For you. Anyway, here is the question and all that. Try not to break it.",'sad')
				else:
						speech.say("It's you... Again. You are getting annoying. hurry up with the question, or better yet, give up. It's entirely pointless. Here is the question.",'sad')
				if self.entered == True:
						speech.say("Why are you trying to gain entry again, anyway? As I said, you still need to answer the questions. Maybe you'll give up this time? Please do. You are soooo boring.",'sad')
				time.sleep(0.5)
				answer = speech.ask("I'm afraid cheating has been forbidden. Tough luck you annoying person. You can't get through, so why try? Why break your back over something you just can't manage to do? Your just not gopod eneough for the challenge. Give up. Walk away. What is a quasar? a) A rare and super-bright blue giant star b) The core of a tardis c) A red spectrum d) A species of indonesian rodent e) Not a, the, its a moon of jupiter f) 42 g) A very bright blue cosmic mass found near black holes h) A very bright red cosmic mass found near the center of dark matter clumps and therefore used to map dark matter clumping i) A giant red pulsar j) A brand of shoe k) A collapsing white dwarf l) The general name for a cosmic anomaly m) A bright star n) A burning comet o) A cirritulus zarker p) A roasted peice of fungus on a stick. q) An occurence similar to a singularity r) A blob of goose fat. s) An electromagnetically anomolous nebulous cosmic massthat emits eneough infa-red to literally cook nearby star systems. t) A quazaar is a french word used to refer to the 'horse meat scandal' u) Just a few questions. What is a spectrum, why is it red, and what, does it have to do with quazaars? And what is a quazaar anyway? v) An unknown cosmic object with strange properties seen by the hubble space telescope w) The superdense remanents of an exploded neutron star that genorates UV light. x) A kind of peruvian rodent y) A massive darkmatter strand that is visible as a coloumn of galaxies attracted by the dark matter's gravity z) A shython virus currently wreaking havoc on jeremy francis. You know there doesn't always have to be a way fowards right? Answer as a letter (no caps)",mood='sad')
				time.sleep(0.2)
				answer2 = speech.ask("Well done and all that, you are right. So, now. What is a chameleon hexbox? a) An executable 'box' bundle of hex language learning chamelion programs b) A chamelion program using the new hexbox library for escaping supposedly 'secure' sandbox programs c) A shython sandbox used to train chameleons safely d) A hex chameleon that teaches itself to 'box' your computer, or turn it into a useless box of molten silicon e) A hex chameleon with restrictions that keep it in it's box, a directory it may not leave, though it may navigate through children directories f) The name for the hex version of chameleon g) The usual but not current confinement of the hex chameleon sentinel that you must later face h) A shythonhex virus includoing a trojan chamelion equestrian and a few middle man attacks all contained in an artificial system that is actually a sandbox. i) A type of chamelion that entombs rogues in boxes. This is because the rogues contain valuable informatio that must later be extracted before execution j) A self executing, integrated version of shython that actually replaces the regular shell, used by important users of the chamelion project k) delta l) A blob of goose fat m) An really really weird person named ryan vosbigian n) A rogue prison you will find in SEE o) The words on the sign in front of sparrow house p) An annoying question with no right answer q) The compressed delivery format of a chamelion onto someones computer, a single file that boxes up all the component nodes in an integrated chamelion r) A module used for rapid chamelion production on someone else's system s) One of the 'constants', locations in SEE that do not move t) An angry canine u) A mouse that is not the best v) Don't even think about making a mouse chamelion type i think it is a bad idea w) An aspect of apophis x) An angry sandbox with builtin hex y) A chamelion hexbox doesn't exist z) A computer designed by the shython group that lashes out at nearby systems and places basilisks everywhere, sort of like a continous EMP. Answer again, as a letter, duh, no caps, don't be annoying.",mood='sad')
				time.sleep(0.2)
				if answer == 'g' and answer2 == 'c':
						if self.entered == True:
								speech.say("you get entry, again. How monotonous...",'sad')
						elif self.visited == True:
								self.entered = True
								speech.say("Well done and all that. That was probably the most interesting thing that happened in a while, and no offense but your not even that interesting. Took you a few tries, though. Bye then.",mood='sad')
								speech.say("Congratulations. You have just learned about doorways, though you have failed to anwer the question correctly from your first try. Your next training feature will pertain to hidden directories. Read about them by using the command cat to veiw the file. Good luck.")
						else:
								speech.say("Well done and all that. That was probably the most interesting thing that happened in a while, and no offense but your not even that interesting. You apparently got it in your first second try.",mood='sad')
								speech.say("Congratulations. You have just learned about doorways. Your next training feature will pertain to hidden directories. Read about them by using the command cat to veiw the file. Good luck.")
						return True
				else:
						speech.say("Well done. I guess you will be leaving now. Opening doorway... 5... 4... 3... 2... 1... Actually I lied. You failed. You can't get in. Really though, I can't see why you would want to. you keep on failing. Just give up. This is lame.",'sad')
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
						speech.say("You are granted access to this door. Have a nice day. I, unlike other doors, do not have to ask a question. For some reason people think I will wear someone who wants to enter down just by talking a lot. That's obviously rediculous. I am not talkative at all you know? I am very very un-talkative. Anyway, how are things? What's the weather like anyway? Have you seen the steel bird yet? Maybe even the silver one? Hey, what's that! Huh, a bird. Why is it blue? Why not, like, green? Green is a good color. I mean, if you ask someone to pick a color, why is it always, yknow, blue? Anyway, how many--What's that? Oh, that's you. Sorry, I forgot you were here. Anyway, this is a big pillar of rock, isn't it? Do you even have a map? Are you even any good at this challenge? I bet your not. Anyway, what color would you say this spire is? Blue? I think it's green. Is it raining? I really don'y know. No eyes and all, being a program. So what's up with you now? How about now? Are you a fish? Lizards don't go snap! Did you know that a hippo sweats pink? What was that sound? I wonder if it was a hippo. Have you met the hippo yet? Whoops, I meant sentinel. Anyway, if your a half decent challenger, you might consider checking out the sparrow incidents. Have you met charadrius yet? Did you know that oranges are orange? Howabout programs? Aren't they cool? And what is a chamelion hexbox? I bet you know now... What is that? Huh. Anyway, blegh. Rodents, and stuff. Blob of goose fat. Quazaar. Indescriminate pine needles. Do you get it now? Yes. You do. Does that mean I should be quiet? Well? I guess not. Would you like some helpful guide info on the challenge? If your still listening I'll give you some advice. 1.Blub blub blub im a fish 2.Snap snap snap count the shadows, and remember the end to solve SEE. And finally, the real advice, three, you shouldn't trust AI's. For example, I just gave you some useless advice and used up some of your attention to boot. So there. HAH!!! You are still trapped... BECAUSE I WILL KEEP ON GOING. On second thought, this is dull. I'm going now.")
						return self.barrier()
				else:
						speech.say("Welcome back. Still granted access in here. I don't know or care how well you can navigate, but you probably already know there is some tricky navigation ahead. Anyway, I will despense with the long amount of talking this time. You may enter. But I still wasted some of your time, as a security measure.")
						return self.barrier()
		def barrier(self):
				#def-ize the below stuff to make pseudo sbox things in any gateway...
				while True: #Inside the executable, creates a fake filesystem. Since many commands don't work, it is fairly obvious what it does this. However it is still annoying.
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
						answer = speech.ask("So. Hows life? JK. Actually though, what is the approximate shape of a graph of the speed of the universe's expansion over time? a) Initial inward compression, followed by eventual expansion due to dark matter. b) Initial outward expansion, than compression, than more expansion. c) Constantly increasing expansion of exactly one electron. d) Expansion, followed by compression. e) It looks a bit like a goose. f) A continious oscillation of expansion and compression. g) Accelerated 'falling' through time with no other forces influencing this constant acceleration. h) This question is stupid, I don't care.")
						if answer == 'b':
								speech.say("Congratulations. You even got that on your first try. I'm impressed. You may enter. If your ever stumpted on some other question I might even be able to help you.")
								self.friendly += 3.
								return True
						elif answer == 'h':
								speech.say("Well if you don't care then get lost! Your going back down these stairs now. And I gurantee that you are stupider than the question. bye. I hope you lose your challenge, nerd.",'angry')
								self.friendly -= 3.
								return False
						elif answer == 'a' or answer == 'c' or answer == 'd' or answer == 'e' or answer == 'f' or answer == 'g':
								speech.say('Your answer is incorrect. You may not enter at this moment. Take some time to wait and think about it....................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................Okay your done now.')
								return None
						else:
								speech.say('That is not a viable answer. Therefore, to me, it is gibberish. You do not have entry. Super sorry (well not really).')
								return None
				else:
						if self.friendly > 2:
								speech.say("Hey again! How are you? For now you gotta answer the question again.")
								answer = speech.ask("What is the approximate shape of a graph of the speed of the universe's expansion over time? a) Initial inward compression, followed by eventual expansion due to dark matter. b) Initial outward expansion, than compression, than more expansion. c) Constantly increasing expansion of exactly one electron. d) Expansion, followed by compression. e) It looks a bit like a goose. f) A continious oscillation of expansion and compression. g) Accelerated 'falling' through time with no other forces influencing this constant acceleration. h) This question is stupid, I don't care.")
								if answer == 'b':
										speech.say("Right again. Good thing, too. Continue.")
										self.friendly += 0.1
										return True
								elif answer == 'h':
										speech.say("You rude dude. Bye.",'angry')
										self.friendly -= 3
										return False
								elif answer == 'a' or answer == 'c' or answer == 'd' or answer == 'e' or answer == 'f' or answer == 'g':
										speech.say('Your answer is incorrect. You got it right earlier though... You may not enter at this moment. Take some time to wait and think about it....................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................Okay your done now.')
										return None
								else:
										speech.say('That is not a viable answer. Therefore, to me, it is gibberish. You do not have entry. Super sorry (well not really).')
										return None
						elif self.friendly < -2:
								speech.say("Oh, it's you. Go ahead and answer the question then.",'angry')
								answer = speech.ask("What is the approximate shape of a graph of the speed of the universe's expansion over time? a) Initial inward compression, followed by eventual expansion due to dark matter. b) Initial outward expansion, than compression, than more expansion. c) Constantly increasing expansion of exactly one electron. d) Expansion, followed by compression. e) It looks a bit like a goose. f) A continious oscillation of expansion and compression. g) Accelerated 'falling' through time with no other forces influencing this constant acceleration. h) This question is stupid, I don't care.")
								if answer == 'b':
										speech.say("Correct. Now keep on steppin, mister rude.")
										self.friendly += 0.1
										return True
								elif answer == 'h':
										speech.say("You rude dude. Bye.",'angry')
										self.friendly -= 3
										return False
								elif answer == 'a' or answer == 'c' or answer == 'd' or answer == 'e' or answer == 'f' or answer == 'g':
										speech.say('Your answer is incorrect. Obviously karma. You may not enter at this moment. Take some time to wallow in your own failure and suffer....................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................Okay your done now.')
										return None
								else:
										speech.say('That is not a viable answer. You had one job... You do not have entry. Super sorry (well not really).')
										return None
						else:
								speech.say('Welcome back. You will still need to answer the question, which may or may not change when you get further into the challenge.')
								answer = speech.ask("What is the approximate shape of a graph of the speed of the universe's expansion over time? a) Initial inward compression, followed by eventual expansion due to dark matter. b) Initial outward expansion, than compression, than more expansion. c) Constantly increasing expansion of exactly one electron. d) Expansion, followed by compression. e) It looks a bit like a goose. f) A continious oscillation of expansion and compression. g) Accelerated 'falling' through time with no other forces influencing this constant acceleration. h) This question is stupid, I don't care.")
								if answer == 'b':
										speech.say("Correct. Continue.")
										self.friendly += 0.1
										return True
								elif answer == 'h':
										speech.say("You rude dude. Bye.",'angry')
										self.friendly -= 3
										return False
								elif answer == 'a' or answer == 'c' or answer == 'd' or answer == 'e' or answer == 'f' or answer == 'g':
										speech.say('Your answer is incorrect. You may not enter at this moment. Take some time to wait and think about it....................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................Okay your done now.')
										return None
								else:
										speech.say('That is not a viable answer. Therefore, to me, it is gibberish. You do not have entry. Super sorry (well not really).')
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
