#to do next: cat . fixup, tab completions, mark command, insult expansions, and make mkdir methods for multiple node types, and and basic conversational modules added to programs and basic sandbox in sandbox method for paths and ask() and reply() functions and progMove functions and progMovePlayer functions and progcolor/speech functions and non gprog general personality and feelings Stores and make largescale directory functions to create an entire tree in one functioncall and make globbing and make a door function that prestructures a program already so all it needs is basic response to circumstance feilds filled in, and basic modifiers like code included or question or key required included or persuasion required, and a random choice from a small number of basic configurations and order of typed responses to appear normal, and make a similar preset for moving 'people', for stationary personality terminals, for stationary tool terminals, for animation programs(part of upper categories), and add cart and items variables, and add inGameEasterEgg variables, and add outOfGameEasterEggRepositories, and add base skelaton mainfraims for guiding gprogs and imag+text puzzles withpoint and click and features for detterents and penalties such as prisons, decodings, and sendbacks wrapped up in callable functions, and make adition to program in progress logical boundaries to prevent unraveling of hallenge by user past building of it, and finnally make a secret testing and way past end easter egg capsule with window travel everywhere, cool terminals, further locked testing equipment used by builder of prog with this as home dir, and various challenge plot location insertions, as well as themeduseful stuff for a secret program operative abse etc, and finnally fix up those for loop stuffs with text.split in the insult module.
#also make a 'spellcheck' in commands, that will autocorrect commands after you press enter, counting on the fact that there are only ten commands anyhow
#new node-- pertaining to hidden stuff--print colored(('%-16s' % childname),'grey',attrs=['bold']),
#color coding: obj: cyan  hiddenDoor: bold grey
#sometime rename exc to ac, for access, and polish up error messages...

import readline

from termcolor import colored, cprint

import speech

testMode = False

class Session:
    def __init__(self,fs,name,home,mini=False):
        self.mini = mini
        self.fs = fs
        self.name = name
        self.home = home
        self.pwd = home
        self.own = []
        self.testMode = testMode
    # expands the specified list of paths by replacing any leading ~
    def expand(self,paths):
        expanded = [ ]
        for path in paths:
            if path == '~':
                expanded.append(self.home.abspath())
            elif path.startswith('~'):
                expanded.append(self.home.abspath() + '/' + path[1:])
            else:
                expanded.append(path)
        return expanded
    # returns the node corresponding to the specified path or raises a RuntimeError
    def find(self,path,debug=False):
        # split the path into names separated by '/'
        names = path.split('/')
        if debug: print 'find %r' % names
        # decide which node the path starts from...
        if names[0] == '':
            node = self.fs
            names.pop(0)
        elif names[0] == '~':
            node = self.home
            names.pop(0)
        else:
            node = self.pwd
        if debug: print 'find starting from "%s"' % node.name
        # follow the path
        while names:
            name = names.pop(0)
            if name == '.' or name == '':
                pass
            elif name == '..':
                if node == self.fs:
                    pass
                else:
                    node = node.parent
            elif hasattr(node,'children') and name in node.children:
                node = node.children[name]
            else:
                raise RuntimeError('%s: No such file or directory.' % path)
            if debug: print 'find "%s" => "%s"' % (name,node.name)
        return node
        
    # here we emulate a shell session
    def shell(self,prompt):
        while True:
            try:
                # Prompt the user for a new command. Non-printing characters mess up readline
                # unless they are delimted with \001...\002. For details, see:
                # http://stackoverflow.com/questions/9468435/look-how-to-fix-column-calculation-in-python-readline-if-use-color-prompt
                # bracketing color control sequences should work but doesn't seem to. The problem can
                # be reproduced using raw_input('\001\002> ')
                thisprompt = (
                    '\001' +
                    colored('\002'+self.home.name+'\001', "green", attrs=['bold','dark','underline'])
                    + '\002 \001' +
                    colored('\002'+self.pwd.name+'\001', "yellow", attrs=['bold'])
                    + '\002'+ prompt)
                cmdline = raw_input(thisprompt)
                # Break the command line into an argv list
                argv = cmdline.split()
                if len(argv) == 0:
                    continue
                # Expand the command line
                argv = self.expand(argv)
                # Look for a builtin handler that matches argv[0]
                handler = getattr(self,argv[0]+'_builtin',None)
                if handler:
                    handler(argv)
                else:
                    print '%s: %s: command not found.' % (self.name,argv[0])
            except KeyboardInterrupt:
                print
            except EOFError:
                print ' '
                print self.name, ': EOF Error'
    # command handlers go here
    def leave_builtin(self,argv):
        print 'leaving...'
        raise SystemExit

    def pwd_builtin(self,argv):
        #tie to test mode
        print self.pwd.abspath()

    # Emulate the behavior of /bin/ls with no options
    # add restrictions on ls dirname as opposed to ls . regainable via an in game easter egg thing...
    def ls_builtin(self,argv):
        # Default argument is '.'
        if len(argv) == 1:
            argv.append('.')
        # Loop over the arguments and separate them into dirs and files
        dirs = { }
        files = { }
        for name in argv[1:]:
            try:
                node = self.find(name)
                if node.read == False:
                    print self.name, ": vw: According to the challenge, you don't have permissions to do that here. You don't have read permissions on this node, which includes ls."
                    return
                if node.isDir():
                    dirs[name] = node
                elif node.isGate():
                    dirs[name] = node
                else:
                    files[name] = node
            except RuntimeError,error:
                print '%s: %s' % (argv[0],str(error))
        # List files in alphabetical order
        for name in sorted(files.iterkeys()):
            print ('%-16s' % name),
        # Blank line to separate files and dirs
        if len(files) > 0: print
        if len(files) > 0 and len(dirs) > 0: print
        # List dirs in alphabetical order
        firstdir = True
        for name in sorted(dirs.iterkeys()):
            if not firstdir: print
            firstdir = False
            # Print dir name if we got more than 1 arg
            if len(argv) > 2:
                print '%s:' % name
            # Print dir contents in alphabetical order, where it gets colors
            for childname in sorted(dirs[name].children.iterkeys()):
                    node = dirs[name].children[childname]
                    if node.color() == None:
                        if node.isDir() == True:
                            if node.isPassage() == True:
                                print colored(('%-16s' % childname),'grey',attrs=['bold']),
                            elif node.isPassage() == None:
                                pass
                            else:
                                print colored(('%-16s' % childname),'blue',attrs=['bold']),
                        elif node.isFile() == True:
                            print ('%-16s' % childname),
                        elif node.isExc() == True:
                            if node.isGate() == True:
                                if node.isHold() == True:
                                    print colored(('%-16s' % childname),'yellow',attrs=['bold']),
                                else:
                                    print colored(('%-16s' % childname),'magenta',attrs=['bold']),
                            else:
                                if node.isPerson() == True:
                                    print colored(('%-16s' % childname),'white',attrs=['bold']),
                                else:
                                    print colored(('%-16s' % childname),'green',attrs=['bold']),
                        elif node.isObj() == True:
                            print colored(('%-16s' % childname),'cyan',attrs=['bold']),
                        else:
                            print colored(('%-16s' % childname+'--None'),'red',attrs=['bold']),
                    else:
                        try:
                            print node.color(),
                        except:
                            print 'mash: vw: colored name error'
                            raise KeyboardInterrupt
            print

    def whoami_builtin(self,argv):
        cprint('Seriously???', 'yellow', 'on_yellow', attrs=['bold','dark','underline'])
        print 'cd-- like normal system cd  ls-- like normal system ls but with no -a/l argv modifiers and new color coding  cat-- shows text in read permission granted files  whoami-- comments on that question  pwd-- prints current directory, might be disabled for most of challenge  find-- lets you find stuff will definetely be disabled in challenge but useful sandbox command  man-- tells you about commands  exc-- executes an executable  take-- takes an object, which later may be used  nodes-- simplified ls for testing purposes, as it has no restrictions and has a -l operand  use-- lets you use an object if you own it  decode-- with a modifier pertaining to something in the current directory, able to reveal hidden things...'

    def cd_builtin(self,argv):
        #if there is no second argument go home
        if len(argv) == 1:
            self.pwd = self.home
        # otherwise, use the second arg and ignore any extra ones
        else:
            try:
                node = self.find(argv[1])
                if not node.isDir():
                    print '%s: %s: %s: Not a directory' % (self.name,argv[0],argv[1])
                elif node.isPassage == None:
                    print '%s: %s: %s: Not a directory' % (self.name,argv[0],argv[1])
                else:
                    if node.execute2 == False:
                        print self.name, ": cd: You do not have execute permissions to cd into this directory."
                    else:
                        if node.isAutoExc():
                            node.execute()
                        self.pwd = node
            except RuntimeError,e:
                print '%s: %s: %s' % (self.name,argv[0],str(e))

    def goto_builtin(self,argv):
        #if there is no second argument go home like in cd
        if len(argv) == 1:
            self.pwd = self.home
        #if argument number two is .. go to your current directory's parent directory
        else:
            if argv[1] == '..':
                #if there is no parent directory just do nothing
                if self.pwd.parent != None:
                    self.pwd = self.pwd.parent
                else:
                    pass
            #if none of the above is triggered looks through your directory's children and if they match argument two you are taken to that directory
            else:
                realDirectory = False
                for name in self.pwd.children:
                    if name == argv[1]:
                        if self.pwd.children[name].isDir() == True:
                            self.pwd = self.pwd.children[name]
                            realDirectory = True
                        else:
                            realDirectory = None
                if realDirectory == False:
                    print self.name, ": goto:", argv[1], ": No such file or directory"
                if realDirectory == None:
                    print self.name, ": goto:", argv[1], ": Not a directory"

    def cat_builtin(self,argv):
        #if there is no second argument refer to man page
        if len(argv) == 1:
            print self.name, ": cat:", "Missing operand"
            print "Try 'cat --help' for more information"
        else:
            if argv[1] == '--help':
                print "No! You don't get help. This is a challenge. Work it out. Meow."
            else:
                try:
                    node = self.find(argv[1])
                    if node.read == False:
                        print self.name, ': cat:', argv[1], ': You are not granted read permissions on this node.'
                    if node.isFile():
                        print node.contents
                    if node.isDir():
                        print self.name, ": cat:", argv[1], ": Is a directory"
                    if node.isExc():
                        print self.name, ": cat:", argv[1], ": Is an executable"
                except RuntimeError,e:
                    print '%s: %s: %s' % (self.name,argv[0],str(e))

    def look_builtin(self,argv):
        if self.pwd.read == False:
            print self.name, ': look: Your current directory does not have read permissions'    
        print self.pwd.look
#sometime, you should meld look and cat, as they do about the same thing, just one for files and one for dirs.

    def find_builtin(self,argv):
        #tie to test mode
        for path in argv[1:]:
            try:
                self.find(path,debug=True)
            except RuntimeError,e:
                print str(e)

    def man_builtin(self,argv):
        print "The man pages are down. Sorry for the inconvenience and all that. They're not likely to be back up any time soon."

    def exc_builtin(self,argv):
        if len(argv) == 1:
            print self.name, ": exc: seriously???? All you have to do is type exc then an executable file! no python this, no bash this, just exc than program! Sheesh!"
        else:
            if argv[1] == '--help':
                print "No! You don't get help. This is a challenge. Work it out. Get it right or this program will exc you."
            else:
                realProg = False
                for name in self.pwd.children:
                    if name == argv[1]:
                        if self.pwd.children[name].isExc() == True:
                            if True:
                                if self.pwd.children[name].execute2 == False:
                                    print self.name, ': exc: You do not have execute permissions for this node'
                                    return
                                passing = self.pwd.children[name].execute()
                                #true means you advance to directory, false means your booted back to homedir, none means nothing happens
                                if passing == True:
                                    self.pwd = self.pwd.children[name]
                                if passing == False:
                                    self.pwd = self.home
                                if passing == None:
                                    pass
                                if self.mini == True and passing == 'end':
                                    raise SystemExit
                                realProg = True
                        else:
                            realProg = None
                if realProg == False:
                    print self.name, ": exc:", argv[1], ": No such file or directory"
                if realProg == None:
                    print self.name, ": exc:", argv[1], ": Not a program"

    def take_builtin(self,argv):
        if len(argv) == 1:
            print self.name, ": take: specify and object... sheesh."
        else:
            if argv[1] == '--help':
                print "Nope! You don't get help, so work it out okay?"
            elif argv[1] == '.' or argv[1] == '..':
                print self.name, ': take: Is a directory. You should really know better.'
            else:
                try:
                    node = self.find(argv[1])
                    if node.isObj():
                        self.own.append(node)
                        node.taken = True
                    if node.execute2 == False:
                        print self.name, ': take: You do not have execute permissions on this node, which includes "take"'
                        return
                except RuntimeError,e:
                    print '%s: %s: %s' % (self.name,argv[0],str(e))
    def nodes_builtin(self,argv):
        #tells you all nodes on self.pwd without any restrictions(for example permissions), color coding, or fancy touches. Useful for testing, link to test mode variable later
        for child in self.pwd.children:
            node = self.find(child)
            if len(argv) > 1:
                if argv[1] == '-l':
                    text = str('%-16s'%child+'%-16s'%('r:'+str(node.read))+'%-16s'%('w:'+str(node.write))+'%-16s'%('x:'+str(node.execute2)))
                elif argv[1] == '-a':
                    text = child
                else:
                    print self.name, ': nodes:', argv[1], ': No such operand'
                    return
            else:
                text = child
            print colored((text),'white',attrs=['bold'])
    def use_builtin(self,argv):
        if len(argv) == 1:
            print self.name, ": use: specify an object... sheesh."
        else:
            if argv[1] == '--help':
                print "No help allowed. What word about challenge don't you understand? Theres only even one word, so that's pretty sad."
            else:
                find = False
                for thing in self.own:
                    if thing.name == argv[1]:
                        if thing.execute2 == True:
                            thing.use()
                        else:
                            print self.name, ': use: This object does not give you executables permissions'
                            return
                        find = True
                if find == False:
                    print self.name, ": use: You don't even have an object called", argv[1], "! Get it togethor! You clearly can't use something you don't own!"
    def decode_builtin(self,argv):
        #below is a auto-decode code for testing purposes
        if len(argv) == 1:
            print self.name, ": decode: specify a keyword... sheesh."
        elif argv[1] == '--help':
            print "No help allowed. Super sorry... If you beleive that not receiving any help is somehow unfair, please lodge a complaint with SEE..."
        elif argv[1] == '-all':
            for child in self.pwd.children:
                node = self.find(child)
                if node.isPassage() == None:
                    node.found = True
        else:
            for child in self.pwd.children:
                node = self.find(child)
                if node.isPassage() == None:
                    if argv[1] == node.key:
                        node.found = True
