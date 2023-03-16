import csv

rawdata = []
with open("decimal_log.csv","r") as file:
    reader = csv.reader(file)

    for row in reader:
        rawdata.append(row)
print("loaded")

def add_data(to_dict,i,start,change):
    if i not in to_dict:
        to_dict[i] = [start, change]
    else:
        to_dict[i][1] = to_dict[i][1] + change

users = {}
temp = {}
k = {}
for x in range(1,len(rawdata)-1):
    try:
        if int(rawdata[x][0]) % 1000 == 0:
            for y in k:
                add_data(temp,y,int(k[y][0]),1)
            k = {}
        if int(rawdata[x][0]) % 100000 == 0:
            print(rawdata[x][0])
            for y in temp:
                add_data(users,y,temp[y][0],temp[y][1])
            temp = {}
        if rawdata[x][1] not in k:
            add_data(k,rawdata[x][1],int(rawdata[x][0])//1000,1)
    except:
        pass

last = int(rawdata[-1][0]) // 1000

for y in k:
    add_data(temp,y,int(k[y][0]),1)
for y in temp:
    add_data(users,y,temp[y][0],temp[y][1])
s_d = []
for y in users:
    if users[y][1] > 25:
        s_d.append([y, users[y][0],users[y][1],100*users[y][1]/(last-users[y][0])])


s_d.sort(key=lambda x:x[3],reverse=True)

with open("results/threads_participated_since_join.txt","w") as f:
    f.write("Rank|User|First thread|Participation|Percentage\n")
    print("Rank|User|First thread|Participation|Percentage")
    f.write(":-:|:-:|:-:|:-:|:-\n")
    print(":-:|:-:|:-:|:-:|-:")
    for x in range(len(s_d)):
        f.write(f"{str(x+1)} | {s_d[x][0]} | {s_d[x][1]} | {s_d[x][2]} | {s_d[x][3]:.2f}%\n")
        print(f"{str(x+1)} | {s_d[x][0]} | {s_d[x][1]} | {s_d[x][2]} | {s_d[x][3]:.2f}%")
    f.write(f"^Stats ^to ^{last}k")
    print(f"^Stats ^to ^{last}k")