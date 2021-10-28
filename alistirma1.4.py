#3 basamaklı palindromik sayıları bulup ekrana yazdıran program
sayı=range(100,1000)
for a in sayı:
    a=str(a)
    if a[0]==a[2]:
        print(a)
