import csv

#users = user, curr1, curr2, record1, record2, currdiff, recorddiff

def add_data(users,user,c):
    found = False
    for x in range(len(users)):
        if user == users[x][0]:
            if users[x][5] < (c - users[x][2]):
                users[x] = (user, users[x][2], c, users[x][2], c, c - users[x][2], c - users[x][2])
            else:
                users[x] = (user, users[x][2], c, users[x][3], users[x][4], c - users[x][2], users[x][6])
            found = True
    if not found:
        append = (user, c, c, c, c, 0, 0)
        users.append(append)

rawdata = []
with open("ALL.csv","r") as file:
    reader = csv.reader(file)

    for row in reader:
        rawdata.append(row)

temp = []
users = []
for x in range(len(rawdata)):
    try:
        add_data(temp,rawdata[x][1],int(float(rawdata[x][0])))
    except:
        pass
    if x % 10000 == 0:
        for i in range(len(temp)):
            add_data(users,temp[i][0],temp[i][2])
        temp = []
        print(x)
        users.sort(key=lambda x:x[5],reverse=False)

for i in range(len(temp)):
    add_data(users,temp[i][0],temp[i][2])

users.sort(key=lambda x:x[6],reverse=True)

print("Rank|User|First Count|Ending Count|Diff")
print(":-:|:-:|:-:|:-:|-:")
for x in range(len(users)):
    if users[x][6] > 10000:
        print(str(x+1) + "|" + users[x][0] + "|" + str(users[x][3]) + "|" + str(users[x][4]) + "|" + str(users[x][6]))
        
