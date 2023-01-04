#include <bits/stdc++.h>

using namespace std;

int n, p[1000]={0,};

int main(){
    cin >> n;
    
    for(int i=0; i<n; i++){
        cin >> p[i];
    }
    sort(p,p+1000);
    int tmp=0, result=0;
    for(int i=0; i<1000; i++){
        tmp += p[i];
        result += tmp;
    }
    cout << result << endl;
    return 0;
}