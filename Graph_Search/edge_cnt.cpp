#include <bits/stdc++.h>

using namespace std;

int n,m;

vector<int> arr[1001];
bool visited[1001];

void dfs(int x){
    visited[x]=true;

    for(int i=0; i<arr[x].size(); i++){
        int y = arr[x][i];
        if(!visited[y]){
            dfs(y);
        }
    }
}

//bfs
// int bfs(int x){
//     queue<int> que;
    
//     que.push(x);
//     visited[x]=true;

//     while(!que.empty()){
//         int tmp = que.front();
//         que.pop();
//         for(int i=0; i<arr[tmp].size(); i++){
//             if(!visited[arr[tmp][i]]){
//                 que.push(arr[tmp][i]);
//                 visited[arr[tmp][i]]=true;
             
//             }
//         }
//     }
// }

int main(){
    int cnt = 0;
    int x,y;
    cin >> n >> m;
    for(int i=0;i<m;i++){
        cin >> x >> y;
        arr[x].push_back(y);
        arr[y].push_back(x);
 
    }
    //bfs
    // for(int i=1; i<=n; i++){
    //     if(!visited[i]){
    //         bfs(i);
    //         cnt++;
    //     }
    // }
    // cout << cnt << endl;

    for(int i=1; i<=n; i++){
        if(!visited[i]){
            dfs(i);
            cnt++;
        }
    }
    cout << cnt << endl;
    return 0;
}