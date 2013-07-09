import insult as ins
from termcolor import cprint, colored
import sys
import time
import tty
import termios
import random
import textwrap

def isIn(text,meaning):
        #ignore words, like that is good, that is #really# good
        #negatory words, like that is good, that is !not! good
        #base synonyms for more common things, like that is good, that is =great=
        #base formatting for common instances, like that is good, that's good
        #base phrase equivalents, like shut up, be quiet
        #base understanding of the concept of the double negative, like that is good, that's not bad(which will return a false, when usually no trigger returns none)
        findIn = text.split()
        findWhat = meaning.split()
        index = 0
        foundIndex = 0
        finalIndex = 0
        found = False
        marker = False
        for word in findIn:
                marker = False
                index = index + 1
                for part in findWhat:
                        if part == word:
                                if foundIndex == 0:
                                        foundIndex = index
                                        finalIndex = 0
                                        marker = True
                                if index == foundIndex and marker == True:
                                        foundIndex = foundIndex + 1
                                        finalIndex = finalIndex + 1
                                        if finalIndex == len(findWhat):
                                                found = True
                        elif marker == True:
                                marker = False
                                foundIndex = 0
                #print index, foundIndex
        return found

def say(text,mood='norm',enter=True):
                timed = None
                text = textwrap.fill(text,75)
                if mood == 'norm':
                        text = colored(text,'yellow',attrs=['bold'])
                elif mood == 'angry':
                        text = colored(text,'red',attrs=['bold'])
                elif mood == 'happy':
                        text = colored(text,'green',attrs=['bold'])
                elif mood == 'scared':
                        text = colored(text,'magenta',attrs=['bold'])
                elif mood == 'excited':
                        text = colored(text,'white',attrs=['bold'])
                elif mood == 'sad':
                        text = colored(text,'grey',attrs=['bold'])
                elif mood == 'rand':
                        nText = []
                        for letter in text:
                                thing = random.choice(['red','blue','green','yellow','white','grey','cyan','magenta'])
                                nText.append(colored(letter,str(thing),attrs=['bold']))
                        text = ''.join(nText)
                        timed = 0.01
                fd = sys.stdin.fileno()
                oldSet = termios.tcgetattr(fd)
                tty.setraw(sys.stdin)
                for word in text:
		        if timed == None:
		                randthing = random.random()
		                randVariable = float(randthing/7)
                        else:
		                randVariable = timed
                        if word == '\n':
                                termios.tcsetattr(fd, termios.TCSADRAIN, oldSet)
                                print '\n',
                                fd = sys.stdin.fileno()
                                oldSet = termios.tcgetattr(fd)
                                tty.setraw(sys.stdin)
                        else:
		                sys.stdout.write(word)
		        sys.stdout.flush()
		        time.sleep(randVariable)
                termios.tcsetattr(fd, termios.TCSADRAIN, oldSet)
                if enter == True:
                        print ' '

def ask(question,mood='norm'):
        say(question,mood,enter=False)
        variable = raw_input(' : ',)
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

def reply(qname,say,reply,returnBool=True,directedAt='me',reverseBool=False):
        #after dinner incorporate negatoried and directed at, for example if told to find if the word idiot is directed at self, will not trigger in these times because of this: your not an idiot,  or he is an idiot, also paralell synonyms, such as your and idiot and your stupid, and basic speech formatting, such as your an idiot and you are an idiot. remove punctuation, recognize negations, reference synonyms, and determine loose ordering
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

def askreply():
        pass

def talk():
        pass

def config():
        pass

#gprint termcolor.cprint('hello how are you','red','on_white',attrs=['bold','dark','underline','reverse'])

class state():
        #responsedict can contain specific config modifiers using setattribute. They just send setattribute(statename.attributename,newattribute)
        def __init__(self,question,responsedict,defaultconfig,configmodifiers,automodifiers):
                self.question = question
                self.responses = responsedict
                self.default = defaultconfig
                self.default += config modifers
                #once config is properly made, there won't be a self.default, there'll be an unpacked set of colors etc. config modifers are manually added. automodifiers are automatically added to represent mood change, thought they can be turned off
        def activate():
                answer = ask(self.question)
                
        def setattribute(attribute,new):
                attribute = new

'''

SPEECH OUTLINE

lang:

yes: 
no: 
choice [number/letter]: not [number/letter]
you: 
I: 
name: {name}
etre(all of them):
possible is adjectives:


grapes: wet raisins
raisins: dried grapes

defs:

config()
        takes any specific inclanations towards and against names, I's, and You's, takes questions it will ask and how it responds(in a treebuilder parsing stringthing), takes overall responses, takes specific phrase responses (there aren't many words you may freely combine, mind you), takes specified insult responses and general personality insult responses(in this lang), takes speech color settings for small individual AIs(bigger ones have there own class for that, and the smaller ones do have a default and all)
        Actually, scratch that. config just does general sets, most of which were listed. Then, a different def creates conversation states. This allows one question/wait/replies thing to direct to other states according to what you say. States are ordered more or less chronologically, by convention. There will also be an in state function to return anything the executable will have to do other than printing. (that includes moving things, changing permissions, granting access, et cetera. there will be a parser waiting on the other side that will execute something like mv in more complicated lowlevel scripting). Obviously, a conversation capsule is a class, whereas config creates a variable containing all the base config any other speech function will want to see (and as i said, all programs have a default config, the bigger ones even have unique defaults.)

'''
