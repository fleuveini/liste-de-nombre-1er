import json
import time

start=time.time()

chemin="C:\\Users\\rapha\\OneDrive\\Bureau\\code\\nombre 1er\\nombre 1er.json"
with open (chemin,"r") as f:
    listenb1er=json.load(f)

nbtester=1
diviseur=1
test=0
nb_facteurs=0
nb_de_nb1er=0

if len(listenb1er)>2:
        nbtester=max(listenb1er)

for loop in range(100):
    
    while diviseur <= nbtester:
        test=nbtester/diviseur
        diviseur+=1
        if test==int(test):
            nb_facteurs+=1
            
    if nb_facteurs==2:
        print(nbtester ,"est bien un nombre 1er")#nbtester
        listenb1er.append(nbtester)
        nb_de_nb1er+=1
        
    nbtester+=1
    diviseur=1
    nb_facteurs=0
    
    with open(chemin, "w") as f:
            json.dump(listenb1er, f, indent=4)

print(time.time()-start)

