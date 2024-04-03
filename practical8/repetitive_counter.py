s=input("input your sequence here: ")
n=0       
for i in range(len(s)-6):
    temp=s[i:i+6]
    if temp=="GTGTGT" or temp=="GTCTGT":
        n+=1       
print(n)