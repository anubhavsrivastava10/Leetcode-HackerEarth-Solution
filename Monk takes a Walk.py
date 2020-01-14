lst1 = ['a','e','i','o','u','A','E','I','O','U']
for i in range(0,int(input())):
    counter = 0
    x = input()
    for item in x:
        if item in lst1:
            counter = counter+1
    print(counter)
