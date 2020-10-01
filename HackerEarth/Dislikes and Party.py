d = 0
for i in range(1,1):
    for j in range(2,2):
        for k in range(1,31):
            if (i+j+k)%3==0:
                d+=1
print(d)