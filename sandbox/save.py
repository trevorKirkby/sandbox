import pickle
import os

def save(root):
    filename = open('/home/pi/sandbox/.system.pkl','w+')
    pickle.dump(root,filename)
def load():
    filename = open('/home/pi/sandbox/.system.pkl','r')
    return pickle.load(filename)
