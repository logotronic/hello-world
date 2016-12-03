'''
NewFile Transfer GUI w/Python 3.5
By Logan Boespflug
For Windows 10 OS
Created 12/1/16
'''

import time
from datetime import datetime
from datetime import date
from datetime import timedelta
from threading import Timer
import shutil
import os
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import filedialog
import getpass

filemanger=[' ',' '] #Track of Directory Locations

class MoveFiles:
    def __init__(self,master):
        self.master=master
        master.title('Transfer Directory')
                            
        self.lbl_COPYFROM=tk.Label(self.master,text='Copy From:')
        self.lbl_COPYFROM.grid(row=0,column=0,padx=(5,0),pady=(10,0),sticky=N+W)
        self.Browser=tk.Button(text = 'Browse',command=lambda: self.directorystuff(0)).grid(row = 1,column = 0)

        self.lbl_PASTETO=tk.Label(self.master,text='Paste To:')
        self.lbl_PASTETO.grid(row=3,column=0,padx=(5,0),pady=(10,0),sticky=N+W)
        self.Browser2=tk.Button(text = 'Browse',command=lambda:self.directorystuff(1)).grid(row = 4,column = 0)

        self.COMPLETE=tk.Button(text = 'Run',background='green',command=self.transfers).grid(row = 6,column = 0,pady=(5,0))

    def directorystuff(self,throughput):
        direct=str(filedialog.askdirectory()) #Returns a selected directory name
        filemanger[throughput]=direct
        if throughput==0:
            print ('Copy New Files from: '+str(direct))
        else:
            print ('Paste New Files into: '+str(direct))
        return filemanger

    def transfers(self):
        additional='//' #Needed to create final destination
        copy=str(filemanger[0])
        paste=str(filemanger[1])
        comparision=time.time()
        for filename in os.listdir(copy):
            if comparision-os.path.getmtime(copy+additional+filename)<86400:
                print (filename)
                print (time.ctime(os.path.getmtime(copy+additional+filename)))
                shutil.copy(copy+additional+filename,paste+additional+filename)

def main():
    root=Tk()
    Script=MoveFiles(root)
    root.mainloop()                        
if __name__ == "__main__": main()
    
