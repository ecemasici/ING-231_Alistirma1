# 4 basamaklı tam sayılardan ilk rakamı son rakamından büyük olanları yazdıran program
sayı=range(1000,10000)
for a in sayı:
    a=str(a)
    if a[0]>a[3]:
        print(a)
