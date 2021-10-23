toplam=0
sayı=range(1,1000000)
for n in sayı:
    toplam=toplam+(1/n**2)
print("pi yaklaşık değeri",(toplam*6)**0.5)
    

