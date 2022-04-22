szotar = {

}

f = open("szavak.txt")



for line in f:
    kezdo = line[0]
    if kezdo in szotar.keys():
        szotar[kezdo] += 1
    else:
        szotar[kezdo] = 1




f.close()
print(szotar)







hany_szo = {}


f = open("feladat.txt")

for line in f:
    #print(line.split(" "))
    for szo in line.split(" "):
        #print(szo)
        kezdo = szo
        if kezdo in hany_szo.keys():
            hany_szo[kezdo] += 1
        else:
            hany_szo[kezdo] = 1    



f.close()
print(hany_szo)



'''
bekeres = input('Kérek egy betut: ').lower().strip()

darab = 0

for line in f:
    if line[0] == bekeres[0]:
        darab += 1

print(darab)
'''











































