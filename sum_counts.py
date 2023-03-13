import csv
from datetime import datetime, timedelta

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
with open("decimal_log.csv","r") as file:
    reader = csv.reader(file)

    for row in reader:
        rawdata.append(row)

users = []
temp = []
for x in range(1,len(rawdata)-1):
    try:
        add_data(temp,rawdata[x][1],int(rawdata[x][0]))
        if int(float(rawdata[x][0])) % 10000 == 0:
            for y in range(len(temp)):
                add_data(users,temp[y][0],temp[y][1])
            users.sort(key=lambda x:x[1],reverse=True)
            temp.clear()
            print(int(float(rawdata[x][0])))
    except:
        pass

for y in range(len(temp)):
    add_data(users,temp[y][0],temp[y][1])

sorted_data = []


for x in range(len(users)):
    if users[x][1] > 1000000000:
        sorted_data.append(users[x])

sorted_data.sort(key=lambda x:x[1],reverse=True)

print("Rank|User|Total sum of counts")
print(":-:|:-:|:-:")
for x in range(len(sorted_data)):
    print(f"{str(x+1)} | {sorted_data[x][0]} | {'{:,}'.format(sorted_data[x][1])}")

