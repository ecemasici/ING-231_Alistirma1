#1'den 999'a kadar tam sayılardan rakamları toplamı 9'dan küçük olan sayıları bulup yan yana yazdıran program
sayı=range(1,1000)
liste1=list()
for a in sayı:
    a=str(a)
    
    if len(a)==1:
        if int(a[0])<9:
         liste1.append(int(a))
        

    if len(a)==2:
        if int(a[0])+int(a[1])<9:
         liste1.append(int(a))
        
    if len(a)==3:
        if  int(a[0])+int(a[1])+int(a[2])<9:
         liste1.append(int(a))

for i in liste1:
    print(i, end=" ")
