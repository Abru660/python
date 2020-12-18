file = open("nameslist.txt","r")

cpt = 0

for line in file:
    cpt+=1
    
print("number of lines : " + str(cpt))

file.close()