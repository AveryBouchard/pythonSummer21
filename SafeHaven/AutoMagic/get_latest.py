import os
import glob

folder_path = r'/home/avery/Downloads'
os.chdir(folder_path)

files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)

print(files)

newest = files[-1]

print(newest)