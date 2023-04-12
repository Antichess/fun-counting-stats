# this script assumes you have all nessecary files of the log_files, in a sub-directory containing all of those files that is named "files" as well
# https://drive.google.com/drive/folders/1_FWMSR66QqOjPIVjklzzN8RytjYyyKg3

import csv
import os

users = {}
def add_data(u):
    if u not in users:
        users[u] = 1
    else:
        users[u] = users[u] + 1

diff = 1
file_list = [x for x in os.listdir(os.path.join(os.getcwd(),"files")) if x.endswith(".csv")]
for c,file in enumerate(file_list):
    rawdata = []
    with open(os.path.join(os.getcwd(),"files",file),"r",encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            rawdata.append(row)
        print(f"{c}/{len(file_list)}: {file}")
        for x in range(1,len(rawdata)-1):
            if (int(float(rawdata[x-1][2]))+diff == int(float(rawdata[x][2]))):
                add_data(rawdata[x][1])
                #print(f"{rawdata[x][1]} https://www.reddit.com/r/counting/comments/{rawdata[x][4]}/_/{rawdata[x][3]}/?context=3")

l = [[x,users[x]] for x in users]
print(f"Rank|User|{diff}s")
print(f":-:|:-:|:-:")
for c,x in enumerate(l):
    print(f"{c+1}|{x[0]}|{x[1]}")
