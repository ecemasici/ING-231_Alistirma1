#kullanıcının girdiği 3 veya 4 basamaklı sayının palindromik olup olmadığını kontrol eden program
sayı=input("Lütfen bir sayı giriniz:")
if len(sayı)==3 and sayı[0]==sayı[2]:
    print("Sayı palindromiktir!")

elif len(sayı)==4 and sayı[0]==sayı[3] and sayı[1]==sayı[2]:
    print("Sayı palindromiktir!")

else:
    print("Sayı palindromik değildir!")
         
         
