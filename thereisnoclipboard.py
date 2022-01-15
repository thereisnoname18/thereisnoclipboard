#Project to copy and paste multiple items(more information in help)
import keyboard as k   #for listening to keyboard activities and pressing keys
#suppress function does not work completely, therefore necessary adjustments were made
#due to this, the program will not run effectively on mac OS
import pyperclip       #for copying and pasting data from the system clipboard
import time      #for adding some neccessary delays(does not affect speed of program)
d = {}     #dictionary to store copied values
x = y = z = 1    #for making gates to prevent looping
d['copy'] = ''   #key for normal copy(ctrl+c)
a = '1234567890abcdefghijklmnopqrstuvwxyz'
ch,ph,xh = 'ctrl+c','ctrl+v','ctrl+x'   #default hotkeys
for i in a:  #ordinate method was not used as this is faster and an error occurs if hotkey is assigned to a special character
        d[i] = ''  #key for all other values
def copy(c):   #function to copy data(ctrl+c is not pressed as user presses it by default)
    d[c] = pyperclip.paste()  #to paste copied data into respective key
    pyperclip.copy('')  #this had to be done as suppress function does not work properly
    update(c)  #to change the copied data in the user interface
def special_copy(c):  #this is used when a non-default hotkey is used
                      #this was not added with copy() to increase the speed of copy()
    global y
    if y == 1:  #this prevents infinite looping(since ctrl+c is pressed inside the loop)
        y = 0
        k.press_and_release('ctrl+c')  #manual copy done as the user does not press ctrl+c while copying
        time.sleep(1)  #since pressing ctrl+c takes a small amount of time, program is slightly delayed
                       #however speed of the program is not affected to a large extent
        d[c] = pyperclip.paste()
    else:
        y = 1
    pyperclip.copy('')
    update(c)
def special_cut(c):  #this is used when a non-default hotkey is used
    global z
    if z == 1:  
        z = 0
        k.press_and_release('ctrl+x')  #manual cut done as the user does not press ctrl+x while cutting
        time.sleep(1)  #since pressing ctrl+x takes a small amount of time, program is slightly delayed
                       #however speed of the program is not affected
        d[c] = pyperclip.paste()
    else:
        z = 1
    pyperclip.copy('')
    update(c)
def paste(c):  #function to paste data
    pyperclip.copy(d[c]) #copies value from key and store in system clipboard
    global x
    if x == 1:  #similar gate as special_copy()
        x = 0
        k.press_and_release('ctrl+v')
        time.sleep(1)
        pyperclip.copy('')
    else:
        x = 1
    pyperclip.copy('')
def default_clip(): #this will be run when user doesnt change hotkeys
    global d,a
    k.add_hotkey('ctrl+c', copy, args = ['copy'], suppress = True, timeout = 10, trigger_on_release = True)
    k.add_hotkey('ctrl+x', copy, args = ['copy'], suppress = True, timeout = 10, trigger_on_release = True)
    k.add_hotkey('ctrl+v', paste, args = ['copy'], suppress = True, timeout = 10, trigger_on_release = True)
    #hotkeys for default copy and paste
    for i in a:  #copy hotkeys for all alphabets and numbers(symbols dont work)
        d[i] = ''  #for resetting to default values
        n = 'ctrl+c+'+i
        k.add_hotkey(n, copy, args = [i], suppress = True, timeout = 10, trigger_on_release = True)
        n = 'ctrl+v+'+i   #paste hotkeys for all alphabets and numbers
        k.add_hotkey(n, paste, args = [i], suppress = True, trigger_on_release = True)
        n = 'ctrl+x+'+i
        k.add_hotkey(n, copy, args = [i], suppress = True, timeout = 10, trigger_on_release = True)
def customized_clip():  #if user enters his own hotkeys
    global d,a,ch,ph
    k.add_hotkey('ctrl+c', copy, args = ['copy'], suppress = True, timeout = 10, trigger_on_release = True)
    k.add_hotkey('ctrl+x', copy, args = ['copy'], suppress = True, timeout = 10, trigger_on_release = True)
    k.add_hotkey('ctrl+v', paste, args = ['copy'], suppress = True, timeout = 10, trigger_on_release = True)
    for i in a:  #similar to default_clip()
        d[i] = ''
        n = ch+'+'+i
        k.add_hotkey(n, special_copy, args = [i], suppress = True, timeout = 10, trigger_on_release = True)
        n = ph+'+'+i
        k.add_hotkey(n, paste, args = [i], suppress = True, trigger_on_release = True)
        n = xh+'+'+i
        k.add_hotkey(n, special_cut, args = [i], suppress = True, timeout = 10, trigger_on_release = True)

import tkinter as tk  #for user interface
from tkinter import *
from tkinter import messagebox
win = Tk()
win['bg'] = 'black'
win.title("There Is No Clipboard")
win.iconphoto(True, tk.PhotoImage(file='/usr/bin/thereisnoclipboard/thereisnoclipboard_icon.png'))
win.geometry('900x800')
w = Label(win, text = "Welcome to There Is No Clipboard!",
          font = 40, bg = 'black', fg = 'green')
w.grid(column = 1)
w.config(font = ('Arial',20))
def check():  #to run the code when user presses activate button
    global ch,ph,xh
    if cb.get() == 1:
        if ch == 'ctrl+c' and ph == 'ctrl+v' and xh == 'ctrl+x':
            default_clip()
        else:  #to check if hotkey is entered by user
            customized_clip()
        btn['state'] = NORMAL
        btn.configure(text = 'ACTIVATED')
    elif cb.get() == 0:
        k.remove_all_hotkeys()
        btn['state'] = DISABLED
        btn.configure(text = 'DEACTIVATED')
    else:
        messagebox.showerror('UNKNOWN ERROR!')
def hotkey_set():  #to input hotkey from user
    global ch,ph,xh
    ch = cv.get()
    ph = pv.get()
    xh = xv.get()
    if ch == '':
        ch = 'ctrl+c'
    if ph == '':
        ph = 'ctrl+v'
    if xh == '':
        xh = 'ctrl+x'
    update_hotkey()
cb = IntVar()
b = Checkbutton(win, text = 'activate clipboard',  #button to activate script
                variable = cb, onvalue = 1,
                offvalue = 0, command = check,
                bg = 'black', fg = 'green').grid(row = 2, column = 1)
btn = Button(win, text = 'DEACTIVATED', state = DISABLED, bg = 'black', fg = 'green')
btn.grid(row = 3, column = 1)
cl = Label(win, text = "Hotkey for copy:", bg = 'black', fg = 'green')
cl.grid(row = 4, column = 0)
pl = Label(win, text = "Hotkey for paste:", bg = 'black', fg = 'green')
pl.grid(row = 5, column = 0)
xl = Label(win, text = "Hotkey for cut:", bg = 'black', fg = 'green')
xl.grid(row = 6, column = 0)
cv = tk.StringVar()
pv = tk.StringVar()
xv = tk.StringVar()
ce = Entry(win,textvariable = cv, bg = 'black', fg = 'green').grid(row = 4, column = 1)
pe = Entry(win,textvariable = pv, bg = 'black', fg = 'green').grid(row = 5, column = 1)
xe = Entry(win,textvariable = xv, bg = 'black', fg = 'green').grid(row = 6, column = 1)
sb = Button(win,text = 'Submit', command = hotkey_set,
            bg = 'black', fg = 'green').grid(row = 7, column = 1)
cch = Label(win, text = 'current hotkey for copy:', bg = 'black', fg = 'green')
cph = Label(win, text = 'current hotkey for paste:', bg = 'black', fg = 'green')
cxh = Label(win, text = 'current hotkey for cut:', bg = 'black', fg = 'green')
cch.grid(row = 4, column = 2)
cph.grid(row = 5, column = 2)
cxh.grid(row = 6, column = 2)
cchv = Label(win, text = ch, bg = 'black', fg = 'green')  
cphv = Label(win, text = ph, bg = 'black', fg = 'green')  #this shows user current hotkeys
cxhv = Label(win, text = xh, bg = 'black', fg = 'green')
cchv.grid(row = 4, column = 3)
cphv.grid(row = 5, column = 3)
cxhv.grid(row = 6, column = 3)
msg = '''Thank you for using the world's only super-lightweight,clipboard manager
that helps you to paste any copied item with a single keypress.'''
msg1 = 'How to use(it\'s very simple!!):\n\
1)Enter hotkey for copy and that for paste(default is ctrl+c and ctrl+v\
 respectively).\n\
  This will be the keys you will have to press in order to copy and paste.\n\
  Leave this space empty for using the default hotkeys\n\
2)Click on \'activate clipboard\' to activate the clipboard\n\
3)To copy or paste hold <command>+<key>,where <command> is the value you entered\
  for the hotkey and <key> is any alphabet or number(DO NOT use default hotkeys\
  like ctrl+c+q as the system will do the default function(ctrl+q,\
  this will quit the tab)after copying)\n\
  eg:ctrl+c+1 will copy your data in key <1>\n\
     ctrl+p+1 will paste this data\n\
     (while releasing keys, release p or c first and then release<key>)\n\
NOTES:\n\
1)You can still use your normal copy and paste(just ctrl+c or ctrl+v) while\
  the program is running\n\
2)DO NOT use any of the systems default hotkeys or symbols(except ctrl+c and ctrl+v)\
  for copy and pasting hotkeys as they may cause some errors\n\
3)To change the hotkeys, deactivate the code, add the hotkeys and then activate it\
  again\n\
4)To quit the code, close the main window and press "esc"'

def instructions():  #to setup a help window
    global msg,msg1
    hwin = Tk()
    hwin['bg'] = 'black'
    hwin.title("Help")
    hwin.geometry('750x750')
    hw = Label(hwin, text = "Welcome to Help!", bg = 'black', fg = 'green')
    hw.place(x = 225,y = 50)
    hw.config(font = ('Arial',20))
    mmsg = Message(hwin, text = msg, bg = 'black', fg = 'green')
    mmsg.place(x = 30,y = 100)
    mmsg.config(font = ('Times New Roman',15))
    mmsg1 = Message(hwin, text = msg1, bg = 'black', fg = 'green')
    mmsg1.place(x = 30,y = 300)
    mmsg1.config(font = ('Times New Roman',15))
btn2 = Button(win,text = 'HELP', command = instructions,
            bg = 'black', fg = 'green').grid(row = 1, column = 2)
d2 = {} 
d3 = {} #these dictionaries are used to show the copied data to user
q = 9
for i in a[:18]:  #since 1 single row was too long, it has been split into 2
    t = i+':'
    d2[i] = Message(win, text = t, bg = 'black', fg = 'green')
    d2[i].grid(row = q, column = 0)
    d3[i] = Message(win, text = d[i], bg = 'black', fg = 'green')
    d3[i].grid(row = q, column = 1)
    q+= 1
q = 9
for i in a[18:]:
    t = i+':'+d[i]
    d2[i] = Message(win, text = t, bg = 'black', fg = 'green')
    d2[i].grid(row = q, column = 2)
    d3[i] = Message(win, text = d[i], bg = 'black', fg = 'green')
    d3[i].grid(row = q, column = 3)
    q+= 1
def update(c): #to change the value shown to user whenever new data is copied
    global d
    try:
        d3[c].config(text = d[c])  #to prevent showing value for ctrl+c
                                       #symmetry is broken if ctrl +c is shown
    except:
        pass
def update_hotkey(): #to change hotkey value
    global ch,ph
    cchv.config(text = ch)
    cphv.config(text = ph)
    cxhv.config(text = xh)
win.mainloop()
 