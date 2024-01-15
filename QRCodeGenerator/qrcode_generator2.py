from tkinter import *
import qrcode

window = Tk()
window.title('QRCode Generator')
window.geometry('400x180')

col1 = 'white'
col2 = 'red'


frame_line = Frame(window, width=400, height=6, bg=col2)
frame_line.grid(row=0, column=0)

frame_body = Frame(window, width=400, height=200, bg=col1)
frame_body.grid(row=1, column=0)

label1 = Label(frame_body, width=15, height=1, bg=col1, font='Ivy 12', text='Enter the text')
label1.place(x=30, y=30)

label2 = Label(frame_body, width=15, height=1, bg=col1, font='Ivy 12', text='QR Code name')
label2.place(x=30, y=70)

entry1 = Entry(frame_body, width=40, bg=col1, font='Ivy 8')
entry1.place(x=150, y=30)

entry2 = Entry(frame_body, width=35, bg=col1, font='Ivy 8')
entry2.place(x=158, y=70)

entry3 = Entry(frame_body, width=40, bg=col1, font='Ivy 8')
entry3.place(x=90, y=140)

def qrcodegenertor():
    url = entry1.get()
    img = qrcode.make(url)
    save = entry2.get()
    img.save(save)
    entry3.delete(0, END)
    entry3.insert(0, 'QR code is generated and saved in the file.')


b = Button(frame_body, width=8, height=1, text='Generate', command=qrcodegenertor)
b.place(x=150, y=100)

window.mainloop()