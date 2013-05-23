class File:
    def __init__(self,name,contents=None):
        self.name = name
        self.contents = contents

class Directory:
    def __init__(self,name):
        self.name = name
        self.parent = None
        self.children = [ ]
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

class Filesystem(Directory):
    def __init__(self):
        Directory.__init__(self,'')
