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

class LDirectory(Directory):
#locked directory, ls disabled
    def __init__(self,name,look):
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
        return False

class Filesystem(Directory):
    def __init__(self,look):
        Directory.__init__(self,'',look)

class World(Directory):
    def __init__(self,name,look):
        Directory.__init__(self,name,look)
