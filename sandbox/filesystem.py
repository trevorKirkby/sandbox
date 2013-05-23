class Node:
    def __init__(self,name):
        self.name = name
        self.parent = None
    # Returns the absolute path of this node as a list node names
    def abspath(self):
        path = [ self.name ]
        node = self
        while node.parent:
            node = node.parent
            path.insert(0,node.name)
        return path
        
class File(Node):
    def __init__(self,name,contents=None):
        Node.__init__(self,name)
        self.isFile = True
        self.contents = contents
    def isDir(self):
        return False

class Directory(Node):
    def __init__(self,name):
        Node.__init__(self,name)
        self.children = { }
        self.look = 'nothing'
    # Add a generic node
    def add(self,node):
        node.parent = self
        self.children[node.name] = node
        return node
    # Makes and returns an empty subdirectory
    def mkdir(self,name):
        return self.add(Directory(name))
    def isDir(self):
        return True

class Program:
    #acess progName = prog.execute(self)
    def __init__(self,name,contents):
        self.name = name
        self.contents = contents
    def execute(self):
        exec contents
    def isDir(self):
        return False

class Path:
    def __init__(self,name,choiceList,failureChoiceList):
        self.name = name
        self.parent = None
        self.children = [ ]
        self.choiceList = choiceList
        self.failureChoiceList = failureChoiceList
        self.passing = True
    # Add a File or Directory to our contents
    def add(self,node):
        node.parent = self
        self.children.append(node)
    # Returns a list of the directory names in our absolute path
    def abspath(self):
        path = [ self.name ]
        node = self
        while node.parent:
            node = node.parent
            path.insert(0,node.name)
        return path
    def execute(self):
        for item in self.choiceList:
            exec item
            #program can make passing false if you get it's requirements wrong
        if passing == False:
            for item in self.failureChoiceList:
                exec item
                #these end in pwd = worldRoot
        if passing == True:
            pass
            #pwd = self
    def isDir(self):
        return False

class Filesystem(Directory):
    def __init__(self):
        Directory.__init__(self,'')

class World(Directory):
    def __init__(self,name):
        Directory.__init__(self,name)
