import math
from tkinter import *
import time

window=Tk()
window.title('Analog Clock')
window.geometry('400x400')

def update_clock():
    h=int(time.strftime('%H'))
    m=int(time.strftime('%M'))
    s=int(time.strftime('%S'))

    sec_x = s_hand_len * math.sin(math.radians(s*6))+center_x
    sec_y = -1 * s_hand_len * math.cos(math.radians(s*6))+center_y

    canvas.coords(s_hand,center_x,center_y,sec_x,sec_y)

    min_x = m_hand_len * math.sin(math.radians(m * 6)) + center_x
    min_y = -1 * m_hand_len * math.cos(math.radians(m * 6)) + center_y

    canvas.coords(m_hand, center_x, center_y, min_x, min_y)

    hour_x = h_hand_len * math.sin(math.radians(h * 30)) + center_x
    hour_y = -1 * h_hand_len * math.cos(math.radians(h * 30)) + center_y

    canvas.coords(h_hand, center_x, center_y, hour_x, hour_y)

    window.after(1000, update_clock)



canvas=Canvas(window, width=400, height=400, bg='black')
canvas.pack(expand=True, fill='both')

bg=PhotoImage(file='dial_400.png')
canvas.create_image(200,200,image=bg)

center_x=200
center_y=200
s_hand_len=95
m_hand_len=80
h_hand_len=60

s_hand=canvas.create_line(200,200,200+s_hand_len,200+s_hand_len,width=1.5,fill='red')
m_hand=canvas.create_line(200,200,200+m_hand_len,200+m_hand_len,width=2,fill='white')
h_hand=canvas.create_line(200,200,200+h_hand_len,200+h_hand_len,width=4,fill='white')

update_clock()
window.mainloop()