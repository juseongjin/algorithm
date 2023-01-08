#include <bits/stdc++.h>

using namespace std;

long long n, k, t;

int main(){
    cin >> n >> k >> t;
    long long sum=0, cnt=0;
    long long a[100001]={0,};
    for(int i=0; i<n; i++){
        cin >> a[i];
        sum += a[i];
    }
    sort(a, a+n);
    
    if(sum%k!=0) cout << "NO" << endl;
    else{
        for(int j=0; j<sum/k; j++){ // sum/k는 가득 채워질 바구니 개수
            cnt+=k-a[n-1-j]; // 뒤에서 부터 채우는 게 최소한으로 이동시키는 방법
        }
        if(cnt<=t) cout << "YES" << endl;
        else cout << "NO" << endl;
    }
    return 0;
}