'''
NewFile Transfer GUI&DB w/Python 3.5
By Logan Boespflug
For Windows 10 OS
Created 12/3/16
'''

import time
from time import strftime
from datetime import datetime,date,timedelta
from threading import Timer
import shutil
import os
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import filedialog
import getpass
import sqlite3

filemanger=[' ',' ']                                                                #Track of Directory Locations

class MoveFiles:
    connection=sqlite3.connect("TransDate.db")
    connection.execute("DROP TABLE IF EXISTS TransDate")
    connection.execute("CREATE TABLE TransDate(ID INTEGER PRIMARY KEY AUTOINCREMENT,Date FLOAT, Copied TEXT, Pasted TEXT, EpochSec FLOAT)")
    cur=connection.cursor()
    
    def __init__(self,master):                                                      #Runs the GUI for Program, note uses filemanger to track directories
        self.master=master
        master.title('Transfer Directory')
                            
        self.lbl_COPYFROM=tk.Label(self.master,text='Copy From:')                   #Section for Copy
        self.lbl_COPYFROM.grid(row=0,column=0,padx=(5,0),pady=(10,0),sticky=N+W)
        self.Browser=tk.Button(text = 'Browse',command=lambda: self.directorystuff(0)).grid(row = 1,column = 0)

        self.lbl_PASTETO=tk.Label(self.master,text='Paste To:')                     #Section for Paste
        self.lbl_PASTETO.grid(row=3,column=0,padx=(5,0),pady=(10,0),sticky=N+W)
        self.Browser2=tk.Button(text = 'Browse',command=lambda:self.directorystuff(1)).grid(row = 4,column = 0)

        self.COMPLETE=tk.Button(text = 'Run',background='green',command=self.transfers).grid(row = 6,column = 0,pady=(5,0))         #Executes Transfer

    def directorystuff(self,throughput):                                            #Generates Directory List in filemanger
        direct=str(filedialog.askdirectory())                                       #Returns a selected directory name
        filemanger[throughput]=direct
        if throughput==0:
            print ('Copy New Files from: '+str(direct))
        else:
            print ('Paste New Files into: '+str(direct))
        return filemanger

    def transfers(self):                                                            #Actually Transfer Process
        additional='//'                                                             #Needed to create final destination
        copy=str(filemanger[0])
        paste=str(filemanger[1])
        
        comparision=time.time()                                                     
        rightnow=datetime.now().strftime('%Y-%m-%d %H:%M') 
        last=self.cur.lastrowid                                                     #Checks if Table is Empty
        
        if last==None:
            for filename in os.listdir(copy):
                if comparision-os.path.getmtime(copy+additional+filename)<86400:
                    print (filename)
                    print (time.ctime(os.path.getmtime(copy+additional+filename)))
                    shutil.copy(copy+additional+filename,paste+additional+filename)
            self.lbl_RESULTS=tk.Label(self.master,text='TRANSFERED FOR THE FIRST TIME')
            self.lbl_RESULTS.grid(row=7,column=0,padx=(5,0),pady=(10,0),sticky=N+W)
            self.cur.execute("INSERT INTO TransDate VALUES(NULL,?,?,?,?)",(rightnow,copy,paste,comparision))
            self.connection.commit()
        else:
            self.lbl_RESULTS.grid_forget()
            self.cur.execute("SELECT * FROM TransDate WHERE ID=last_insert_rowid()")
            for row in self.cur.fetchall():
                key=row
                timestamp=key[4]
            for filename in os.listdir(copy):
                if timestamp-os.path.getmtime(copy+additional+filename)<86400: 
                    print (filename)
                    print (time.ctime(os.path.getmtime(copy+additional+filename)))
                    shutil.copy(copy+additional+filename,paste+additional+filename)
            self.lbl_RESULTS=tk.Label(self.master,text='PROGRAM LAST RAN AT THIS TIME:')
            self.lbl_RESULTS.grid(row=7,column=0,padx=(5,0),pady=(10,0),sticky=N+W)
            
            self.lbl_RESULTS1=tk.Label(self.master,text=rightnow)
            self.lbl_RESULTS1.grid(row=8,column=0,padx=(5,0),pady=(10,0),sticky=N+W)
            
            self.cur.execute("INSERT INTO TransDate VALUES(NULL,?,?,?,?)",(rightnow,copy,paste,comparision))
            self.connection.commit()
            
def main():
    root=Tk()
    Script=MoveFiles(root)
    root.mainloop()                        
if __name__ == "__main__": main()
    
