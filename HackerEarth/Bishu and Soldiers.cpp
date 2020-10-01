#include<bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin>>n;
    int A[n];
    for(int i=0;i<n;i++)
        cin>>A[i];
    int q,r,count,sum;
    cin>>q;
    while(q--)
    {
        count = 0;
        sum = 0;
        cin>>r;
        for(int i=0;i<n;i++)
        {
            if(A[i]<=r)
            {
                count = count + 1;
                sum = sum + A[i];
            }
        }
        cout<<count<<" "<<sum<<endl;
    }
}
