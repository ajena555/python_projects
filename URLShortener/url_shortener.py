from tkinter import *
import pyshorteners

window = Tk()
window.geometry('400x180')
window.title('URL Shortener')

col1 = 'red'
col2 = 'black'
col3 = 'white'

frame_line = Frame(window, width=500, height=5, bg=col1)
frame_line.grid(row=0, column=0)

frame_body = Frame(window, width=500, height=200, bg=col3)
frame_body.grid(row=1, column=0)

label1 = Label(frame_body, width=15, height=1, text='Enter the url - ', bg=col3, font='Ivy 12')
label1.place(x=20, y=20)

label2 = Label(frame_body, width=15, height=1, text='Shortened url - ', bg=col3, font='Ivy 12')
label2.place(x=20, y=100)

entry1 = Entry(frame_body, width=40)
entry1.place(x=150, y=22)

entry2 = Entry(frame_body, width=40)
entry2.place(x=150, y=102)


def shortener():
    url = entry1.get()
    s = pyshorteners.Shortener()
    shortened_url = s.tinyurl.short(url)
    entry2.delete(0, END)
    entry2.insert(0, shortened_url)


b = Button(frame_body, width=8, height=1, text='Generate', bg=col3, font='Ariel 12', command=shortener)
b.place(x=130, y=58)

window.mainloop()






