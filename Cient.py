import socket
from threading import Thread
from tkinter import *
from tkinter import ttk
import ftplib
import os
import time
import ntpath #This is used to extract filename from path

from tkinter import filedialog
from pathlib import Path


from playsound import playsound
import pygame
from pygame import mixer


SERVER = None
PORT = 8050
IP_ADDRESS = "127.0.0.1"
BUFFER_SIZE=4096
SONG_COUNTER=0
SONG_SELECTED=""

def setup():
    global SERVER
    global PORT
    global IP_ADDRESS
    global SONG_COUNTER


    socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS,PORT))
    musicScreen()

def musicScreen():
    windowm=Tk()
    windowm.title("Music Window")
    windowm.geometry("300x300")
    windowm.configure(bg="LightSkyBlue")

    sLabel=Label(windowm,text="Select a song!",bg='LightSkyBlue',font=("Calibri",8))
    sLabel.place(x=2,y=1)

    listbox=Listbox(windowm,heigh=10,width=39,activestyle="dotbox",borderwidth=2,font=("Calibri",10))

    for file in os.listdir('shared_files'):
        filename=os.fsdecode(file)
        listbox.insert(SONG_COUNTER,filename)
        SONG_COUNTER+=1
    
    
    windowm.mainLoop()

def play():
    global SONG_SELECTED
    SONG_SELECTED=listbox.get(ANCHOR)

    pygame
    mixer.init()
    mixer.music.load("shared_files/"+SONG_SELECTED)
    mixer.music.play()



setup()