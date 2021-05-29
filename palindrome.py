import csv


rawdata = []
with open("ALL.csv","r") as file:
    reader = csv.reader(file)

    for row in reader:
        rawdata.append(row)

users = []
for x in range(len(rawdata)):
    try:
        if (str(int(float(rawdata[x][0]))) == str(int(float(rawdata[x][0])))[:: -1]):
            found = False
            for i in range(len(users)):
                if rawdata[x][1] == users[i][0]:
                    users[i] = (users[i][0], users[i][1] + 1)
                    found = True
                    break
            if not found:
                append = (rawdata[x][1], 1)
                users.append(append)
                print(rawdata[x][0] + " " + rawdata[x][1])
    except:
        pass

users.sort(key=lambda x:x[1],reverse=True)
print("Rank|User|Palindromes")
print(":-:|:-:|:-:")
for x in range(len(users)):
    print(str(x+1) + "|"  + users[x][0] + "|" + str(users[x][1]))
