import sandbox.filesystem as fs
import sandbox.session as se
import sandbox.executables as ex
import sandbox.galartheor as gp


SEE = fs.SuperRoot('SEE',"If you are reading this, you somehow gained entry to this directory, which would be cheating. Which is really, not cool. Anyway, leave, and don't come back please.")




PathSpire = SEE.mkdir('Path Spire',"The large stone spire that marks the entry to SEE. It also serves other purposes in this system...")


ShadeLibrary = SEE.mkdir('Shade Library',"This is an ornate, dimly lit library. Count the name...")


VisitorRoom = SEE.mkdir('Visitor Room',"'Welcome to the S.E.E. visitor's room! This is a semi-experimental simulation of a semi-real institute via complex electronics that you probably wouldn't understand and that will not be explained. If you are disatisfied in any way with the services of S.E.E, get over it! We really don't care. Anyway, try not to make to much of a mess in here, because its supposed to look somewhat clean. Sincerely, S.E.E. welcoming program.'  Large portable type room. Old desks with a few papers. Lots of broken down printers and computers. Reception desk with a loudspeaker welded onto it. One computer with a flickering screen thrown into the corner. Old wooden door labeled shade library, steel tunnel with railings and path to path spire, grassy trail leading into the distance blocked off by a large iron gate, a steel vault door labelled employees only, and a old wooden door labelled the road of redundance.")


HillsofSparrows = SEE.mkdir('Hills of the Sparrows',"A sprawling area of hills covered in vegetation and several buildings. The buildings are vaguely oriental")




#cs = challenge session
CS = se.Session(SEE,'mash',PathSpire)
CS.shell('/$: ')
