#include <bits/stdc++.h>

using namespace std;

const int INF=987654321;
int n,m, result, tmp1=INF, tmp2=INF;

int main(){
    cin >> n >> m;
    for(int i=0; i<m; i++){
        int x, y;
        cin >> x >> y;
        tmp1 = min(tmp1, x);
        tmp2 = min(tmp2, y);
    }
    if(tmp1>tmp2*6)result+=tmp2*n;
    else{
        result = min((n/6)*tmp1+tmp2*(n%6), ((n/6)+1)*tmp1);
    }
    cout << result << endl;
    return 0;
}
