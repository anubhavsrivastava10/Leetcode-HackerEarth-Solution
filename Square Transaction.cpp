#include <bits/stdc++.h>
using namespace std;

int main()
{
int t;
cin>>t;
int ar[t];
for(int i=0;i<t;i++)
{
    cin>>ar[i];
}
int q;
cin>>q;
while(q!=0)
{
    int a;
    int sum=0;
    cin>>a;
    for(int i=0;i<t;i++)
    {
        sum=sum+ar[i];
        if(sum>=a)
        {
            cout<<i+1<<"\n";
            break;
        }
    }
    if(sum<a)
    {
        cout<<"-1\n";
    }
    q--;
}
return 0;
}

/*

-----------------------------Python solution----------------------------------
######################It will show error on the 5th test case TLE

N = int(input())
lst = list(map(int,input().split()))
for i in range(0,int(input())):
    add = 0
    A = int(input())
    for j in range(0,N):
        add = add + lst[j]
        if add >= A:
            print(j+1)
            break
    if add < A:
        print('-1')
        
*/
