import csv

def get_time_diff(time):
    d = time
    if d < 3600:
        return f"{d//60}m {d%60}s"
    
    else:           
        if d > 84600:
            return f"{d//86400}d {d%86400//3600}h {d%86400%3600//60}m"
        else:
            return f"{d//3600}h {d%3600//60}m"

rawdata = []
with open("decimal_log.csv","r") as file:
    reader = csv.reader(file)
    for row in reader:
        rawdata.append(row)
print("loaded")

user = "The_NecromancerTin"

with open(f"results/all_counts_with/{user}.csv","w") as f:
    fw = csv.writer(f, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL,lineterminator='\n')
    try:
        for x in range(1,len(rawdata)-1):
            if rawdata[x][1] == user:
                fw.writerow([rawdata[x][0],rawdata[x-1][1],get_time_diff(int(float(rawdata[x][2]))-int(float(rawdata[x-1][2]))),f"https://www.reddit.com/r/counting/comments/{rawdata[x][4]}/_/{rawdata[x][3]}/"])
            if x % 100000 == 0:
                print(x)
    except:
        pass
