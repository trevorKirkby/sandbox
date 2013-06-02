#to do before challenge construct: clean up speech, make hidden dir class, and make permissions

class Node:
    def __init__(self,name):
        #you could shift a node by changing its parent, even across trees, just with a different 'directory'. why cant you do the same to a session's pwd?
        self.name = name
        self.parent = None
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
        
class File(Node):
    def __init__(self,name,contents=" "):
        Node.__init__(self,name)
        self.contents = contents
    def isFile(self):
        return True

class obj(Node):
    def __init__(self,name,contents=" "):
        Node.__init__(self,name)
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
    def __init__(self,name,look):
        Node.__init__(self,name)
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
    def mkdir(self,name,look):
        return self.add(Directory(name,look))
    def isDir(self):
        return True

class Filesystem(Directory):
    def __init__(self,look):
        Directory.__init__(self,'',look)

class World(Directory):
    def __init__(self,name,look):
        Directory.__init__(self,name,look)



#objects below:


class key(obj):
        def __init__(self):
                obj.__init__(self,'key','A key shaped depression in the chest bottom...')
                self.used = False
                self.taken = False
        def use(self):
                if self.taken == True and self.used == False:
                        print 'key is used. type solve to get through the gate. also, pay a visit to bob.'
                        self.used = True
                else:
                        print 'key already used'
