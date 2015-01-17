import sandbox.filesystem as fs
import sandbox.session as se
import sandbox.executables as ex
import sandbox.galartheor as gp
from sandbox.termcolor import colored, cprint


SEE = fs.SuperRoot('SEE',"If you are reading this, you somehow gained entry to this directory, which would be cheating. Well done. Anyway, leave, and don't come back please. Hacking is frowned upon in most societies.")




PathSpire = SEE.mkdir('PathSpire',"The large stone spire that marks the entry to SEE. It also serves other purposes in this system... Miles down the foot of the spire fades into the clouds. Miles above the top fades into the clouds. There is a baroque, embellished stone doorway, a painted white steel doorway, a sketch looking bridge suspended along the side of the spire face, and a carved stone stairway leading down. The area has been described and all that. Good luck with the whole challenge, you will undoubtedly require it.")


ShadeLibrary = SEE.mkdir('ShadeLibrary',"This is an ornate, dimly lit library. You should leave...")


VisitorRoom = SEE.mkdir('VisitorRoom',"'Welcome to the S.E.E. visitor's room! This is a semi-experimental simulation of a semi-real institute via complex semi-electronics that you probably wouldn't understand and that will not be explained anyway. If you are disatisfied in any way with the services of S.E.E, or if you feel that we have posed you any kind of misfortune, get over it! We really don't care. Anyway, try not to make to much of a mess in here, because its supposed to look somewhat respectable and I think the cleaning program died a few weeks ago. Sincerely, S.E.E. welcoming algorithm.'  Large portable. Old desks with a few papers. Lots of broken down printers and computers. Reception desk with a loudspeaker welded onto it. One computer with a flickering screen thrown into the corner. Old wooden door labeled shade library, steel tunnel with railings and path to path spire, grassy trail leading into the distance blocked off by a large iron gate, a steel vault door labelled 'employees only', and a old wooden door labelled 'the road of redundance'.")


HillsofSparrows = SEE.mkdir('HillsOfTheSparrows',"A sprawling area of hills covered in vegetation and several buildings. The buildings are vaguely oriental. You can tell with your incredible skills of deduction that nothing is wrong here and you aren't about to be murdered.")


Docks = SEE.mkdir('Docks',"A small docks and town at the side of albatross lake. In the center, an island is visible through the fog. Blub blub blub I am a fish. Remember this above all else.")


AlbatrossLake = SEE.mkdir('AlbatrossLake',"A majestic lake blanketed in fog, with an island in the center. The island is fabled to contain the abondoned nest of an albatross hidden in it.")


GatewayRepublic = SEE.mkdir('GatewayRepublic',"A curious area filled with artificial intelligence possessing doors. These doors have formed their own sophisticated government, building a prosperous country. The area is rumored to have suffered some recent catastrophes recently, but the doors are still a proud rebuplic.")


SignStone = SEE.mkdir('SignStone',"Somewhere nearby, there is an engraved stone placed to mark an electronic center of order. Even though order in the system collapses, this is still a constant location.")


SecretiveSalamander = SEE.mkdir('AmphibiousForge',"SNAP... Snap... Snap.. snap... snap.......snap................")


BarrowOfTrensildor = SEE.mkdir('BarrowOfTrensildor',"A massive stone monolith full of large spire monuments... and maybe some rogue basilisks who want to eat you.")


RealmOfTheRadioActiveRodents = SEE.mkdir('DangerRadioactivity',"A sign reads: Warning. The indigenous population are highly radioactive.")


CrypticGoose = SEE.mkdir('FowlCrypt',"Nah, you don't get a description this time. Work it out. Explore.")


EmployeesOnly = SEE.mkdir('EmployeesOnly',"A light up sign flashes 'WELCOME!' and there are rows upon rows of broken down electronics. In the back a damaged looking automaton is talking to itself.")


ScorchedStandardValley = SEE.mkdir('ScorchedValley',"Below lies a huge valley full of swirling snow and fog. In the distance a damaged looking camp lies at the center of the valley. Looks super mysterious and all that.")


RiverNight = SEE.mkdir('RiverNight',"This is the river of night. If you don't know what that is you'll find out pretty soon. Or not, depending on whether we lowered our requisite intelligence for the challenge again.")


HouseOfInsults = SEE.mkdir('HouseOfRubberBands',"You'll have to work out the reason for the name to get an easter egg here... It may make sense eventually, just think about the prevalent force in this 'house'. Speaking of that, you are no longer on the river of night, as you got somewhat sidetracked... You moron.")



#PATH SPIRE

BaroqueStair = PathSpire.mkdir('BaroqueDoor','A spiral staircase winds upwards and all, theres nothing really to see. It would be advisable to continue.')
CarvedStair = PathSpire.mkdir('CarvedStairwayDown','A stairway made of stone leads down. Fog surrounds you, and the environment is very dramatic and all that.')
VisitorPath = PathSpire.mkdir('SteelDoor',"A clean, white painted plastic and steel room somewhere inside the path spire. A sign reads: Welcome to the path spire! Proceed to the visitor's room or visit the steel nest. If your doing that, your going the wrong way.")
SketchBridge = ex.BridgeToTerrace()
PathSpire.add(SketchBridge)

#PATH SPIRE--BAROQUE STAIR

StepA = BaroqueStair.mkdir('StoneStep','Everything but the steps in front and behind you fade into fog. Basically, I refuse to tell you anything about your surroundings for now. In this challenge I totally dont have to you know. From, -FISH')
StepB = StepA.mkdir('StoneStep','Everything but the steps in front and behind you fade into fog. I continue to not tell you anything. From, -FISH')
StepC = StepB.mkdir('StoneStep','Everything but the steps in front and behind you fade into fog. I continue to continue to not tell you anything. From, -FISH')
StepD = StepC.mkdir('StoneStep','Everything but the steps in front and behind you fade into fog. Basically, still nothing at all visible, so there. I will not tell you anything. I am keeping you utterly in the dark. How do you like that? From, -FISH')
StepE = StepD.mkdir('StoneStep','Good news: There is now something to see. The face of a large and delapidated office building is barely visible in the distance. Nearby, an embellished statue of a fish is labelled "blub blub blub"...')
StepF = StepE.mkdir('StoneStep','A flash of silver can be seen higher up on an overhang, so yeah. Anyway, how is the challenge going? I imagine it is extremely chaotic.')
StepG = StepF.mkdir('StoneStep',"You know you don't usually think of the mechanics of going up a stair, step by step, but it actually takes kind of a while, doesn't it? Plus even one step is a complex thing and all that. Point being, brace yourself for a long trip up this spiral staircase...")
StepH = StepG.mkdir('StoneStep',"Lots of fog, not a lot to see really.")
StepI = StepH.mkdir('StoneStep',"Still lots of fog. Exciting, isn't it.")
StepJ = StepI.mkdir('StoneStep',colored('Very foggy. Your surroundings are completely white.','white',attrs=['bold','underline']))
StepK = StepJ.mkdir('StoneStep',"A lemur gargoyle statue is suspended on a rope over your head. Don't ask me why, I don't know either.")
StepL = StepK.mkdir('StoneStep',"Graffiti etches on the steps depict a clock strapped to a huge computer with lots of wires leading from it. The computer has an eye drawn into it's screen. There is also an elephant carrying a flagpole. Probably deeply symbolic etchings of a long lost civilization. You nerd.")
StepM = StepL.mkdir('StoneStep',"Foggy again. Sorry.")
StepN = StepM.mkdir('StoneStep',"Well, not so foggy. You can see a few steps ahead of you.")
StepO = StepN.mkdir('StoneStep',"You can see stuff. You know you should really count how many steps there are. It is a common base number for you. (think mathematically)")
StepP = StepO.mkdir('StoneStep',"A largish body of water with an island in the middle is barely visible.")
StepQ = StepP.mkdir('StoneStep',"A largish sloth can be seen hanging from a huge tree far off in the distance.")
StepR = StepQ.mkdir('StoneStep',"The walls get progressively wetter as you procceed up, due to elevation and due to dew. Get it? Due to dew? Ha ha ha.")
StepS = StepR.mkdir('StoneStep',"A shrub is growing in the side of the spire. Kind of weird that this is the only shrub here...")
StepT = StepS.mkdir('StoneStep',"Foggy again. Oh boy.")
StepU = StepT.mkdir('StoneStep',"This step is of mild importance.")
StepV = StepU.mkdir('StoneStep',"Still foggy. Weird shapes are visible in the fog. Probably hallucinations.")
StepW = StepV.mkdir('StoneStep',"Another flash of steel is visible not too far up. Probably important.")
StepX = StepW.mkdir('StoneStep',"CALAMARI")
StepY = StepX.mkdir('StoneStep',"FUNGUS")
StepZ = StepY.mkdir('StoneStep',"You can now see a small platform, followed by a switchback ramp. A small wooden gateway blocks you.")
FinalStep = ex.QuestionGateSteelbirdNest()
StepZ.add(FinalStep)
Platform2 = FinalStep.mkdir("RampEntrance","The first turnaround of the switchback. You can now see the spiral staircase below you. So no fog and all that right now.")
Platform3 = Platform2.mkdir("continuation","Two paths branch off, one is blocked by a gateway. One leads up.")

#PLATFORM 3
Platform4 = Platform3.mkdir("Ramp","Hello, this is a challenge help sign. Here is the advice: try not to lose... Such good advice might give you an unfair advantage so I will be sure to put something unpleasant in your future.")
SilverGate = ex.silvergate()
Platform3.add(SilverGate)

#PLATFORM 4
noobPkg = fs.StarterTerrace()
Platform4.add(noobPkg)

#STARTER TERRACE
Chest2 = ex.chest2()
noobPkg.add(Chest2)
Stairway = noobPkg.mkdir('Stairway','You are on a stairway upward and all... ... ... ... ...What else do you even want to know? ...  ... There is not anything else! You can go now! ... ... LEAVE! Bye.')

#CHEST 2
notes = fs.Notebook()
Chest2.add(notes)

#STAIRWAY
overlook = Stairway.mkdir('overlook','Impressive veiw, yadda yadda yah. Large monument made of darkened stone, large, elaborately carved, flat building, and a river visible in the distance.')
nextstep = Stairway.mkdir('nextStep','Ahead you can see a fork')

#cs = challenge session
CS = se.Session(SEE,'mash',PathSpire)
CS.shell('/$: ')
