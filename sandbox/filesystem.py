class Node:
    def __init__(self,name):
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
        
class File(Node):
    def __init__(self,name,contents=None):
        Node.__init__(self,name)
        self.isFile = True
        self.contents = contents
    def isDir(self):
        return False

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
    # Makes and returns an empty subdirectory
    def mkdir(self,name,look):
        return self.add(Directory(name,look))
    def isDir(self):
        return True
'''
class Program(File):
    #acess progName = prog.execute(self)
    def __init__(self,name,contents):
        File.__init__(self,name)
        self.contents = contents
        self.isProg = True
    def execute(self):
        for line in self.contents:
            exec line
        return None
class Path(Directory):
    def __init__(self,name,choiceList,failureChoiceList,look,loopBool):
        Directory.__init__(self,name,look)
        self.children = { }
        self.choiceList = choiceList
        self.failureChoiceList = failureChoiceList
        self.passing = True
        self.isProg = True
        self.loop = loopBool
    # Add a File or Directory to our contents
    def add(self,node):
        node.parent = self
        self.children.append(node)
        return node
    # Returns our absolute path as a string
    def abspath(self):
        path = [ self.name ]
        node = self
        while node.parent:
            node = node.parent
            path.insert(0,node.name)
        return '/'.join(path)
    def execute(self):
        for item in self.choiceList:
            exec item
            #program can make passing false if you get it's requirements wrong
        if self.passing == False:
            for item in self.failureChoiceList:
                exec item
            if self.loop == True:
                return False
            else:
                return None
        if self.passing == True:
            return True
    def isDir(self):
        return False
'''
class Filesystem(Directory):
    def __init__(self,look):
        Directory.__init__(self,'',look)

class World(Directory):
    def __init__(self,name,look):
        Directory.__init__(self,name,look)
