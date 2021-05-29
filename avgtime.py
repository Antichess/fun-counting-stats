import csv


rawdata = []
with open("ALL.csv","r") as file:
    reader = csv.reader(file)

    for row in reader:
        rawdata.append(row)

def add_data(users,user,c,s):
    found = False
    for x in range(len(users)):
        if user in users[x]:
            users[x] = (user, (users[x][1]+c), (users[x][2]+s))
            found = True
            break
    if not found:
        append = (user, 1, s)
        users.append(append)
        
users = []
temp = []

for x in range(1,len(rawdata)-1):
    try:
        #print(int(float(rawdata[x+1][2]))-int(float(rawdata[x][2])))
        add_data(temp,rawdata[x][1],1,(int(float(rawdata[x+1][2]))-int(float(rawdata[x][2]))))
        if (int(float(rawdata[x][0])) % 10000) == 0:
            for y in range(len(temp)):
                add_data(users,temp[y][0],temp[y][1],temp[y][2])
            
            users.sort(key=lambda x:x[1],reverse=True)
            #print(temp)
            #print(len(users))
            temp.clear()
            #sort so it will be slightly faster. improved times drastically for me
            print(int(float(rawdata[x][0])))
    except:
        pass
#users.sort(key=lambda x:x[1],reverse=True)

sorted_data = []
for x in range(len(users)):
    if users[x][1] > 499:
        append = (users[x][0], round(users[x][2]/users[x][1],4))
        sorted_data.append(append)

sorted_data.sort(key=lambda x:x[1])


print("Rank|User|Avg reply time")
print(":-:|:-:|:-:")
for x in range(len(sorted_data)):
    print(str(x+1) + "|"  + sorted_data[x][0] + "|" + str(sorted_data[x][1]))
