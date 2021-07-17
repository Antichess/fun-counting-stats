import csv

rawdata = []
with open("comments.csv","r",encoding='UTF-8') as file:
    reader = csv.reader(file)
    for row in reader:
        rawdata.append(row)

print(len(rawdata))
with open('goodnight.csv', mode='w',  newline='') as writer:
    writer = csv.writer(writer, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for x in range(len(rawdata)):
        try:
            if "good night all" in rawdata[x][8].lower():
                writer.writerow([rawdata[x][0],rawdata[x][2].split(" ")[0],rawdata[x][2].split(" ")[1],rawdata[x][8]])
                #print(rawdata[x][0] + " " + rawdata[x][8])
        except:
            pass
