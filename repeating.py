import csv

def repeating(n):
    arr = list(str(n))
    n = []
    for x in range(0,10):
        if arr.count(str(x)) == 1:
            return False
            break
    return True

rawdata = []
with open("ALL.csv","r") as file:
    reader = csv.reader(file)

    for row in reader:
        rawdata.append(row)

users = []
for x in range(len(rawdata)):
    try:
        if repeating(rawdata[x][0]):
            found = False
            for i in range(len(users)):
                if rawdata[x][1] == users[i][0]:
                    users[i] = (users[i][0], users[i][1] + 1)
                    found = True
                    break
            if not found:
                append = (rawdata[x][1], 1)
                users.append(append)
    except:
        pass

users.sort(key=lambda x:x[1],reverse=True)
print("Rank|User|Repeating Digits")
print(":-:|:-:|-:")
for x in range(len(users)):
    print(str(x+1) + "|"  + users[x][0] + "|" + str(users[x][1]))
