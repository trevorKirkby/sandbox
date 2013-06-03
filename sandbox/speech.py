import insult as ins

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
                print index, foundIndex
        return found

def say(text,mood='norm',enter=True):
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
