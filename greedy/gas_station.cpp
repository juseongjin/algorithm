#include <bits/stdc++.h>

using namespace std;

int n;

int main(){
    cin >> n;
    long long int price[n], dst[n-1], result;

    for(int i=0; i<n-1; i++){
        int x;
        cin >> x;
        dst[i] = x;
    }
    for(int j=0; j<n;j++){
        int y;
        cin >> y;
        price[j] = y;
    }
    result += dst[0]*price[0];
    int tmp = price[0];
    for(int k=1; k<n-1; k++){
        if(tmp<=price[k])result+=tmp*dst[k];
        else {
            tmp = price[k];
            result += tmp*dst[k];
        }
    }
    cout << result << endl;

    return 0;
}