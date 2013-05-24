import sandbox.filesystem as fs
import sandbox.session


rootdir = fs.Filesystem('this is rootDir. Cool command isnt it?')

users = rootdir.mkdir('users','user folder, two doors, yadda yadda ya...')

trevor = users.mkdir('trevor','welcome to your home directory. This is a sandbox simulation and all that.')
desktop = trevor.mkdir('desktop','this is a desktop folder. Theres not a lot in it is there?')

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
