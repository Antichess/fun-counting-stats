import csv

rawdata = []
with open("decimal_log.csv","r") as file:
    reader = csv.reader(file)
    for row in reader:
        rawdata.append(row)
print("loaded")

def add_data(to_dict,i,change,mode):
    if i not in to_dict:
        to_dict[i] = [0,0]
    to_dict[i][mode] = to_dict[i][mode] + change

users = {}
# 0 replied , replies TO
# 1 replies , replies FROM

user = "Antichess"
for x in range(1,len(rawdata)-1):
    try:
        if rawdata[x][1] == user:
            add_data(users,rawdata[x-1][1],1,1)
            add_data(users,rawdata[x+1][1],1,0)
        if x % 100000 == 0:
            print(x)
    except:
        pass

sorted_data = []
for x in users:
    if (users[x][0] + users[x][1]) > 50:
        sorted_data.append([x, users[x][0], users[x][1], users[x][0] + users[x][1]])
sorted_data.sort(key=lambda x:x[3],reverse=True)


print(f"{user}'s favourite counters\n")
print(f"Rank|User|Replies to|Replies from|Combined")
print(f":-:|:-:|-:|-:|-:")
for c,x in enumerate(sorted_data):
    print(f"{c+1}|{x[0]}|{x[1]}|{x[2]}|{x[3]}")