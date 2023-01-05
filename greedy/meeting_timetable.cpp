#include <bits/stdc++.h>

using namespace std;

int n, cnt=1;
vector<pair<int,int>> plan;

int main(){
    cin >> n;
    for(int i=0; i<n; i++){
        int start, end;
        cin >> start >> end;
        plan.push_back({end, start});
    }
    sort(plan.begin(), plan.end());
    
    int tmp = plan[0].first;

    for(int i=1; i<plan.size(); i++){
        if(plan[i].second>=tmp){
            cnt++;
            tmp = plan[i].first;
        }
    }
    cout << cnt << endl;
    return 0;
}