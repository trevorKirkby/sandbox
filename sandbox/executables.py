import filesystem as fs
import insult
import time

class program(fs.Node):
        def __init__(self,name):
                fs.Node.__init__(self,name)
        def isDir(self):
                return False
        def isExc(self):
                return True


class path(fs.Directory):
        def __init__(self,name,look):
                fs.Directory.__init__(self,name,look)
                self.children = { }
                self.passing = None
                self.isProg = True
        def isDir(self):
                return False
        def isExc(self):
                return True


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
                for word in variable:
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
