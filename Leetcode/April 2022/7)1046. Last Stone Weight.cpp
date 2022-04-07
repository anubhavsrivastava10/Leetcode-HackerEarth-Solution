class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        priority_queue<int> g;
        for(auto item: stones){
            g.push(item);
        }
        while(g.size()>1){
            int first = g.top();
            g.pop();
            int second = g.top();
            g.pop();
            if(first==second){
                g.push(0);
                continue;
            }
            else{
                g.push(abs(first-second));
            }
        }
        return g.top();
        
    }
};