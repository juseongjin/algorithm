#include <bits/stdc++.h>

using namespace std;

int n,m;
bool visited[101][101];
int check[101][101]; //미로를 지나면서 현재 위치 까지의 거리 => 최단경로를 위하여
int mymap[101][101];
int dx[] = {-1,1,0,0};
int dy[] = {0,0,1,-1};

void find(int x, int y){
    queue<pair<int,int>> que;
    que.push({x,y});
    
    visited[x][y]=true;

    while(!que.empty()){
        int x = que.front().first;
        int y = que.front().second;
        que.pop();
        for(int i=0; i<4; i++){
            int nx = x + dx[i];
            int ny = y + dy[i];
            if(nx>=0 && ny>=0 && ny<=100 && nx<=100){
                if(!visited[nx][ny] && mymap[nx][ny]==1){
                    que.push({nx,ny});
                    visited[nx][ny]= true;
                    check[nx][ny] = check[x][y]+1;
                }
            }
        }
    }
}


int main(){
    cin >> n >> m;
    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++) scanf("%1d", &mymap[i][j]);
    }
    find(0,0);
    cout << check[n-1][m-1]+1 << endl;
    return 0;
}