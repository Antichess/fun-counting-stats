import csv

def get_time(d):
    if d < 3600:
        return f"{d//60}m {d%60}s"
    else:          
        if d > 84600:
            return f"{d//86400}d {d%86400//3600}h {d%86400%3600//60}m"
        else:
            return f"{d//3600}h {d%3600//60}m"


users = {}

def add_data(user,s):
    if user not in users:
        users[user] = s
    else:
        users[user] = users[user] + s
rawdata = []
with open("decimal_log.csv","r") as file:
    reader = csv.reader(file)

    for row in reader:
        rawdata.append(row)

print("loaded")


for x in range(1,len(rawdata)-1):
    try:
        add_data(rawdata[x][1],(int(float(rawdata[x+1][2])) - int(float(rawdata[x][2]))))
        #print(rawdata[x][0] + " " + rawdata[x][1] + " " + str(int(float(rawdata[x+1][2])) - int(float(rawdata[x][2]))))
        if int(float(rawdata[x][0])) % 100000 == 0:
            print(int(float(rawdata[x][0])))
    except:
        pass

sorted_data = [[x,users[x]] for x in users if users[x] > 20000]
sorted_data.sort(key=lambda x:x[1],reverse=True)

with open("results/time_held_count.txt","w") as f:

    print("Rank|User|Time held count")
    f.write(f"Rank|User|Time held count\n")
    print(":-:|:-:|:-:")
    f.write(f":-:|:-:|:-:\n")
    for c,x in enumerate(sorted_data):
        print(f"{c+1}|{x[0]}|{get_time(x[1])}")
        f.write(f"{c+1}|{x[0]}|{get_time(x[1])}\n")

