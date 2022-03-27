class Solution {
public:
    int twoCitySchedCost(vector<vector<int>>& costs) {
        // answer is to send every person to the CityA and then according to the 
        // difference between CityB-CityA send half of the people to CityB
        int total = 0;
        vector<int> diff;
        
        for(int i=0;i<costs.size();i++){
            total += costs[i][0];
            diff.push_back(costs[i][1]-costs[i][0]);
        }
        
        sort(diff.begin(),diff.end());
        
        for(int i=0;i<costs.size()/2;i++){
            total += diff[i];
        }
        
        return total;
    }
};