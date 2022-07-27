import socket
from threading import Threading
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

PORT = 3027
IP_ADDRESS = "127.0.0.1"
SERVER = None
BUFFER_SIZE = 4096

window=Tk()
window.title('Music Window')
window.geometry("300x300")
window.configure(bg='LightSkyBlue')

def MusicWindow():
    selectlabel = Label(Window, text="Select Song", bg='LightSkyBlue', font=('Calibri',8))
    selectlabel.place(x=2, y=1)

    listbox = Listbox(window, height=10, width=39, activestyle='dotbox', bg='LightSkyBlue', borderwidth=2, font=('Calibri', 10))
    listbox.place(x=10, y=10)

    scrollbar1 = Scrollbar(listbox)
    scrollbar1.place(relheight=1, relx=1)
    scrollbar1.config(commnd=listbox.yview)

    playButton= Button(window, text="play", width=10, bg='SkyBlue', font=('calibri',10))
    playButton.place(x=30, y=200)

    Stop= Button(window, text="Stop", width=10, bg='SkyBlue', font=('calibri',10))
    Stop.place(x=200, y=200)

    Upload= Button(window, text="Upload", width=10, bg='SkyBlue', font=('calibri',10))
    Upload.place(x=30, y=250)

    Download= Button(window, text="play", width=10, bg='SkyBlue', font=('calibri',10))
    Download.place(x=200, y=250)

    infoLabel = Label(window, text="", fg="blue", font=("Calibri", 8))
    infoLabel.Place(x=4, y=280)

    window.mainloop()