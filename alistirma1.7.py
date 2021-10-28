# 3 basamaklı tam sayılardan kaç tanesinin ilk iki rakamının toplamının son rakamına eşit olduğunu bulup onları ekrana yazdıran program
sayı=range(100,1000)
adet=0
for a in sayı:
    a=str(a)
    if int(a[0])+int(a[1])==int(a[2]):
        print(a)
        adet+=1
print(adet)
  
