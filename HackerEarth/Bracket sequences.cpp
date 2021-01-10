#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
 
const int maxn = 3e2 + 14;
string s;
int main()
{
    ios::sync_with_stdio(0), cin.tie(0);
    cin >> s;
    map<int, int> mp;
    int su = 0;
    for(auto c : s){
        su += (c == '(' ? +1 : -1);
        mp[su]++;
    }
    cout << (su == 0) * mp.begin() -> second << '\n';
}