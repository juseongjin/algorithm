#include <bits/stdc++.h>

using namespace std;

int n;
long long pose, crossroads, max_dst=0;

int main(){
    cin >> n;
    vector<pair<long long, long long>> info;
    int result = 1;
    for(int i=0;i<n;i++){
            cin >> pose;
            info.push_back({pose,0});
        }
    if(n>1){
        for(int i=0; i<n-1; i++){
            cin >> crossroads;
            if(info[i].first+crossroads > max_dst) max_dst = info[i].first+crossroads;
            if(max_dst < info[i+1].first) result = 0;
        }
    }
    if(result || n==1) cout << "권병장님, 중대장님이 찾으십니다" << endl;
    else cout << "엄마 나 전역 늦어질 것 같아" << endl;
    
    

    return 0;
}