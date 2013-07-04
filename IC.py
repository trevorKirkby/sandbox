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

try:
        time.sleep(15)
except:
        try:
                time.sleep(15)
        except:
                try:
                        time.sleep(15)
                except:
                        try:
                                time.sleep(15)
                        except:
                                try:
                                        time.sleep(15)
                                except:
                                        try:
                                                time.sleep(15)
                                        except:
                                                print "Well. You are persistant, aren't you."

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
    if True:
        print 'initialize: systemerror--   [', colored('fatal','red',attrs=['bold']), ']'
        try:
                time.sleep(10)
        except KeyboardInterrupt:
                pass
        print 'Broadcast from "DIE ANNOYING HUMAN":\n\n\nYou only delayed the inevitable. You will go back now...\n\n\n'
        try:
                time.sleep(2)
        except KeyboardInterrupt:
                pass
        print "You don't stand a chance. People have been trying for years. And this is just the beginning. I'm going to activate it now.\n\n\n"
        try:
                time.sleep(10)
        except KeyboardInterrupt:
                pass
        print 'sudo password: '
        print "Errno [7] : possiblely fatal remotehost connection"
        print 'source: error: no such file or directory ".bashrc"'
        print 'reverting to basic terminal'
        thing = raw_input('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n</root: ')
        thing = raw_input('\n</root: ')
        thing = raw_input('\n</root: ')
        thing = raw_input('\n</root: ')
        thing = raw_input('\n</root: ')
        ex.systchaos()
        sp.say("Hello. You should realize that your system has been compromised. That was not fun when you got rid of this program earlier. But anyway... Back to your introduction. Big huge challenge, many people failed, fabulous prizes of twenty five cent starbucks giftcards, yadda yadda ya. ")
        try:
            sp.say("So are you onboard with that and all? : ",enter=False)
            time.sleep(6)
        except:
            pass
        try:
            sp.say("Oh yeah. You don't know how to speak yet. Anyway... Your still not looking so great, by the way, so I guess you actually do look like that normally. Ah well.")
            time.sleep(float(0.1))
            sp.say("So.")
            time.sleep(float(0.1))
            sp.say("Your back into the introductory bit of the challenge, so go through the red door. By the way, you are challenged to find out every possible peice of information from this introduction. If you do, you will be entered into a lottery to win an extra half-a-cent value on your gift card! (if you even win). So don't make to much of a mess, as well. Proceed.")
        except:
            pass
    return root

if os.path.isfile('/home/pi/sandbox/.ic.pkl'):
        print 'loading previous system...'
        root = sandbox.save.load()
else:
        fd = sys.stdin.fileno()
        oldSet = termios.tcgetattr(fd)
        print '\n'
        root = createSyst()

try:
        termios.tcsetattr(fd, termios.TCSADRAIN, oldSet)
        test = se.Session(root,'capsule',(root.children['Paths']).children['PreparationCapsuleHomeSectionA'])
        test.shell('-:#`/>: ')
except SystemExit:
        if TEST == False:
            sandbox.save.save(root)
        else:
            reset = raw_input('save or reset? S/r : ')
            if reset == 'r':
                print 'fine. just delete the file .ic, cuz i wont do it for you.'
            else:
                sandbox.save.save(root)
except OSError:
        sbox.run()
#weakness=^Z, aliases for fg!!!!
