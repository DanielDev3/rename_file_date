# Daniel Godinez | Version 1 | Python 3.6.3 | March 2018
# Credits: Max S.
# This python script is relating to OpenEMR backup procedures
# This can be run immediately after the backup script runs on Linux.
# but it can be altered to your own purposes. See Version 2 for a manual version
# Import Modules

import os
import time

time = time.strftime("%Y%m%d-%H%M%S")

filename1 ="openemr"
filename2 = "openemr.1.tar.gz"
src_path ="/home/administrator/backups"

dst_path ="/home/administrator/backups"
newfilename1 = filename1+"_"+time
newfilename2 = "openemr"+"_"+time+".tar.gz"

current_name  = os.path.join(src_path,filename1)
current_name2 = os.path.join(src_path,filename2)
 
new_name  = os.path.join(dst_path,newfilename1)
new_name2 = os.path.join(dst_path,newfilename2)

os.rename(current_name, new_name)
os.rename(current_name2,new_name2)

