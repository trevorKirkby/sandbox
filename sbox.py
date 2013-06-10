import sandbox.filesystem as fs
import sandbox.session
import sandbox.executables as ex
import sandbox.galartheor as gp
import sandbox.save
import os

TEST = False

def createSyst():
        rootdir = fs.Filesystem('this is rootDir. Cool command isnt it?')
        restrict = rootdir.mkdir('restricted','how the heck did you get in here???',' ')
        users = rootdir.mkdir('users','user folder, two doors, yadda yadda ya...')
        dog = ex.rootAI()
        rootdir.add(dog)
        demo = gp.samplePrinter()
        rootdir.add(demo)
        passage = fs.hiddenDir('secretPassage','a mysterious secret passage with big, secret stuff inside...','rootAI')
        labrador = fs.File('puzzlePeice.txt','You will use your other peices in the desktop...')
        passage.add(labrador)
        rootdir.add(passage)
        trevor = users.mkdir('trevor','welcome to your home directory. This is a sandbox simulation and all that.')
        desktop = trevor.mkdir('desktop','this is a desktop folder. Theres not a lot in it is there?')
        passage2 = fs.hiddenDir('secretPassageTwo','A sign reads: Wow! You have totally shattered all of our expectations. Actually, you actually might have. Chances are we have very little faith in you, and probably for good reason.','5279')
        thingamobob = ex.win()
        passage2.add(thingamabob)
        desktop.add(passage2)
        #talker = gp.program()
        #trevor.add(talker)
        gate = ex.gateway()
        trevor.add(gate)
        poodle = fs.File('puzzlePeice.txt','Your going to need to use the decode command on the numbers you found. The other peices show the keyword number, and directory you type the number.')
        gate.add(poodle)
        filething = fs.File('file.txt','blub blub im a fish')
        desktop.add(filething)
        test = ex.bob()
        desktop.add(test)
        a = fs.File('a.txt','The quick brown fox...')
        trevor.add(a)
        b = fs.File('b.txt','...jumped over the lazy dog')
        trevor.add(b)
        ryan = users.mkdir('ryan','blank')
        c = fs.File('c.txt','Here I am!')
        ryan.add(c)
        woodenChest = ex.chest()
        ryan.add(woodenChest)
        dog = fs.File('puzzlePeice.txt','Two digits of the code you need are five and seven')
        woodenChest.add(dog)
        keyObject = fs.key()
        woodenChest.add(keyObject)
        return rootdir

def run():
        if os.path.isfile('/home/pi/sandbox/.system.pkl'):
                print 'loading previous system...'
                rootdir = sandbox.save.load()
        else:
                print 'creating new system...'
                rootdir = createSyst()

        try:
                s = sandbox.session.Session(rootdir,'mash',(rootdir.children['users']).children['trevor'])
                s.shell('/$: ')
        except SystemExit:
                if TEST == True:
                        sandbox.save.save(rootdir)
                else:
                        print 'Resetting...'
                        os.remove('/home/pi/sandbox/.system.pkl')
