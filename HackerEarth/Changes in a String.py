for _ in range(int(input())):
    x = int(input())
    p = list(input())
    # if the string is full of A's or B's
    if p.count('A')==x or p.count('B')==x:
        print(0)
    else:
        for i in range(x):















        # for i in range(x):
        #     if p[i]=='A':
        #         z=i
        # c=0
        # k=0
        # if p[:z].count('A')<=p[:z].count('B'):
        #     c+=p[:z+1].count('A')
        #     k=1
        # else:
        #     c+=p[:z+1].count('B')
        # # print(c)
        # if k==1:
        #     c+=p[z+1:].count('A')
        # else:
        #     if p[z+1:].count('A')<=p[z+1:].count('B'):
        #         c+=p[z+1:].count('A')
        #     else:
        #         c+=p[z+1:].count('B')
        # print(c)
# Aababbaaabbabb
#
# A=AABBAABBABAB
# count = 0
# for i in range A:
#     if  i ==A:
#          count+=1
# B='A' * count + 'B' * (len-count)
# c=0
# for i in range(len(A) :
#      if A[i] ! = B[i] :
#        c+=1
# print(c)