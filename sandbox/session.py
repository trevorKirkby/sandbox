#to do next: goto/cat . fixup, tab and up arrow completions, mark command, and insult expansions, and add to autoprint so you may specify modifier if you dont want fully automatized

from termcolor import colored, cprint

class Session:
    def __init__(self,fs,name,home):
        self.fs = fs
        self.name = name
        self.home = home
        self.pwd = home
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
                # Prompt the user for a new command
                #cprint(self.pwd.name, 'yellow', attrs=['bold'])
                print colored(self.home.name, "green", attrs=['bold','dark','underline']),
                print colored(self.pwd.name, "yellow", attrs=['bold']),
                cmdline = raw_input(prompt)
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
                pass
    # command handlers go here
    def exit_builtin(self,argv):
        print 'exit'
        raise SystemExit

    def pwd_builtin(self,argv):
        print self.pwd.abspath()

    # Emulate the behavior of /bin/ls with no options
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
                if node.isDir():
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
            # Print dir contents in alphabetical order
            for childname in sorted(dirs[name].children.iterkeys()):
                    print ('%-16s' % childname),
            print

    def whoami_builtin(self,argv):
        cprint('Seriously???', 'yellow', 'on_yellow', attrs=['bold','dark','underline'])

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
                realFile = False
                for name in self.pwd.children:
                    if name == argv[1]:
                        try:
                            if self.pwd.children[name].isFile == True:
                                print self.pwd.children[name].contents
                                realFile = True
                        except:
                            realFile = None
                if realFile == False:
                    print self.name, ": cat:", argv[1], ": No such file or directory"
                if realFile == None:
                    print self.name, ": cat:", argv[1], ": Is a directory"

    def look_builtin(self,argv):    
        print self.pwd.look

    def find_builtin(self,argv):
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
                                passing = self.pwd.children[name].execute()
                                #true means you advance to directory, false means your booted back to homedir, none means nothing happens
                                if passing == True:
                                    self.pwd = self.pwd.children[name]
                                if passing == False:
                                    self.pwd = self.home
                                if passing == None:
                                    pass
                                realProg = True
                        else:
                            realProg = None
                if realProg == False:
                    print self.name, ": exc:", argv[1], ": No such file or directory"
                if realProg == None:
                    print self.name, ": exc:", argv[1], ": Not a program"
