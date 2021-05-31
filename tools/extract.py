f = open("extract.txt","r")
for x in f:
    link = x.split("|")[2].split("(")[1].split(")")[0].replace("?","/?")
    print(link)
