''' File Mover written w/Python 2.7
by Logan Boespflug
created on 11/30/16
'''

import shutil
import os
movee="C://Users//Logan//Desktop//Folder A"
destination="C://Users//Logan//Desktop//Folder B"
additional='//' #Needed to create final destination
for filename in os.listdir(movee):
    if filename.endswith(".txt"):
        print filename
        shutil.move(movee+additional+filename,destination+additional+filename)
