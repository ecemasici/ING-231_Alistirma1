
# 5 basamaklı tüm asal sayıları bulup ekrana basan program
for i in range(10000,100000):
    for k in range(2,i):
        if(i%k)==0:
            break
    else:
        print(i)
    

            

