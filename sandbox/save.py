import pickle
import os

def save(root):
    filename = open('/home/pi/sandbox/.system.pkl','w+')
    pickle.dump(root,filename)
def load():
    filename = open('/home/pi/sandbox/.system.pkl','r')
    return pickle.load(filename)

def save2(home):
    filename = open('/home/pi/sandbox/.systHome.pkl','w+')
    pickle.dump(home,filename)
def load2():
    filename = open('/home/pi/sandbox/.systHome.pkl','r')
    return pickle.load(filename)
