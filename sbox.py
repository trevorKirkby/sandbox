import sandbox.filesystem as fs
import sandbox.session

sbox = fs.Filesystem()

users = fs.Directory('users')
sbox.add(users)

trevor = fs.Directory('trevor')
users.add(trevor)
a = fs.File('a.txt','The quick brown fox...')
trevor.add(a)
b = fs.File('b.txt','...jumped over the lazy dog')
trevor.add(b)

ryan = fs.Directory('ryan')
users.add(ryan)
c = fs.File('c.txt','Here I am!')
ryan.add(c)

s = sandbox.session.Session(sbox,'mash',trevor)
s.shell('> ')
