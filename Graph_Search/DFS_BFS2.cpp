#include <bits/stdc++.h>

using namespace std;


int node_num, edge_num, start_node;
bool visited[1001];
vector<int> edge[1001];

void dfs(int num){
    visited[num]=true;
    cout << num << ' ';
    sort(edge[num].begin(), edge[num].end());
    for(int i=0; i< edge[num].size(); i++){
        int y = edge[num][i];
        if(!visited[y]) dfs(y);
    }
}

void bfs(int num){
    queue<int> que;
    visited[num]=true;
    que.push(num);

    while(!que.empty()){
        int tmp = que.front();
        cout << tmp << ' ';
        que.pop();
        sort(edge[num].begin(), edge[num].end());
        for(int i=0; i<edge[tmp].size(); i++){
            if(!visited[edge[tmp][i]]){
                que.push(edge[tmp][i]);
                visited[edge[tmp][i]] = true;
            }
        }
    }
}

int main(){
    cin >> node_num >> edge_num >> start_node;
    for(int i=0; i<edge_num; i++){
        int x,y;
        cin >> x >> y;
        edge[x].push_back(y);
        edge[y].push_back(x);
    }

    dfs(start_node);
    cout << endl;
    memset(visited, 0, sizeof(visited));
    bfs(start_node);
    cout << endl;
    return 0;
}