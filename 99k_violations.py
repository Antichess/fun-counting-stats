import csv

two_minute_rule = [2199,2299,2999,4999]
last_counts = {}
users = {}
def add_data(u):
    if u not in users:
        users[u] = 1
    else:
        users[u] = users[u] + 1

rawdata = []
with open("decimal_log.csv","r") as file:
    reader = csv.reader(file)
    for row in reader:
        rawdata.append(row)
print("loaded")
permit = 60
thread_start = 0


for x in range(1,len(rawdata)-1):
    
    if int(rawdata[x][0]) // 1000 % 100 == 99:
        if int(rawdata[x][0]) % 1000 == 0:
            thread_start = int(float(rawdata[x][2]))
        if (int(rawdata[x][0]) // 1000) in two_minute_rule:
            permit = 120
        else:
            permit = 60
        if rawdata[x][1] in last_counts:
            if int(float(rawdata[x][2])) - last_counts[rawdata[x][1]] < permit:
                if int(float(rawdata[x][2])) - thread_start < 86400:
                    add_data(rawdata[x][1])
        last_counts[rawdata[x][1]] = int(float(rawdata[x][2]))
    else:
        last_counts = {}

data = [[x,users[x]] for x in users]
data.sort(key=lambda x:x[1],reverse=True)
print(data)
        
print(f"Rank|User|99k violations")
print(f":-:|:-:|:-:")
for c,x in enumerate(data):
    print(f"{c+1}|{x[0]}|{x[1]}")
