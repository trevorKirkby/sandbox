class Session:
    def __init__(self,fs,name,home):
        self.fs = fs
        self.name = name
        self.home = home
        self.pwd = home
    # here we emulate a shell session
    def shell(self,prompt):
        while True:
            try:
                # Prompt the user for a new command
                cmdline = raw_input(self.pwd.name + prompt)
                # Break the command line into an argv list
                argv = cmdline.split()
                if len(argv) == 0:
                    continue
                # Look for a handler that matches argv[0]
                handler = getattr(self,argv[0]+'_handler',None)
                if handler:
                    handler(argv)
                else:
                    print '%s: %s: command not found.' % (self.name,argv[0])
            except KeyboardInterrupt:
                print
            except EOFError:
                pass
    # command handlers go here
    def exit_handler(self,argv):
        print 'exit'
        raise SystemExit

    def pwd_handler(self,argv):
        print '/'.join(self.pwd.abspath())

    def ls_handler(self,argv):
        for name in self.pwd.children:
            print ('%-16s' % name),
        print

    def whoami_handler(self,argv):
        print 'seriously??'

    def goto_handler(self,argv):
        #if there is no second argument go home like in cd
        if len(argv) == 1:
            self.pwd = home
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

    def cat_handler(self,argv):
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
    def look_handler(self,argv):    
        print self.pwd.look
