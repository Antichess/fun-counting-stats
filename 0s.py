import csv


rawdata = []
with open("decimal_log.csv","r") as file:
    reader = csv.reader(file)

    for row in reader:
        rawdata.append(row)


users = {}
def add_data(u):
    if u not in users:
        users[u] = 1
    else:
        users[u] = users[u] + 1
diff = 0
# difference to test for

for x in range(len(rawdata)-1):
    try:
        if int(float(rawdata[x][2])) == int(float(rawdata[x-1][2])) + diff:
            add_data(rawdata[x][1])
    except:
        pass

print(users)
data = [[x,users[x]] for x in users]
data.sort(key=lambda x:x[1],reverse=True)

print("Rank|User|"+str(diff)+"s")
print(":-:|:-:|:-:")
for c,x in enumerate(data):
    print(f"{c+1}|{x[0]}|{x[1]}")
