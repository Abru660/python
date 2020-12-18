with open("happynumbers.txt", "r") as file1:
    with open("primenumbers.txt", "r") as file2:
        same = set(file1).intersection(file2)

#same.discard('\n') doesn't work ?
        
result = []

for e in same:
    result.append(int(e.rstrip('\n')))
    
result.sort()

print(result)

file1.close()
file2.close()