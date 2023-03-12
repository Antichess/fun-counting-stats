import csv

rawdata = []
with open("LOG_4980001to4981000.csv","r") as file:
    reader = csv.reader(file)

    for row in reader:
        rawdata.append(row)
   
def get_times(x):
    seconds = x
    leftover = seconds % 86400
    seconds -= leftover
    days = seconds / 86400
    seconds = leftover
    leftover = seconds % 3600
    seconds -= leftover
    hours = seconds / 3600
    seconds = leftover
    leftover = seconds % 60
    seconds -= leftover
    mins = seconds / 60
    seconds = leftover
    timestr = ""
    if days > 0:
        timestr = timestr + str(int(days)) + "d "
    if hours > 0:
        timestr = timestr + str(int(hours)) + "h "
    if mins > 0:
        timestr = timestr + str(int(mins)) + "m "
    timestr = timestr + str(int(seconds)) + "s "
    return timestr
    


userstats = []
for i in range(len(rawdata)-1):
    found = False
    append = []
    for x in userstats:
        if x[0] == rawdata[i+1][1]:
            if x[1] == (int(float(rawdata[i+1][2])) - int(float(rawdata[i][2]))):                
                found = True
                break
    if found is False:
        append = (rawdata[i+1][1],(int(float(rawdata[i+1][2])) - int(float(rawdata[i][2]))),1)
        userstats.append(append)
    else: #if found is true
        for j in range(len(userstats)):
            if (userstats[j][0] == rawdata[i+1][1]):
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
                print(str(x[0]) + " | " + get_times(t) + "| " + str(x[2]))
                break


print()
print("Username|Reply time sum")
print("---|---")

user_sums.sort(key = lambda x: x[1])
for x in user_sums:
    
    print(x[0] + " | " + get_times(x[1]))
