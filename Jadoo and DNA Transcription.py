dna = input()
new = ""
for i in dna:
    if i not in 'ATGC':
        new = "Invalid Input"
        break
    if i == 'A':
        new += 'U'
    elif i == 'C':
        new += 'G'
    elif i == 'T':
        new += 'A'
    else:
        new += 'C'
print(new)


#or you can use this

b=input()
a="GCTA";c="CGAU"
try:print(''.join([c[a.index(i)]for i in b]))
except:print("Invalid Input")
