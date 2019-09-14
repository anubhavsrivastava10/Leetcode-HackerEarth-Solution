#include <bits/stdc++.h>
using namespace std;
const int maxn = 2;
int t, n, cost[maxn], used[maxn], ph[maxn], pu[maxn], ans[maxn];
int main(){
	ios::sync_with_stdio(0), cin.tie(0);
	cin >> t;
	while(t--){
		used[0] = used[1] = 0;
		for(int i = 0; i < maxn; i++)
			cin >> cost[i];
		cin >> n;
		for(int i = 0; i < n; i++)
			for(int j = 0; j < maxn; j++){
				int x;
				cin >> x;
				used[j] += x;
			}
		cout << min(cost[0] * used[0] + cost[1] * used[1], cost[1] * used[0] + cost[0] * used[1]) << '\n';
	}
}
