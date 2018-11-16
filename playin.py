# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 17:41:18 2018

@author: hillg2
"""
# This is for GUI stuff and making sure it works
import tkinter
#m=tkinter.Tk()
#m.title('Counting')
#button = tkinter.Button(m, text='Stop', width=25, command=m.destroy) 
#button.pack() 
#m.mainloop()

usernameButton = tkinter.Tk()
tkinter.Label(usernameButton, text='Username').grid(row = 0, column = 0) 

e1 = tkinter.Entry(usernameButton)
e1.grid(row = 0, column = 1)

def callback():
    print (e1.get())
    
def send():

    b = tkinter.Button(usernameButton, text="Send", width=10, command=callback)
    b.grid(row = 0, column = 2 )
    usernameButton.mainloop()
    s = e1.get()
    print(s)

send()