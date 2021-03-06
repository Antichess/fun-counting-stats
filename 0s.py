import csv


rawdata = []
with open("ALL.csv","r") as file:
    reader = csv.reader(file)

    for row in reader:
        rawdata.append(row)


users = []
diff = 0

for x in range(len(rawdata)-1):
    try:
        if (int(float(rawdata[x][2]))+diff == int(float(rawdata[x+1][2]))):
            found = False
            for i in range(len(users)):
                if rawdata[x+1][1] == users[i][0]:
                    users[i] = (users[i][0], users[i][1] + 1)
                    found = True
                    break
            if not found:
                append = (rawdata[x+1][1], 1)
                users.append(append)
    except:
        pass

users.sort(key=lambda x:x[1],reverse=True)
print("Rank|User|"+str(diff)+"s")
print(":-:|:-:|:-:")
for x in range(len(users)):
    print(str(x+1) + "|"  + users[x][0] + "|" + str(users[x][1]))
