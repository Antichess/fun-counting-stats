# this script assumes you have all nessecary files of the log_files, in a sub-directory containing all of those files that is named "files" as well
# also have ids in a sub-directory called "ids" with the ids
# https://drive.google.com/drive/folders/1_FWMSR66QqOjPIVjklzzN8RytjYyyKg3

import csv
import os

file_list = [x.replace("_log.csv","") for x in os.listdir(os.path.join(os.getcwd(),"files")) if x.endswith(".csv")]

users = {}
def add_data(u):
    if u not in users:
        users[u] = 1
    else:
        users[u] = users[u] + 1

for c,side_name in enumerate(file_list):
    print(f"{c}/{len(file_list)}: {side_name}")
    ids = []
    rawdata = []
    with open(os.path.join(os.getcwd(),"ids",f"{side_name}_ids.csv"),"r") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) == 2:
                ids.append(row[1])
    with open(os.path.join(os.getcwd(),"files",f"{side_name}_log.csv"),"r",encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            rawdata.append(row)
    ind = 0
    fail = False
    start = 0
    e_o = ["",""]
    high_score = 0
    try:
        for x in range(len(rawdata)):
            if not fail:
                if e_o[start % 2] == "":
                    e_o[start % 2] = rawdata[x][1]
                elif e_o[start % 2] != rawdata[x][1]:
                    e_o[start % 2] = "fail"
                if e_o == ["fail","fail"]:
                    fail = True
            if ids[ind] == rawdata[x][3]:
                if not fail:
                    [add_data(z) for z in e_o if z != "fail"]
                    [print(f"https://www.reddit.com/r/counting/comments/{rawdata[x][4]}/") for z in e_o if z != "fail"]
                ind = ind + 1
                start = 0
                e_o = ["",""]
                fail = False
            start = start + 1

    except IndexError:
        print("indexerror")
        pass

data = [[x,users[x]] for x in users]
data.sort(key=lambda x:x[1],reverse=True)

print(f"Rank|User|Perfect threads")
print(f":-:|:-:|:-:")
for c,x in enumerate(data):
    print(f"{c+1}|{x[0]}|{x[1]}")
