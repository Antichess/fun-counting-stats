import csv
from datetime import datetime



rawdata = []
with open("decimal_log.csv","r") as file:
    reader = csv.reader(file)

    for row in reader:
        rawdata.append(row)
print("loaded")



def gen_get_user_string(user):
    if user not in get_users:
        get_users[user] = 1
        return user
    else:
        get_users[user] = get_users[user] + 1
        return f"{user}^{get_users[user]}"
    
def gen_assist_user_string(user):
    if user not in assist_users:
        assist_users[user] = 1
        return user
    else:
        assist_users[user] = assist_users[user] + 1
        return f"{user}^{assist_users[user]}"
        
def get_time_diff(time,last):
    d = time-last
    if d < 3600:
        return f"{d//60} min{' ' if d//60 == 1 else 's '}{d%60} second{'' if d%60 == 1 else 's'}"
    else:
        if d % 60 >= 30:
            d = d + (60-(d%60))
            
        if d > 84600:
            return f"{d//86400} day{' ' if d//86400 == 1 else 's '}{d%86400//3600} hour{' ' if d%86400//3600 == 1 else 's '}{d%86400%3600//60} min{'' if d%86400%3600//60 == 1 else 's'}"
        else:
            return f"{d//3600} hour{' ' if d//3600 == 1 else 's '}{d%3600//60} min{'' if d%3600//60 == 1 else 's'}"

get_users = {}
assist_users = {}
gets = {}
assists = {}
last_get = int(float(rawdata[0][2]))
last_year = datetime.utcfromtimestamp(last_get).strftime('%Y')
print(datetime.utcfromtimestamp(last_get).strftime('%d %b %H:%M'))


for x in range(1,len(rawdata)):
    if x % 100000 == 0:
        print(x)
    try:
        if int(rawdata[x][0]) % 1000 == 0:
            last_year = datetime.utcfromtimestamp(int(float(rawdata[x][2]))).strftime('%Y')
            if last_year not in gets:
                gets[last_year] = []
                assists[last_year] = []
            gets[last_year].append(f"|{int(rawdata[x][0]):,}| [/u/{gen_get_user_string(rawdata[x][1])}](https://www.reddit.com/r/counting/comments/{rawdata[x][4]}/_/{rawdata[x][3]}/?context=3) | {datetime.utcfromtimestamp(int(float(rawdata[x][2]))).strftime('%d %b %H:%M')} | {get_time_diff(int(float(rawdata[x][2])),last_get)}")
            assists[last_year].append(f"|{int(rawdata[x][0]):,}| [/u/{gen_assist_user_string(rawdata[x-1][1])}](https://www.reddit.com/r/counting/comments/{rawdata[x-1][4]}/_/{rawdata[x-1][3]}/?context=3)|")
            last_get = int(float(rawdata[x][2]))
    except:
        print(f"Error: {rawdata[x][0]}")
        pass


with open("results/hall_of_fame.txt","w") as f:
    top_10 = [[x, get_users[x]] for x in get_users]
    top_10.sort(key=lambda x:x[1],reverse=True)
    f.write("###Leaderboard:\n")
    f.write("| Rank   | Username    | # of gets |\n")
    f.write("|:-----------:|:------------:|:------------:|\n")
    for x in range(10):
        f.write(f"{x+1} | /u/{top_10[x][0]} | {top_10[x][1]}\n")

    for year in gets:
        f.write(f"**{year}**\n\n")
        f.write("| Get | Getter | Date and time | Time from previous 1,000 |\n")
        f.write("|:-----------|:------------|:------------|:------------|\n")
        for k in gets[year]:
            f.write(f"{k}\n")

with open("results/hall_of_999s.txt","w") as f:
    top_10 = [[x, assist_users[x]] for x in assist_users]
    top_10.sort(key=lambda x:x[1],reverse=True)
    f.write("###Leaderboard:\n")
    f.write("| Rank   | Username    | # of 999s |\n")
    f.write("|:-----------:|:------------:|:------------:|\n")
    for x in range(10):
        f.write(f"{x+1} | /u/{top_10[x][0]} | {top_10[x][1]}\n")
    for year in assists:
        f.write(f"**{year}**\n\n")
        f.write("| Get assisted | Username |\n")
        f.write(":---|:---\n")
        for k in assists[year]:
            f.write(f"{k}\n")
