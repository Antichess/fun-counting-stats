import csv


rawdata = []
with open("decimal_log.csv","r") as file:
    reader = csv.reader(file)

    for row in reader:
        rawdata.append(row)

print("loaded")

d = {}
user = "ClockButTakeOutTheL"
diff = 1

for c,x in enumerate(rawdata):
    try:
        if x[1] == user:
            t = int(float(rawdata[c][2]))-int(float(rawdata[c-1][2]))
            if t > 15:
                t = 15
            if t not in d:
                d[t] = 1
            else:
                d[t] = d[t] + 1
            
    except:
        pass

k = sorted(d.keys())
s_d = [[key,d[key]] for key in k]
print(s_d)
print("Reply time (s)|Count")
print(":-|:-")
for x in s_d:
    print(f"{x[0]}|{x[1]}")
