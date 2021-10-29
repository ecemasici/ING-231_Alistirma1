liste=[]
a=121211
for sayı1 in range(1,121213):
    for sayı2 in range(1,121213):
        if sayı1*sayı2==121212:
            if abs(sayı1-sayı2)<a:
                a=abs(sayı1-sayı2)
                liste.clear()
                liste.append([sayı1,sayı2])
print(liste)
                




    
