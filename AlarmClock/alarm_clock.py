from tkinter.ttk import *
from tkinter import *
from PIL import Image, ImageTk
from pygame import mixer
import datetime
from time import sleep
from threading import Thread


bg_color = '#ffffff'
col1 = 'red'
col2 = 'black'

window = Tk()
window.geometry("350x150")
window.title("")
window.config(bg=bg_color)

frame_line = Frame(window, width=400, height=5, bg=col1)
frame_line.grid(row=0, column=0)

frame_body = Frame(window, width=400, height=300, bg=bg_color)
frame_body.grid(row=1, column=0)

img = Image.open('icon.png')
img.resize((100, 100))
img = ImageTk.PhotoImage(img)

app_img = Label(frame_body, height=100, image=img, bg=bg_color)
app_img.place(x=15, y=15)

name = Label(frame_body, text='Alarm', height=1, font=('Ivy 18 bold'), bg=bg_color)
name.place(x=130, y=15)

hour = Label(frame_body, text='hour', height=1, font=('Ivy 10 bold'), bg=bg_color, fg=col2)
hour.place(x=130, y=45)

c_hour = Combobox(frame_body, width=2, font=('ariel 15'))
c_hour.place(x=130, y=65)
c_hour['values'] = ('00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12')
c_hour.current(0)


min = Label(frame_body, text='min', height=1, font=('Ivy 10 bold'), bg=bg_color, fg=col2)
min.place(x=180, y=45)

c_min = Combobox(frame_body, width=2, font=('ariel 15'))
c_min.place(x=180, y=65)
c_min['values'] = ('00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15',
                    '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32',
                    '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49',
                    '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60')
c_min.current(0)

sec = Label(frame_body, text='sec', height=1, font=('Ivy 10 bold'), bg=bg_color, fg=col2)
sec.place(x=230, y=45)

c_sec = Combobox(frame_body, width=2, font=('ariel 15'))
c_sec.place(x=230, y=65)
c_sec['values'] = ('00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15',
                    '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32',
                    '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49',
                    '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60')
c_sec.current(0)

period = Label(frame_body, text='period', height=1, font=('Ivy 10 bold'), bg=bg_color, fg=col2)
period.place(x=280, y=45)

c_period = Combobox(frame_body, width=3, font=('ariel 15'))
c_period.place(x=280, y=65)
c_period['values'] = ('AM', 'PM')
c_period.current(0)

def activate_alarm():
    t = Thread(target=alarm)
    t.start()

def deactivate_alarm():
    print('deactivating the alarm..', selected.get())
    mixer.music.stop()

selected = IntVar()

radbtn1 = Radiobutton(frame_body, text='Activate', value=1, bg=bg_color, command=activate_alarm, variable=selected)
radbtn1.place(x=130, y=100)


def sound_alarm():
    mixer.music.load('clock.mp3.wav')
    mixer.music.play()
    selected.set(0)

    radbtn2 = Radiobutton(frame_body, text='Deactivate', value=2, bg=bg_color, command=deactivate_alarm, variable=selected)
    radbtn2.place(x=200, y=100)

def alarm():
    while True:
        control = selected.get()
        print(control)
        now = datetime.datetime.now()
        hour = now.strftime('%H')
        minute = now.strftime('%M')
        second = now.strftime('%S')
        period = now.strftime('%p')
        alarm_hour = c_hour.get()
        alarm_minute = c_min.get()
        alarm_second = c_sec.get()
        alarm_period = c_period.get()
        alarm_period = str(alarm_period).upper()

        if control == 1:
            if alarm_period == period:
                if alarm_hour == hour:
                    if alarm_minute == minute:
                        if alarm_second == second:
                            sound_alarm()
        sleep(1)



mixer.init()

window.mainloop()


