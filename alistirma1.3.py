# e sayısının yaklaşık değerini hesaplama
sonsuz=100

toplam=0
for sayı in range(0,sonsuz):
    f=1
    for x in range(2,sayı+1):
        f*= x 
    toplam+=(1/f)

print("e'nin değeri=",toplam)

    
