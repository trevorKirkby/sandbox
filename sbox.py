import sandbox.filesystem as fs
import sandbox.session
import sandbox.executables as ex
import sandbox.galartheor as gp

rootdir = fs.Filesystem('this is rootDir. Cool command isnt it?')

users = rootdir.mkdir('users','user folder, two doors, yadda yadda ya...')
dog = ex.rootAI()
rootdir.add(dog)
demo = gp.samplePrinter()
rootdir.add(demo)

trevor = users.mkdir('trevor','welcome to your home directory. This is a sandbox simulation and all that.')
desktop = trevor.mkdir('desktop','this is a desktop folder. Theres not a lot in it is there?')
#talker = gp.program()
#trevor.add(talker)

gate = ex.gateway()
trevor.add(gate)

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
s.shell('/$: ')
