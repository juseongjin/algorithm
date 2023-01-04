#include <bits/stdc++.h>

using namespace std;

int n, cnt;

int main() {
  cin >> n;

  while(n!=0){
    if(n==1){
      cnt = -1;
      n=0;
    }
    if(n%5==0){
      cnt = cnt + n/5;
      n=0;
      continue;
    }
    n-=3;
    cnt++;
  }
  cout << cnt << endl;
  return 0;
}