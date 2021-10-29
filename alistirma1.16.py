# kullanıcı tarafından girilen sayının asal olup olmadığını belirleyen program

sayı=int(input("Bir sayı giriniz:"))

if sayı>1:
       for bölen in range(2,sayı):
              if (sayı%bölen)==0:
                   print("ASAL SAYI DEĞİL!")
                   break
       else:
              print("ASAL SAYI!")
               
