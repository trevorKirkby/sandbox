import sandbox.filesystem as fs
import sandbox.session as se
import sandbox.executables as ex
import sandbox.galartheor as gp
import sandbox.speech as sp
import sandbox.save
import random
import tty
import termios
import sys
import os
import sbox

from sandbox.termcolor import cprint, colored
#border
import time

TEST = False

def createSyst():
    root = fs.Filesystem('This is the root directory of your challenge introduction capsule.')
    
    paths = root.mkdir('Paths','This is the central area to the capsule','r')
    
    homeA = paths.mkdir('PreparationCapsuleHomeSectionA',"A sign reads: Well done. It seems you have found out how to look. It really is an invaluable life skill, isn't it.")
    
    redDoor = fs.redDoor()
    homeA.add(redDoor)
    
    forkA = redDoor.mkdir('forkA',"Empty steel room. A sign reads: sorry, you got the pathway wrong. You could get there by methodically starting at the start, but not as quickly as if you took a    logical guess. Too bad, isn't it.")
    
    forkB = redDoor.mkdir('forkB',"Empty steel room. A sign reads: Well done. You sucessfully navigated a difficult labrynth. All other barriers in the actual challenge should now pose no threat to you. Seriously, great job.")

    testEx = ex.ExecutePath()
    forkB.add(testEx)

    testEx2 = ex.ExecutePath2()
    testEx.add(testEx2)

    filething = fs.File('file','use the decode command to examine anything fishy...')
    testEx2.add(filething)

    passage = fs.hiddenDir('secretPassage','A sign reads: well done. You have demonstated massive skills of perception in deciding to decode this program. The real challenge should be really, really easy for you.','program37')
    testEx2.add(passage)

    next = fs.yellowDoor()
    passage.add(next)

    progA = ex.prog1()
    testEx2.add(progA)

    progB = ex.prog2()
    testEx2.add(progB)

    progC = ex.prog3()
    testEx2.add(progC)

    progD = ex.prog4()
    testEx2.add(progD)

    progE = ex.prog5()
    testEx2.add(progE)

    progF = ex.prog6()
    testEx2.add(progF)

    progG = ex.prog7()
    testEx2.add(progG)
    
    forkC = redDoor.mkdir('forkC',"Empty steel room. A sign reads: sorry, you got the pathway wrong. The logic that it would be the last one is faulty. Too bad, isn't it.")

    blueDoor = fs.blueDoor()
    homeA.add(blueDoor)

    greenDoor = fs.greenDoor()
    blueDoor.add(greenDoor)
    #
    if TEST == False:
        print '\n' + '\n' + '\n'
        print 'bash: error: tellnet_deamon: Greetings...'
        print ' '
        print ' '
        print ' '
        try:
            time.sleep(2)
        except:
            pass
        print 'system restart...'
        print '\n'
        try:
            time.sleep(2)
        except:
            pass
        print 'actually, nah. Lets not restart. ^C!'
        try:
            time.sleep(2)
        except:
            pass
        print '\n\n\n'
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
        for number in range(700):
            variable = random.choice(range(20))
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
            if variable == 10:
                try:
                    time.sleep(1)
                except:
                    pass
            if variable == 11:
                sp.say('HAHAHA','happy')
            if variable == 12:
                print '--SEE SEE SEE SEE SEE SEE SEE SEE--'
            if variable == 13:
                print "help! Whatever you do, beware the sparrows, count the shadows, and don't trust the sentinel. I can't tell you more about the rest, but you'll know what I mean when the time comes!"
            if variable == 14:
                print colored(random.choice(range(300)),'magenta','on_cyan')
            if variable == 15:
                print 'the answer is time_the answer is time_the answer is time_the answer is time_the answer is time_the answer is time_the answer is time_the answer is time_the answer is time_the answer is time_the answer is time_the answer is time_the answer is time_the answer is time_the answer is time_the answer is time_the answer is time_the answer is time_the answer is time_the answer is time_the answer is time_the answer is time_the answer is time_the answer is time_the answer is time_the answer is time_the answer is time_the answer is time'
            if variable == 16:
                print 'BLUB BLUB BLUB'
            if variable == 17:
                print 'SNAP SNAP SNAP'
            if variable == 18:
                print 'rivers; data, night, styx, lethe! Great Spire! Abyss! Galartheor!'
            if variable == 19:
                print "I don't know where I am!"
        print '\n'
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
            sp.say("That's the way you actually normally look. Anyway. You want to finish the challenge, right? So, 'the challenge', something people have been tasked to for a while now I guess, is simple. We want you to go into this system, and retreive several invaluable codes for us. If you do what we say, your reward will be a twenty five cent gift card to your nearest coffe shop, so huzzah for that. Anyway, it's my job to make sure that your somewhat prepared. Well, ok, I won't lie, it's actually my job to make sure you don't make too much of a mess in the entryway. But yes, you are supposed to do some practice. The system is a little different than one you might be used to. It has a lot of useful stuff that you probably take for granted in a typical system, with restrictions and new names. To begin your testing, advance through the red door. To do this, type ls to veiw the list of directory children, and cd to go a directory.")
        except:
            pass
    return root

if os.path.isfile('/home/pi/sandbox/.ic.pkl'):
        print 'loading previous system...'
        root = sandbox.save.load()
else:
        print 'Traceback (Most recent call last): file <.bashrc> : you are doomed'
        root = createSyst()

try:
        test = se.Session(root,'capsule',(root.children['Paths']).children['PreparationCapsuleHomeSectionA'])
        test.shell('-:#`/>: ')
except OSError:
        sbox.run()
except SystemExit:
        if TEST == False:
            sandbox.save.save(root)
        else:
            reset = raw_input('save or reset? S/r : ')
            if reset == 'r':
                print 'fine. just delete the file .ic, cuz i wont do it for you.'
            else:
                sandbox.save.save(root)
#weakness=^Z, aliases for fg!!!! hahah
