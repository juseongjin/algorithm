#include <bits/stdc++.h>

using namespace std;

int t, n, tmp, cnt;

int main(){
    cin >> t;
    for(int i=0; i<t; i++){
        cin >> n;
        cnt = 0;
        vector<pair<int, int>> score;
        for(int j=0; j<n; j++){
            int doc, interview;
            cin >> doc >> interview;
            score.push_back({doc, interview});
        }
        sort(score.begin(), score.end());
        
        int tmp = score[0].second;
        cnt++;
        for(int k=1; k<score.size(); k++){
            if(tmp>=score[k].second){
                cnt++;
                tmp = score[k].second;
            }
        }
        cout << cnt << endl;
    }
    
    return 0;
}