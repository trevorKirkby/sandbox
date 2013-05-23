import sandbox.filesystem as fs
import sandbox.session


rootdir = fs.Filesystem()

users = fs.Directory('users')
rootdir.add(users)

trevor = fs.Directory('trevor')
users.add(trevor)

desktop = fs.Directory('desktop')
trevor.add(desktop)

filething = fs.File('file.txt','blub blub im a fish')
desktop.add(filething)

a = fs.File('a.txt','The quick brown fox...')
trevor.add(a)

b = fs.File('b.txt','...jumped over the lazy dog')
trevor.add(b)

ryan = fs.Directory('ryan')
users.add(ryan)

c = fs.File('c.txt','Here I am!')
ryan.add(c)


s = sandbox.session.Session(rootdir,'mash',trevor)
s.shell('> ')
