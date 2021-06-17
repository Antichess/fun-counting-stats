import time
import datetime
import csv


rawdata = []
with open("ALL.csv","r") as file:
    reader = csv.reader(file)

    for row in reader:
        rawdata.append(row)

users = []
for x in range(len(rawdata)):
    try:
        found = False
        for i in range(len(users)):
            if users[i][0] == rawdata[x][1]:
                sconvert = datetime.datetime.fromtimestamp(int(float(rawdata[x][2])))
                currentstamp = str(sconvert.strftime('%Y-%m-%d'))
                if users[i][2] != currentstamp:
                    nextdayconvert = datetime.datetime.fromtimestamp(int(float(users[i][5]))+86400)
                    nextday = str(nextdayconvert.strftime('%Y-%m-%d'))
                    if currentstamp == nextday:
                        users[i] = (users[i][0],users[i][1],currentstamp,users[i][3],users[i][4],int(float(rawdata[x][2])),users[i][6]+1,users[i][7])
                    else:
                        if users[i][6] > users[i][7]:
                            users[i] = (users[i][0],currentstamp,currentstamp,users[i][1],users[i][2],int(float(rawdata[x][2])),1,users[i][6])
                        else:
                            users[i] = (users[i][0],currentstamp,currentstamp,users[i][3],users[i][4],int(float(rawdata[x][2])),1,users[i][7])
                        
                else:
                    users[i] = (users[i][0],users[i][1],users[i][2],users[i][3],users[i][4],int(float(rawdata[x][2])),users[i][6],users[i][7])
                    
                found = True
                break
        if not found:
            timestamp = datetime.datetime.fromtimestamp(int(float(rawdata[x][2])))
            startstamp = str(timestamp.strftime('%Y-%m-%d'))
            append = (rawdata[x][1],startstamp,startstamp,startstamp,startstamp,int(float(rawdata[x][2])),1,1)
            users.append(append)

        if x % 10000 == 0:
            users.sort(key=lambda x:x[6],reverse=True)
            print(str(x))
    except:
        pass

for x in range(len(users)):
    if users[i][6] > users[i][7]:
        users[i] = (users[i][0],currentstamp,currentstamp,users[i][1],users[i][2],int(float(rawdata[x][2])),1,users[i][6])
    else:
        users[i] = (users[i][0],currentstamp,currentstamp,users[i][3],users[i][4],int(float(rawdata[x][2])),1,users[i][7])
    
users.sort(key=lambda x:x[7],reverse=True)
print("Rank|User|Start Date|End Date|Days")
print(":-:|:-:|:-:|:-:|-:")
for x in range(len(users)):
    
    if int(users[x][7]) > 4:
        print(str(x+1) + "|" + users[x][0] + "|" + users[x][3] +  "|" + users[x][4] + "|" + str(users[x][7]))
