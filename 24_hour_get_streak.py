import csv

def get_time_diff(d):
    if d < 3600:
        return f"{d//60} min{' ' if d//60 == 1 else 's '}{d%60} second{'' if d%60 == 1 else 's'}"
    
    else:
        if d % 60 >= 30:
            d = d + (60-(d%60))
            
        if d > 84600:
            return f"{d//86400} day{' ' if d//86400 == 1 else 's '}{d%86400//3600} hour{' ' if d%86400//3600 == 1 else 's '}{d%86400%3600//60} min{'' if d%86400%3600//60 == 1 else 's'}"
        else:
            return f"{d//3600} hour{' ' if d//3600 == 1 else 's '}{d%3600//60} min{'' if d%3600//60 == 1 else 's'}"
        
rawdata = []
with open("decimal_log.csv","r") as file:
    reader = csv.reader(file)

    for row in reader:
        rawdata.append(row)
print("loaded")

records = {}
current_streaks = {}

def add_streak(user,t,k):
    if user not in current_streaks:
        current_streaks[user] = [0,t,t,k,k]
    current_streaks[user][0] = current_streaks[user][0] + 1
    current_streaks[user][2] = t
    current_streaks[user][4] = k

def transfer_record(user,r,diff,f,l):
    if user not in records:
        records[user] = [r,diff,f,l]
    elif diff > records[user][1]:
        records[user] = [r,diff,f,l]

for x in range(1,len(rawdata)):
    if x % 100000 == 0:
        print(x)
    #try:
    if int(rawdata[x][0]) % 1000 == 0:
        if rawdata[x][1] in current_streaks:
            if int(float(rawdata[x][2])) - current_streaks[rawdata[x][1]][2] > 86400:
                transfer_record(rawdata[x][1],current_streaks[rawdata[x][1]][0],current_streaks[rawdata[x][1]][2]-current_streaks[rawdata[x][1]][1]+86399,current_streaks[rawdata[x][1]][3],current_streaks[rawdata[x][1]][4])
                current_streaks.pop(rawdata[x][1])
        add_streak(rawdata[x][1],int(float(rawdata[x][2])),f"[{int(rawdata[x][0])//1000:.0f}k](https://www.reddit.com/r/counting/comments/{rawdata[x][4]}/_/{rawdata[x][3]}/?context=3)")
    """ except:
        print(rawdata[x][0])
        pass """
    
l = [[x,records[x][0],records[x][1],records[x][2],records[x][3]] for x in records]
l.sort(key=lambda x:x[2],reverse=True)

with open(f"results/24_hour_get_streak.txt","w") as f:
    f.write(f"Rank|User|Gets|Time|First|Last\n")
    f.write(f":-:|:-:|:-:|:-:|:-:|:-:\n")
    for c,x in enumerate(l):
        f.write(f"{c+1}|{x[0]}|{x[1]}|{get_time_diff(x[2])}|{x[3]}|{x[4]}\n")
