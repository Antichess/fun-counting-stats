import csv

rawdata = []
with open("decimal_log.csv","r") as file:
    reader = csv.reader(file)

    for row in reader:
        rawdata.append(row)
print("loaded")

def new_1000_list():
    return [0 for x in range(1001)]

def find_max(user_data):
    max = [0]
    min = [0]
    for c in range(len(user_data)-1):
        x = user_data[c]
        if all(x > user_data[y] for y in max):
            max = [c]
        elif all(x == user_data[y] for y in max):
            max.append(c)
        elif all(x < user_data[y] for y in min):
            min = [c]
        elif all(x == user_data[y] for y in min):
            min.append(c)
    return [max,min]

def string(list):
    ret = ""
    for x in list:
        if x != list[-1]:
            ret = ret + f"{x}, "
        else:
            ret = ret + f"{x}"
    return ret

d = {}

for x in range(len(rawdata)):
    if x % 100000 == 0:
        print(x)
    try:
        if rawdata[x][1] not in d:
            d[rawdata[x][1]] = new_1000_list()
            d[rawdata[x][1]][int(rawdata[x][0]) % 1000] = 1
            d[rawdata[x][1]][1000] = 1
        else:
            d[rawdata[x][1]][int(rawdata[x][0]) % 1000] = d[rawdata[x][1]][int(rawdata[x][0]) % 1000] + 1
            d[rawdata[x][1]][1000] = d[rawdata[x][1]][1000] + 1
    except:
        pass

d_list = [[x, d[x]] for x in d if d[x][1000] > 5000]
d_list.sort(key=lambda x:x[1][1000],reverse=True)


with open("results/most_least_counted_number.txt","w") as fw:
    print(f"Rank|Username|Most counted #|Freq|Least counted #|Min freq")
    fw.write(f"Rank|Username|Most counted #|Freq|Least counted #|Min freq\n")
    print(f":-:|:-:|:-:|:-:|:-:|:-:")
    fw.write(f":-:|:-:|:-:|:-:|:-:|:-:\n")
    for c,x in enumerate(d_list):
        f = find_max(x[1])
        fw.write(f"{c+1} | {x[0]} | {string(f[0])} | {x[1][f[0][0]]}x | {string(f[1])} | {x[1][f[1][0]]}x\n")
        print(f"{c+1} | {x[0]} | {string(f[0])} | {x[1][f[0][0]]}x | {string(f[1])} | {x[1][f[1][0]]}x")