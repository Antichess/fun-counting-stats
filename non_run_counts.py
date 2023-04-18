import csv
import numpy

rawdata = []
with open("decimal_log.csv","r") as file:
    reader = csv.reader(file)
    for row in reader:
        rawdata.append(row)
print("loaded")

users={}

def add_data(u):
    if u not in users:
        users[u] = 0
    users[u] = users[u] + 1


for x in range(len(rawdata)):
    try:
        if x % 100000 == 0:
            print(x)
        if int(float(rawdata[x][2]))-int(float(rawdata[x-1][2])) >= 30:
            add_data(rawdata[x][1])
        elif rawdata[x][1] != rawdata[x-1][1] and rawdata[x][1] != rawdata[x-2][1]:
            add_data(rawdata[x][1])
    except:
        pass

data = [[x,users[x]] for x in users if users[x] > 1000]
data.sort(key=lambda x:x[1],reverse=True)

with open(f"results/non_run_counts.txt","w") as f:
    print(f"Rank|User|Non-run Counts")
    f.write(f"Rank|User|Non-run Counts\n")
    print(f":-:|:-:|-:")
    f.write(f":-:|:-:|-:\n")
    for c,x in enumerate(data):
        print(f"{c+1}|{x[0]}|{x[1]}")
        f.write(f"{c+1}|{x[0]}|{x[1]}\n")
