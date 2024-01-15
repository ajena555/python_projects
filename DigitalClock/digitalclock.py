from tkinter import *
import time

window=Tk()
window.title('Digital Clock')
l1=Label(window, text='00:00:00', font='Ivy 80 bold')
l1.pack()

def update_clock():
    h=time.strftime('%I')
    m=time.strftime('%M')
    s=time.strftime('%S')
    am_pm=time.strftime('%p')
    time_now=h+':'+m+':'+s+':'+am_pm
    l1.config(text=time_now)
    l1.after(1000, update_clock)

update_clock()

window.mainloop()
