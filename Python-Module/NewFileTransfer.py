''' New/Updated File Transfer w/Python 2.7
By Logan Boespflug
For Windows 10 OS
Created 12/1/16
'''

#Used to copy updated/new files to a new folder once a day
import time
from datetime import datetime
from datetime import date
from datetime import timedelta
from threading import Timer
import shutil
import os

print "Daily Transfer of new files into a New Folder"
print " "
movee="C://Users//Logan//Desktop//New file folder" #Starting Folder
destination="C://Users//Logan//Desktop//Transferring folder" #End Folder

def NewTransfer (movee,destination):  #Function to Move Updated Files
    additional='//' #Needed to create final destination
    print "Files that were copied and moved into new folder:"
    comparision=time.time()
    for filename in os.listdir(movee):
        if comparision-os.path.getmtime(movee+additional+filename)<86400:
            print filename
            print time.ctime(os.path.getmtime(movee+additional+filename))
            shutil.copy(movee+additional+filename,destination+additional+filename)
NewTransfer(movee,destination)

