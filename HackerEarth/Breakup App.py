s = [0] * 2
dates=[]
for i in range(int(input())):
    text = input()
    for c in text.split():
        if c.isdigit():
            dates.append(int(c))
    for n in dates:
        if n in [19,20]:
            if text[0] == 'G':
                s[0] = s[0] + 2 
            else:
                s[0] = s[0] + 1
        else:
            if text[0] == 'M':
                s[1] = s[1] + 2 
            else:
                s[1] = s[1] + 1
if s[0] > s[1]:
    print('Date')
else:
    print("No Date")
    
