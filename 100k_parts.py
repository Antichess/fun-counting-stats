import csv
import numpy

rawdata = []
with open("decimal_log.csv","r") as file:
    reader = csv.reader(file)
    for row in reader:
        rawdata.append(row)
print("loaded")

users={}

def new_100k_data():
    d = [False for x in range(100001)]
    d[100000] = 0
    return d

""" def add_data(u,c):
    if u not in users:
        users[u] = [new_100k_data()]
    users[u][c] = True """

def add_data(u,c):
    if u not in users:
        users[u] = []
    users[u].append(c)


for x in range(len(rawdata)):
    if x % 100000 == 0:
        print(x)
    add_data(rawdata[x][1],int(rawdata[x][0])%1000000)

data = [[x,len(set(users[x]))] for x in users if len(users[x]) > 2000]
data.sort(key=lambda x:x[1],reverse=True)

#print(data)

with open(f"results/100k_parts.txt","w") as f:
    print(f"Rank|User|100k parts")
    f.write(f"Rank|User|100k parts\n")
    print(f":-:|:-:|-:")
    f.write(f":-:|:-:|-:\n")
    for c,x in enumerate(data):
        print(f"{c+1}|{x[0]}|{x[1]}")
        f.write(f"{c+1}|{x[0]}|{x[1]}\n")
