import csv
from datetime import datetime, timedelta

def get_time(seconds):
    leftover = seconds % 86400
    seconds -= leftover
    days = seconds / 86400
    seconds = leftover
    leftover = seconds % 3600
    seconds -= leftover
    hours = seconds / 3600
    seconds = leftover
    leftover = seconds % 60
    seconds -= leftover
    mins = seconds / 60
    seconds = leftover
    return str(int(days)) + "d " + str(int(hours)) + "h " + str(int(mins)) + "m " + str(int(seconds)) + "s"


def add_data(users,user,s):
    found = False
    for x in range(len(users)):
        if user in users[x]:
            users[x] = (user, users[x][1] + s)
            found = True
            break
    if not found:
        append = (user, s)
        users.append(append)

rawdata = []
with open("ALL.csv","r") as file:
    reader = csv.reader(file)

    for row in reader:
        rawdata.append(row)

users = []
temp = []
for x in range(1,len(rawdata)-1):
    try:
        add_data(temp,rawdata[x][1],(int(float(rawdata[x+1][2])) - int(float(rawdata[x][2]))))
        #print(rawdata[x][0] + " " + rawdata[x][1] + " " + str(int(float(rawdata[x+1][2])) - int(float(rawdata[x][2]))))
        if int(float(rawdata[x][0])) % 10000 == 0:
            for y in range(len(temp)):
                add_data(users,temp[y][0],temp[y][1])
            users.sort(key=lambda x:x[1],reverse=True)
            temp.clear()
            print(int(float(rawdata[x][0])))
    except:
        pass

sorted_data = []


for x in range(len(users)):
    if users[x][1] > 10000:
        sorted_data.append(users[x])

sorted_data.sort(key=lambda x:x[1],reverse=True)

print("Rank|User|Time held count")
print(":-:|:-:|:-:")
for x in range(len(sorted_data)):
    print(str(x+1) + "|"  + sorted_data[x][0] + "|" + get_time(sorted_data[x][1]))

