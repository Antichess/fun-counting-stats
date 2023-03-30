import csv

rawdata = []
with open("tug_of_war_log.csv","r") as file:
    reader = csv.reader(file)
    for row in reader:
        rawdata.append(row)
print("loaded")

alts = []
with open("../input/prefs/Aliases.txt","r") as f:
    alts = f.read()
alts = alts.split("\n")
alts = [x.split(",") for x in alts]



users = {}

def add_data(u,ch):
    #-1,1
    #pos,neg
    if u not in users:
        if ch == 1:
            users[u] = [1, 0, 1]
        else:
            users[u] = [0, 1, 1]
    else:
        if ch == 1:
            users[u][0] = users[u][0] + 1
        else:
            users[u][1] = users[u][1] + 1
        users[u][2] = users[u][2] + 1

def alt(user):
    for x in alts:
        if x[0] == user:
            return user
        if user in x[1::]:
            return x[0]
    return user

for x in range(len(rawdata)-1):
    if x % 5000 == 0:
        print(x)
    try:
        c = (int(rawdata[x][0])-int(rawdata[x-1][0]))
        add_data(alt(rawdata[x][1]),c)
    except:
        pass

d = [[x] + users[x] + [100*users[x][0]/users[x][2],100*users[x][1]/users[x][2]] for x in users if users[x][2] > 250]

d_n = sorted(d, key=lambda x:(x[4],-x[3]),reverse=False)
d_p = sorted(d, key=lambda x:(x[5],-x[3]),reverse=False)
d_o = sorted(d, key=lambda x:(abs(50-x[4]),-x[3]),reverse=False)

with open(f"results/most_faithful_tow_counters.txt","w") as f:
    f.write(f"#Most faithful Tug of War counters\n")
    print(f"#Most faithful Tug of War counters")
    f.write(f"Faithful towards Positive\n")
    print(f"Faithful towards Positive\n")
    f.write(f"Rank|User|Positive count %|Counts\n")
    print(f"Rank|User|Positive count %|Counts")
    f.write(f":-:|:-:|:-:|:-:\n")
    print(f":-:|:-:|:-:|:-:")
    
    for c,x in enumerate(d_p):
        f.write(f"{c+1}|{x[0]}|{x[4]:.2f}%|{x[3]}\n")
        if c < 10:
            print(f"{c+1}|{x[0]}|{x[4]:.2f}%|{x[3]}")

    f.write(f"Faithful towards Negative\n")
    print(f"Faithful towards Negative\n")
    f.write(f"Rank|User|Negative count %|Counts\n")
    print(f"Rank|User|Negative count %|Counts")
    f.write(f":-:|:-:|:-:|:-:\n")
    print(f":-:|:-:|:-:|:-:")
    
    for c,x in enumerate(d_n):
        f.write(f"{c+1}|{x[0]}|{x[5]:.2f}%|{x[3]}\n")
        if c < 10:
            print(f"{c+1}|{x[0]}|{x[5]:.2f}%|{x[3]}")

    f.write(f"Faithful towards Neither\n")
    print(f"Faithful towards Neither\n")
    f.write(f"Rank|User|Positive count %|Counts\n")
    print(f"Rank|User|Positive count %|Counts")
    f.write(f":-:|:-:|:-:|:-:\n")
    print(f":-:|:-:|:-:|:-:")

    for c,x in enumerate(d_o):
        f.write(f"{c+1}|{x[0]}|{x[4]:.2f}%|{x[3]}\n")
        if c < 10:
            print(f"{c+1}|{x[0]}|{x[4]:.2f}%|{x[3]}")
