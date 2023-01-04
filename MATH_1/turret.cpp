#include <bits/stdc++.h>

using namespace std;

// -10000 <= x,y  <= 10000
// r <= 10000


int main(){
    int t, n=0;
    int x1,y1,r1,x2,y2,r2;
    cin >> t;
    int d;
    // 원 방정식의 교점 개수, 원의 중점과 거리가 같으면 무한대 -1
    
    while(n<t){
        cin >> x1 >> y1 >> r1 >> x2 >> y2 >> r2;
        // sqrt를 사용하면 d의 값이 정수가 아닌 경우 값 비교시 문제 생길 수 있다.
        if((x1==x2) && (y1==y2) && (r1==r2)) cout << -1 << endl;
        else{
            d = pow(x1-x2,2) + pow(y1-y2,2);
            if(pow(r1+r2,2) > d && pow(r1-r2,2) < d) cout << 2 << endl;
            else if(pow(r1+r2,2)==d || pow(r1-r2,2)==d) cout << 1 << endl;
            else if(pow(r1+r2,2) < d || pow(r1-r2,2) > d) cout << 0 << endl;
        }
        n++;
    }

    return 0;
}