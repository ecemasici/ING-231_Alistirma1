# 5 basamaklı tam sayılardan kaç adedinin ilk iki rakamı ile son iki rakamının eşit olduğunu veren program
sayı=range(10000,100000)
adet=0
for a in sayı:
    a=str(a)
    if a[0]==a[4] and a[3]==a[1]:
        adet+=1
print(adet)
