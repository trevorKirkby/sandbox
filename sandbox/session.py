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
                cmdline = raw_input(prompt)
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
    # command handlers go here
    def exit_handler(self,argv):
        print 'exit'
        raise SystemExit

    def pwd_handler(self,argv):
        print '/'.join(self.pwd.abspath())

    def ls_handler(self,argv):
        for child in self.pwd.children:
            print ('%-16s' % child.name),
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
                for item in self.pwd.children:
                    if item.name == argv[1]:
                        self.pwd = item
                        realDirectory = True
                if realDirectory == False:
                    print self.name, ": goto:", argv[1], "no such file or directory"
