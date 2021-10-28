#doğduğu yılın rakamları toplamı ile 2005 yılındaki yaşı aynı olan kişinin hangi yıl doğduğunu bulan program

for yıl in range(1000,2005):
    yıl=str(yıl)
    if int(yıl[0])+int(yıl[1])+int(yıl[2])+int(yıl[3])==2005-int(yıl):
        print(yıl)

