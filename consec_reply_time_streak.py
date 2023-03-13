import csv

rawdata = []
with open("decimal_log.csv","r") as file:
    reader = csv.reader(file)

    for row in reader:
        rawdata.append(row)
print("loaded")

users = {}
e_o = [0,0] # even odd
         # even is 0 odd is 1
index = 0

for x in range(4,len(rawdata)-1):
    if x % 100000 == 0:
        print(x)
    try:
        index = int(rawdata[x][0]) % 2
        

        if (int(float(rawdata[x][2]))-int(float(rawdata[x-1][2]))) == (int(float(rawdata[x-2][2]))-int(float(rawdata[x-3][2]))):
            if rawdata[x][1] == rawdata[x-2][1]:
                if e_o[index] == 0:
                    e_o[index] = [rawdata[x][1], 2, int(float(rawdata[x-2][2]))-int(float(rawdata[x-3][2])), rawdata[x][4], rawdata[x-2][3], rawdata[x][3], rawdata[x-2][0], rawdata[x][0]]
                else:
                    if int(float(rawdata[x-2][2]))-int(float(rawdata[x-3][2])) == e_o[index][2]:
                        e_o[index][1] = e_o[index][1] + 1
                        e_o[index][5] = rawdata[x][3]
                        e_o[index][7] = rawdata[x][0]
                    else:
                        e_o[index] = 0
        else:
            if e_o[index] != 0:
                if int(float(rawdata[x][2]))-int(float(rawdata[x-1][2])) != e_o[index][2]:
                    if e_o[index][0] not in users:
                        users[e_o[index][0]] = e_o[index]
                    else:
                        if users[e_o[index][0]][1] < e_o[index][1]:
                            users[e_o[index][0]] = e_o[index]
                    e_o[index] = 0
                

    except:
        pass


s_d = []
for x in users:
    if users[x][1] > 4:
        s_d.append(users[x])
s_d.sort(key=lambda x:x[1],reverse=True)
print(s_d)



with open("results/consec_reply_times_streak.txt","w") as f:
    f.write("Rank|User|Counts|Streak\n")
    print("Rank|User|Counts|Streak")
    f.write(":-:|:-:|:-:|:-:\n")
    print(":-:|:-:|:-:|:-:")
    for c,x in enumerate(s_d):
        f.write(f"{c+1}|{x[0]}|[{x[6]}](https://www.reddit.com/r/counting/comments/{x[3]}/_/{x[4]}/)-[{x[7]}](https://www.reddit.com/r/counting/comments/{x[3]}/_/{x[5]}/)|{x[1]} streak of {x[2]}s\n")
        print(f"{c+1}|{x[0]}|[{x[6]}](https://www.reddit.com/r/counting/comments/{x[3]}/_/{x[4]}/)-[{x[7]}](https://www.reddit.com/r/counting/comments/{x[3]}/_/{x[5]}/)|{x[1]} streak of {x[2]}s")

