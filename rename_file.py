# daniel godinez | daniel.godinez30@icloud.com |  python 3.6.3 | Version 2 March 2018
# Import Modules
import os
import time

# Credits: Max S., thank you!
# This script will rename 1 or more files based on the name of the curent file and append the current date and time
# be sure to save this script in the same Working directory as the file(s) you want to re-name
# set time and date to a string
# If you want to set this to run on crontab, you can just define the filename in the python script to rename, after a backup is created
time = time.strftime("%Y%m%d-%H%M%S")
# Get the source path from the current working directory
src_path = os.getcwd()
dest_path = src_path
# renaming the old file appending the current date and time

#declare filename you want to rename

def renameFile ():
    filename = str(input('Enter the name of the current file: '))
    newfilename = filename+' '+time
    current_name = os.path.join(src_path, filename)
    new_name = os.path.join(dest_path, newfilename)
    os.rename(current_name, new_name)


renameFile()

cont = str(input("Done. Rename another? (Y for yes, N for no)"))
if cont == "Y" :
    renameFile()
else:
    print("Have a good day!")


      



