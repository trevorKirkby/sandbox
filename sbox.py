import sandbox.filesystem as fs
import sandbox.session


rootdir = fs.Filesystem('this is rootDir. Cool command isnt it?')

users = rootdir.mkdir('users','user folder, two doors, yadda yadda ya...')

trevor = users.mkdir('trevor','welcome to your home directory. This is a sandbox simulation and all that.')
desktop = trevor.mkdir('desktop','this is a desktop folder. Theres not a lot in it is there?')

gateway = fs.Path('gateway',['print "hello"','thingvariable=raw_input("to a frequency of theta thought devided alpha beta absurd and dissonant are its cries, yet convincing when it lies, rarely at the fore of mind, shows you what you couldnt find, only of panic to memory can bind, and without one is less kind. What am I?: ")','if thingvariable != "solve": self.passing = False','if thingvariable == "solve": self.passing = True','print self.passing'],['print "you lose!"','print "no entry!"'],'nothing. you solved it for nothing. so there. haha!',True)
trevor.add(gateway)

filething = fs.File('file.txt','blub blub im a fish')
desktop.add(filething)

a = fs.File('a.txt','The quick brown fox...')
trevor.add(a)

b = fs.File('b.txt','...jumped over the lazy dog')
trevor.add(b)

ryan = users.mkdir('ryan','blank')

c = fs.File('c.txt','Here I am!')
ryan.add(c)

s = sandbox.session.Session(rootdir,'mash',trevor)
s.shell('> ')
