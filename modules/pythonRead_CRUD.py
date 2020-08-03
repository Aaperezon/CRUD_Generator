import os

python = ""
def ReadMaker(tableName):
    global python
    python = (
'''

codigo python


'''
        )

def Run(tableName):
    pRead = './Output_files/Read'+tableName+'.php'

    if os.path.exists(pRead):
        os.remove(pRead)
        print ("Removed last file")
    ReadMaker(tableName);
    f = open(pRead, "a")
    f.write(python)
    f.close()
    print("New file created")
    print()