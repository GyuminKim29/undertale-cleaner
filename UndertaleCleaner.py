import os
import shutil

# get username
user = input("Windows Username : ")
# set location
loc = r"C:\Users\{}\AppData\Local\UNDERTALE".format(user)
# delete savedata(s)
shutil.rmtree(loc)