from pygame import mixer
from tkinter import *

root = Tk()
file = ('C:\\Users\\kevsi\\Desktop\\gamedir\\musdir\\ost\\1.mp3')
mixer.init()
mixer.music.load(file)
mixer.music.play()
root.mainloop()
