import sandbox.filesystem as fs
import sandbox.session


rootdir = fs.Filesystem()

users = rootdir.mkdir('users')

trevor = users.mkdir('trevor')
desktop = trevor.mkdir('desktop')

filething = fs.File('file.txt','blub blub im a fish')
desktop.add(filething)

a = fs.File('a.txt','The quick brown fox...')
trevor.add(a)

b = fs.File('b.txt','...jumped over the lazy dog')
trevor.add(b)

ryan = users.mkdir('ryan')

c = fs.File('c.txt','Here I am!')
ryan.add(c)

s = sandbox.session.Session(rootdir,'mash',trevor)
s.shell('> ')
