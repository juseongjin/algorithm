#include <bits/stdc++.h>

using namespace std;

bool visited[101][101];
char graph[101][101];
int n, m;
int dx[4]={-1,1,0,0};
int dy[4]={0,0,-1,1};
int tmp[2]={1,1};

void dfs(int x, int y){
    visited[x][y]=true;
    for(int i=0; i<4; i++){
        int nx = x+dx[i];
        int ny = y+dy[i];
        if(nx>=0 && ny>=0 && nx<=100 && ny<=100){
            if(!visited[nx][ny] && graph[nx][ny]=='W' && graph[x][y]=='W'){
                tmp[0]+=1;
                dfs(nx,ny);
            }
            else if(!visited[nx][ny] && graph[nx][ny]=='B' && graph[x][y]=='B'){
                tmp[1]+=1;
                dfs(nx,ny);
            }
            nx -= dx[i];
            ny -= dy[i];
        }
    }
}

int main(){
    int W_result=0, B_result=0;
    cin >> n >> m;
    for(int i=0; i<m; i++){
        for(int j=0; j<n; j++){
            scanf("%1s", &graph[i][j]);
        }
    }

    for(int i=0; i<m; i++){
        for(int j=0; j<n; j++){
            if(!visited[i][j] && graph[i][j]=='W'){
                dfs(i,j);
                W_result += pow(tmp[0],2);
                tmp[0] = 1;
            }
            else if(!visited[i][j] && graph[i][j]=='B'){
                dfs(i,j);
                B_result += pow(tmp[1],2);
                tmp[1] = 1;
            }
        }
    }
    cout << W_result << " " << B_result << endl;
    return 0;
}