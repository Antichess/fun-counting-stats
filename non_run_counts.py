import csv
import numpy

rawdata = []
with open("decimal_log.csv","r") as file:
    reader = csv.reader(file)
    for row in reader:
        rawdata.append(row)
print("loaded")

users={}

def add_data(u,bool):
    if u not in users:
        users[u] = [0,0]
    if bool:
        users[u][0] = users[u][0] + 1
    users[u][1] = users[u][1] + 1



for x in range(len(rawdata)):
    try:
        if x % 100000 == 0:
            print(x)
        if int(float(rawdata[x][2]))-int(float(rawdata[x-1][2])) >= 30:
            add_data(rawdata[x][1],True)
        elif rawdata[x][1] != rawdata[x-1][1] and rawdata[x][1] != rawdata[x-2][1]:
            add_data(rawdata[x][1],True)
        else:
            add_data(rawdata[x][1],False)
    except:
        pass

data = [[x,users[x][0],users[x][1]] for x in users if users[x][1] > 1000]
data.sort(key=lambda x:x[1],reverse=True)

with open(f"results/non_run_counts.txt","w") as f:
    print(f"Rank|User|Non-run Counts|% counts")
    f.write(f"Rank|User|Non-run Counts|% counts\n")
    print(f":-:|:-:|-:")
    f.write(f":-:|:-:|-:\n")
    for c,x in enumerate(data):
        print(f"{c+1}|{x[0]}|{x[1]}|{x[1]/x[2]*100:.2f}%")
        f.write(f"{c+1}|{x[0]}|{x[1]}|{x[1]/x[2]*100:.2f}%\n")
