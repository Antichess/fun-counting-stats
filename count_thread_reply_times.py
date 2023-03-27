import csv

rawdata = []
with open("LOG_5035001to5036000.csv","r") as file:
    reader = csv.reader(file)

    for row in reader:
        rawdata.append(row)

alts = []
with open("../input/prefs/Aliases.txt","r") as f:
    alts = f.read()

alts = alts.split("\n")
alts = [x.split(",") for x in alts]


def alt(user):
    for x in alts:
        if x[0] == user:
            return user
        if user in x[1::]:
            return x[0]
    return user

def get_time(d):
    if d < 60:
        return f"{d%60}s "
    if d < 3600:
        return f"{d//60}m {d%60}s "
    else:
        return f"{d//3600}h {d%3600//60}m {d%3600%60}s "
            
userstats = []
for i in range(len(rawdata)-1):
    found = False
    append = []
    for x in userstats:
        if x[0] == alt(rawdata[i+1][1]):
            if x[1] == (int(float(rawdata[i+1][2])) - int(float(rawdata[i][2]))):                
                found = True
                break
    if found is False:
        append = (alt(rawdata[i+1][1]),(int(float(rawdata[i+1][2])) - int(float(rawdata[i][2]))),1)
        userstats.append(append)
    else: #if found is true
        for j in range(len(userstats)):
            if (userstats[j][0] == alt(rawdata[i+1][1])):
                if (userstats[j][1] == (int(float(rawdata[i+1][2])) - int(float(rawdata[i][2])))):
                     temp = list(userstats[j])
                     temp[2] = temp[2] + 1
                     userstats[j] = temp

unique_names = []
user_sums = []
timemax = 0
for x in userstats:

    if x[0] not in unique_names:
        unique_names.append(x[0])

print("Username|Speed|Counts")
print("---|---|---")

for y in unique_names:
    s = 0
    times = []
    for x in userstats:
        if y == x[0]:
            times.append(x[1])
            s = s + (x[1] * x[2])
        times.sort()
    append = (y,s)
    user_sums.append(append)


    for t in times:
        for x in userstats:
            if y == x[0] and t == x[1] and x[2] != 0:
                print(str(alt(x[0])) + " | " + get_time(t) + "| " + str(x[2]))
                break


print()
print("Username|Reply time sum")
print("---|---")

user_sums.sort(key = lambda x: x[1],reverse=True)
for x in user_sums[0:2]:
    
    print(alt(x[0]) + " | " + get_time(x[1]))
