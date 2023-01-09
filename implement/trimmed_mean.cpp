#include <bits/stdc++.h>

using namespace std;

int n, k;

int main(){
    cin >> n >> k;
    double score[n];
    double tmp[n], sum, result1, result2;

    //결과가 5인 경우 5.00으로 출력해줘야함
    cout<<fixed;
    cout.precision(2);

    for(int i=0; i<n; i++){
        cin >> score[i];
    }

    sort(score, score+n);
    //절사평균
    for(int i=k; i<n-k; i++){
        sum += score[i];
    }
    result1 = sum/(n-2*k);

    sum =0;
    //보정평균
    for(int i=0; i<n; i++){
        if(i<k) score[i] = score[k];
        else if(i>=n-k) score[i] = score[n-k-1];
        sum+=score[i];
    }
    result2 = sum/n;
    
    cout << round(result1 * 100)/100 << endl;
    cout << round(result2 * 100)/100 << endl;
    return 0;
}