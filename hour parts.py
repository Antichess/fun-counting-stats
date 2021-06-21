import csv

def add_data(users,user):
    found = False
    for x in range(len(users)):
        if user == users[x][0]:
            users[x] = (user, users[x][1] + 1)
            found = True
            break
    if not found:
        append = (user, 1)
        users.append(append)

rawdata = []
with open("ALL.csv","r") as file:
    reader = csv.reader(file)

    for row in reader:
        rawdata.append(row)


users = []
temp = []
hour = 0

for x in range(len(rawdata)):
    try:
        if hour != (int(float(rawdata[x][2])) // 3600):
            hour = int(float(rawdata[x][2])) // 3600
            for user in temp:
                add_data(users, user)
            temp = []
        if rawdata[x][1] != "[deleted]":
            if rawdata[x][1] not in temp:
                temp.append(rawdata[x][1])
        if x % 10000 == 0:
            users.sort(key=lambda x:x[1],reverse=True)
            print(x)
    except:
        pass
    
users.sort(key=lambda x:x[1],reverse=True)

print("Rank|User|Hour Parts")
print(":-:|:-|:-")
for x in range(len(users)):
    if users[x][1] > 100:
        print(str(x+1) + "|" + users[x][0] + "|" + str(users[x][1]))
