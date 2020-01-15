for i in range(0,int(input())):
    x = input()
    c1=x.count("SUVOJIT")
    y = x.replace("SUVOJIT","")
    c2=y.count("SUVO")
    print('SUVO = '+str(c2)+', SUVOJIT = '+str(c1))
