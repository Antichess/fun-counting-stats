# this script assumes you have all nessecary files of the log_files, in a sub-directory containing all of those files that is named "files" as well
# also have ids in a sub-directory called "ids" with the ids
# https://drive.google.com/drive/folders/1_FWMSR66QqOjPIVjklzzN8RytjYyyKg3

import csv
import os

file_list = [x.replace("_log.csv","") for x in os.listdir(os.path.join(os.getcwd(),"files")) if x.endswith(".csv")]
#file_list.remove("tug_of_war")

users = {}
def add_data(u,dat,main):
    if u not in users:
        users[u] = [[],[]]
    if main:
        users[u][0].append(dat)
    else:
        users[u][1].append(dat)

def get_time_diff(d):
    if d < 3600:
        return f"{d//60} min{' ' if d//60 == 1 else 's '}{d%60} second{'' if d%60 == 1 else 's'}"
    
    else:
        if d % 60 >= 30:
            d = d + (60-(d%60))
            
        if d > 84600:
            return f"{d//86400} day{' ' if d//86400 == 1 else 's '}{d%86400//3600} hour{' ' if d%86400//3600 == 1 else 's '}{d%86400%3600//60} min{'' if d%86400%3600//60 == 1 else 's'}"
        else:
            return f"{d//3600} hour{' ' if d//3600 == 1 else 's '}{d%3600//60} min{'' if d%3600//60 == 1 else 's'}"

for c,side_name in enumerate(file_list):
    print(f"{c}/{len(file_list)}: {side_name}")
    ids = []
    rawdata = []
    with open(os.path.join(os.getcwd(),"files",f"{side_name}_log.csv"),"r",encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            rawdata.append(row)
    main_thread = False
    if side_name == "decimal":
        main_thread = True
    try:
        for x in range(len(rawdata)):
            add_data(rawdata[x][1],int(float(rawdata[x][2])),main_thread)
    except IndexError:
        print("indexerror")
        pass

user_time = {}
for u in users:
    temp_list = users[u]
    unix_list = [sorted(temp_list[0]),sorted(temp_list[1])]
    s = [0,0,len(unix_list[0]),len(unix_list[1])]
    for side_main in range(2):
        local_sum = 0
        if len(unix_list[side_main]) > 1:
            for ind in range(1,len(unix_list[side_main])):
                diff = unix_list[side_main][ind] - unix_list[side_main][ind-1]
                if diff >= 0 and diff < 3600: #failsafe
                    if diff < 11:
                        local_sum = local_sum + diff
                    else:
                        local_sum = local_sum + 11
            s[side_main] = local_sum
    user_time[u] = s

data = [[x,user_time[x][0],user_time[x][1],user_time[x][0]+user_time[x][1],user_time[x][2],user_time[x][3]] for x in user_time]
data.sort(key=lambda x:x[3],reverse=True)

with open(f"../results/time_spent_counting.txt","w") as f:
    print(f"Rank|User|Main Time|Main Counts|Side Time|Side Counts|Total Time|Total Counts")
    f.write(f"Rank|User|Main Time|Main Counts|Side Time|Side Counts|Total Time|Total Counts\n")
    print(f":-:|:-:|:-:|-:|:-:|-:|:-:|-:")
    f.write(f":-:|:-:|:-:|-:|:-:|-:|:-:|-:\n")
    for c,x in enumerate(data):
        if x[3] > 3600:
            f.write(f"{c+1}|{x[0]}|{get_time_diff(x[1])}|{x[4]}|{get_time_diff(x[2])}|{x[5]}|{get_time_diff(x[3])}|{x[4]+x[5]}\n")
            print(f"{c+1}|{x[0]}|{get_time_diff(x[1])}|{x[4]}|{get_time_diff(x[2])}|{x[5]}|{get_time_diff(x[3])}|{x[4]+x[5]}")
