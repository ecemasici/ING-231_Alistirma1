
# 3 rakamlı çift sayılar arasında en az 2 rakamı aynı olan kaç sayı olduğunu bulan program
sayı=range(100,1000,2)
adet=0
for a in sayı:
    a=str(a)
    if a[0]==a[1] or a[0]==a[2] or a[2]==a[1]:
        adet+=1
print(adet)


