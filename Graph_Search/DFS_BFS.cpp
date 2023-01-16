#include <bits/stdc++.h>

using namespace std;

int node_num, edge_num, start_node;
int edge[1001][1001]={0,}; // for edge check
int dfs_visited[1001]={0,};
int bfs_visited[1001]={0,};

void dfs(int num){
    if(dfs_visited[num]==1) return;

    cout << num << ' ';
    dfs_visited[num]=1;
    for(int i=1; i<=node_num; i++){
        if(dfs_visited[i]==1 || edge[num][i]==0)continue;

        dfs(i);
    }
}

void bfs(int num){
    queue<int> que;
    que.push(num);
    bfs_visited[num]=1;
    while(!que.empty()){
        int tmp = que.front();
        cout << tmp << ' ';
        que.pop();
        for(int i=1; i<=node_num; i++){
            if(bfs_visited[i]==1 || edge[tmp][i]==0)continue;
            bfs_visited[i]=1;
            que.push(i);
        }
    }
    cout << endl;
}

int main(){
    cin >> node_num >> edge_num >> start_node;
    int dfs_result, bfs_result;
    for(int i=0; i<edge_num; i++){
        int x,y;
        cin >> x >> y;
        edge[x][y]=1;
        edge[y][x]=1;
    }

    dfs(start_node);
    cout << endl;
    bfs(start_node);
    return 0;
}