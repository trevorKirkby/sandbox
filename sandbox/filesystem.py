#to do before challenge construct: clean up speech, make hidden dir class, and make permissions

import session
import speech
from termcolor import colored, cprint

class Node:
    def __init__(self,name,permissions):
        #you could shift a node by changing its parent, even across trees, just with a different 'directory'. why cant you do the same to a session's pwd?
        self.name = name
        self.parent = None
        self.read = False
        self.write = False
        self.execute2 = False
        for letter in permissions:
            if letter == 'r':
                self.read = True
            elif letter == 'w':
                self.write = True
            elif letter == 'x':
                self.execute2 = True
            else:
                pass
        try:
            if session.testMode == True:
                print 'name:', self.name, '   permissions:', permissions, '   read:', self.read, '   write:', self.write, '   execute:', self.execute2
        except:
            pass
    # Returns our absolute path as a string
    def abspath(self):
        path = [ self.name ]
        node = self
        while node.parent:
            node = node.parent
            path.insert(0,node.name)
        return '/'.join(path)
    def isExc(self):
        return False
    def isDir(self):
        return False
    def isFile(self):
        return False
    def isGate(self):
        return False
    def isHold(self):
        return False
    def isObj(self):
        return False
    def isPerson(self):
        return False
    def isPassage(self):
        return False
    def isAutoExc(self):
        return False
    def color(self):
        return None
        
class File(Node):
    def __init__(self,name,contents=" ",permissions='r'):
        Node.__init__(self,name,permissions)
        self.contents = contents
    def isFile(self):
        return True

class obj(Node):
    def __init__(self,name,contents=" ",permissions='rx'):
        Node.__init__(self,name,permissions)
        self.taken = False
        self.contents = contents
    def isObj(self):
        if self.taken == False:
            return True
        else:
            return False
    def isFile(self):
        if self.taken == False:
            return False
        else:
            return True

class Directory(Node):
    def __init__(self,name,look,permissions='rx'):
        Node.__init__(self,name,permissions)
        self.children = { }
        self.look = look
    # Add a generic node
    def add(self,node):
        node.parent = self
        self.children[node.name] = node
        return node
    def remove(self,node):
        newChildren = {}
        for thing in self.children.keys():
            if thing != node.name:
                newChildren[thing] = self.children[thing]
        self.children = newChildren
        return node
    # Makes and returns an empty subdirectory
    #below are some functions to create 1 way and 2 way soft links, which will be nescessary for the system. This also means you can have a soft link to a non-directory if it is one way, allowing an object to apear but not actually dwell in an area, for example a program. This would technically mean that the object would be in two places, though it would only be aware of it's location in one.
    def addlink(node):
        self.children[node.name] = node
    def add2wayLink():
        self.children[node.name] = node
        node.children[self.name] = self
    def mkdir(self,name,look,permissions='rx'):
        return self.add(Directory(name,look,permissions))
    def isDir(self):
        return True

class AED(Directory):
    def __init__(self,name,look,permissions='rx'):
        Directory.__init__(self,name,look,permissions)
    def isAutoExc(self):
        return True

class hiddenDir(Directory):
    def __init__(self,name,look,keyWord,permissions='rx'):
        Directory.__init__(self,name,look,permissions)
        self.key = keyWord
        self.found = False
    def isPassage(self):
        if self.found == False:
            return None
        else:
            return True

class Filesystem(Directory):
    def __init__(self,look):
        Directory.__init__(self,'',look,'rx')

class SuperRoot(Directory):
    def __init__(self,name,look):
        Directory.__init__(self,name,look,' ')



#objects below:


class key(obj):
        def __init__(self):
                obj.__init__(self,'key','A key shaped depression in the chest bottom...')
                self.used = False
                self.taken = False
        def use(self):
                if self.taken == True and self.used == False:
                        print 'key is used. type solve to get through the gate. also, pay a visit to bob. Ps- there is something fishy about the rootAI'
                        self.used = True
                else:
                        print 'key already used'

#IC challenge

class redDoor(AED):
    def __init__(self):
        AED.__init__(self,'RedDoor','A sign reads: Well done. Please advance as the recording instructs you. Caution: Danger of extremely painful injuries and/or death')
        self.done = False
    def execute(self):
        if self.done == True:
            return
        speech.say("Well done. We will now talk about the execute function. It is used to execute programs and similar objects. For this test, type exc and then the name of the executable node. You will find this node, or you will fail to leave the room.")
        self.done = True
    def color(self):
        return colored('RedDoor','red',attrs=['bold'])

class blueDoor(AED):
    def __init__(self):
        AED.__init__(self,'BlueDoor','A sign reads: You are obviously annoyingly incapable of much anything. Please step through the green door for vaporization.')
        self.done = False
    def execute(self):
        if self.done == True:
            return
        speech.say("Why are you doing that? ? ? ? You are absolutely useless! ! ! ! I tell you to go into the red door, and what do you do?? You go into the blue one! What is the whole point of telling you to do anything if you can't even do it! Anyway, now that your here, there is something kind of cool you might want to see. It's in the green door.")
        self.done = True
    def color(self):
        return colored('BlueDoor','blue',attrs=['bold'])

class greenDoor(AED):
    def __init__(self):
        AED.__init__(self,'GreenDoor','A sign reads: Why are you even reading this? Your about to be painfully vaporized and your busy reading road signs?  A second sign reads: Closed for maintenance')
        self.done = False
    def execute(self):
        if self.done == True:
            return
        speech.say("Just step foward a bit... oh. out of service. never mind. You should probably go. By the way, you didn't by any chance know what those signs said, did you? Good. That's very good. Anyway, don't like, try to find out later or anything. There isn't actually anything in this room, so go back to the red door.")
        self.done = True
    def color(self):
        return colored('GreenDoor','green',attrs=['bold'])

class yellowDoor(AED):
    def __init__(self):
        AED.__init__(self,'YellowDoor','A sign reads: Prepare for part 1B of 7...')
        self.done = False
    def execute(self):
        if self.done == True:
            return
        speech.say("Well done then. This is a nice door, isn't it? Anyway, prepare for part 1B of 7 in your introduction to the challenge. To enter it, just wait a second... In the meantime, the commands to take objects in your directory and use objects you have are take, and use. Simple. Standby...")
        self.done = True
        raise OSError
    def color(self):
        return colored('YellowDoor','yellow',attrs=['bold'])

#SEE challenge

class StarterTerrace(AED):
    def __init__(self):
        AED.__init__(self,"PathLedge",'Another platform of the stairway. Stairway continues.')
        self.done = False
    def execute(self):
        if self.done == True:
            return
        speech.say("Hello. This is the challenge initiation and new contestant package distribution program. As this suggests, you will now receive your new contestant package. You will find the new possessions in the chest.")
        self.done = True

class Notebook(obj):
        def __init__(self):
            obj.__init__(self,'notebook','A fallen plastic casing of a notebook...')
            self.taken = False
            self.contents = []
            self.total = []
        def use(self):
            while True:
                indexZ=0
                for line in self.contents:
                    indexZ+=1
                    print indexZ,'. ',line
                variable = raw_input(">/: ")
                if variable == '\n':
                    pass
                elif variable == 'del':
                    self.contents3 = []
                    indexer = 0
                    for line in self.contents:
                        indexer = indexer + 1
                        if indexer == len(self.contents):
                            pass
                        else:
                            self.contents3 += line
                    self.contents = self.contents3
                elif variable == 'edit':
                    self.contents2 = []
                    number = raw_input("pick a line to edit: ")
                    indexer2 = 0
                    for line in self.contents:
                        indexer2 = indexer + 1
                        if indexer2 == number:
                            lineThing = raw_input("enter a replacement: ")
                            self.contents2.append(lineThing)
                        else:
                            self.contents2.append(line)
                    self.contents = self.contents2
                elif variable == 'save':
                    self.contents.append(self.total)
                    self.contents = []
                elif variable == 'load':
                    index = 0
                    for item in self.total:
                        index += 1
                        print index, '. ', item[0]
                    thing = raw_input('Choose a note to edit(type a number): ')
                    index = 0
                    for item in self.total:
                        index += 1
                        if index == thing:
                            self.contents = item
                        else:
                            self.contents.append(variable)
