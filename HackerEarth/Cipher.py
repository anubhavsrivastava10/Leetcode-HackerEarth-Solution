n=list(input())
k=int(input())
a=len(n)
result=""
for i in range(a):
    char=n[i]
    if (char.isupper()):
        result += chr(( ord(n[i]) -65 + k ) % 26 + 65 )
    elif (char.islower()):
        result += chr(( ord(n[i]) -97 + k ) % 26 + 97)
    elif (char.isdigit()):
        result += chr(( ord(n[i]) - 48 + k) % 10 + 48)
    else:
        result += n[i]
print(result)
