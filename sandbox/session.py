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