import sandbox.filesystem as fs
import sandbox.session as se
import sandbox.executables as ex
import sandbox.galartheor as gp
import sandbox.speech as sp
import random
import tty
import termios
import sys

from sandbox.termcolor import cprint, colored
#border
import time

root = fs.Filesystem('This is the root directory of your challenge introduction capsule.')

paths = root.mkdir('Paths','This is the central area to the capsule')

homeA = paths.mkdir('PreparationCapsuleHomeSectionA',"A sign reads: Well done. It seems you have found out how to look. It really is an invaluable life skill, isn't it.")

redDoor = fs.redDoor()
homeA.add(redDoor)

forkA = redDoor.mkdir('forkA',"Empty steel room. A sign reads: sorry, you got the pathway wrong. You could get there by methodically starting at the start, but not as quickly as if you took a logical guess. Too bad, isn't it.")

forkB = redDoor.mkdir('forkB',"Empty steel room. A sign reads: Well done. You sucessfully navigated a difficult labrynth. All other barriers in the actual challenge should now pose no threat to you. Seriously, great job.")

testEx = ex.ExecutePath()
forkB.add(testEx)

forkC = redDoor.mkdir('forkC',"Empty steel room. A sign reads: sorry, you got the pathway wrong. The logic that it would be the last one is faulty. Too bad, isn't it.")

blueDoor = fs.blueDoor()
homeA.add(blueDoor)

greenDoor = fs.greenDoor()
blueDoor.add(greenDoor)





print ' ' + ' ' + ' '
print 'bash: error: tellnet_deamon: Greetings...'
print ' ' + ' ' + ' '
try:
    time.sleep(2)
except:
    pass
print 'system restart...'
print ' '
try:
    time.sleep(2)
except:
    pass
print 'actually, nah. Lets not restart. ^C!'
try:
    time.sleep(2)
except:
    pass
print ' '
print 'bash: error: automatic node fsck failed'
try:
    time.sleep(2)
except:
    pass
print 'Error No. [7]: failure to node fsck: run manual fsck'
try:
    time.sleep(2)
except:
    pass
print ' '
print 'root login...    [', colored('Error','red',attrs=['bold','dark']),']'
try:
    time.sleep(2)
except:
    pass
print ' '
print "Error: System Failure: Wow! System Failure. That sounds fun!"
try:
    time.sleep(2)
except:
    pass
print ' '

for number in range(500):
    variable = random.choice(range(10))
    if variable == 0:
        print 'network config--     [', colored('System_Error','red',attrs=['bold']), ']                                             ',
    if variable == 1:
        print 'HaHa!---', colored('System_Error','red',attrs=['bold']), ']',
    if variable == 2:
        print '010100001010101010101010111111000000101000000000',
    if variable == 3:
        print 'root--fsck--tellnet',
    if variable == 4:
        print '[', colored('System_Error','red',attrs=['bold']), ']',
    if variable == 5:
        print colored('hello!','red','on_white',attrs=['dark','underline']),
    if variable == 6:
        print 'Error No. [ 3486738475[2081 ]: ERROR',
    if variable == 7:
        print colored('    ---SEE---    ','grey',attrs=['bold','underline']),
    if variable == 8:
        print '                                  fish'
    if variable == 9:
        try:
            time.sleep(0.5)
        except:
            pass

sp.say("Hello. If you are any bit more perceptive than you probably are or than the last bunch was, you may have noticed that the system has been hacked.")
try:
    sp.say("Do you understand? : ",enter=False)
    fd = sys.stdin.fileno()
    oldSet = termios.tcgetattr(fd)
    tty.setraw(sys.stdin)
    time.sleep(6)
    termios.tcsetattr(fd, termios.TCSADRAIN, oldSet)
except:
    pass
try:
    sp.say("Well? Are you going to answer? Oh whatever. Anyway... By the way, you don't look so great. It could be a side effect of the system hacking stuff and all, hold on...")
    time.sleep(float(0.1))
    sp.say("Oh. Whoops.")
    time.sleep(float(0.1))
    sp.say("That's the way you actually normally look. Anyway. You want to finish the challenge, right? So, 'the challenge', something people have been tasked to for a while now I guess, is simple. We want you to go into this system, and retreive several invaluable codes for us. If you do what we say, your reward will be a twenty five cent gift card to your nearest coffe shop, so huzzah for that. Anyway, it's my job to make sure that your somewhat prepared. Well, ok, I won't lie, it's actually my job to make sure you don't make too much of a mess in the entryway. But yes, you are supposed to do some practice. The system is a little different than one you might be used to. It has a lot of useful stuff that you probably take for granted in a typical system, with restrictions and new names. To begin your testing, advance through the red door. To do this, type vw to veiw the list of nodes, and gt to go a directory.")
except:
    pass

test = se.Session(root,'capsule',homeA)
test.shell('-:#`/>: ')
