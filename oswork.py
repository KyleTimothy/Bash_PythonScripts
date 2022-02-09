import os
import pypsrp

#pypsrp
        
"""
This obtain the current directory
"""
def Get_Current_Dir():
    os.getcwd()

"""
Create a directory
"""

def Creating_Dir(directory):
    os.mkdir(directory)
    os.listdir()
    os.getcwd()
    
"""
This will remove directory
"""
def Remove_Dir(directory):
    os.rmdir(directory)
    os.listdir()
    os.getcwd
Remove_Dir("PiePie")
    
def Change_Working_Dir(directory):
    os.chdir(directory)
    os.getcwd()

"""
List files and sub directories
"""

def List_FilandFolders(directory):
    os.listdir(directory)
    os.getcwd()
    
def Environment():
    os.environ

def Remove_File(file):
    os.remove(file)
    os.listdir()
    os.getcwd()
    
def File_Rename(file1, file2):
    os.rename(file1,file2)
    os.listdir()

def FileStarter(directory):
    dir = directory
   
    os.startfile("r"+dir)


