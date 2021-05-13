import os.path
from os import path
import time

req_file = ("Dummy_data.csv")
file_present = path.exists(req_file)

print('Checking file in the location...')
if file_present == True:
    print (f"The file {req_file} exists in the given location")
else:
    print("File doesn't exist")
    

print("Last modified time : %s" % time.ctime(os.path.getmtime("Dummy_data.csv")))
print("Created time : %s" % time.ctime(os.path.getctime("Dummy_data.csv")))

curr_time =   time.ctime(os.path.getmtime("Dummy_data.csv"))
cret_time =   time.ctime(os.path.getctime("Dummy_data.csv"))

print(curr_time)
print(cret_time)

print('Creating hyperfile with the given schema')
import hyper_data_updater

print('All the data has been updated in hyper file with latest changes')