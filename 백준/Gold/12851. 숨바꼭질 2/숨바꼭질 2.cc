#include <iostream>
#include <map>
#include <vector>
#include <queue>
#include <tuple>
#include <algorithm>
#include <set>
#include <limits.h>
#include <sstream>
#include <string>
using namespace std;

int n,k;
int min_time,cnt;
bool visited[100001];

struct loc{
    int cv;
    int t;
    loc(int cv,int t){
        this->cv=cv;
        this->t=t;
    }
};

void bfs(int start){
    
    queue<loc> q;
    bool find=false;
    q.push(loc(start,0));
    while(!q.empty()){
        
        loc cur_p=q.front();
        visited[cur_p.cv]=true;
        q.pop();
        if(cur_p.t>min_time){
            break;
        }
        if(cur_p.cv==k){
            find=true;
            min_time=cur_p.t;
            cnt++;
        }
        if(!find){
            if(cur_p.cv-1>=0&&!visited[cur_p.cv-1]){
                q.push(loc(cur_p.cv-1,cur_p.t+1));
            }
            if(cur_p.cv+1<=100000&&!visited[cur_p.cv+1]){
                q.push(loc(cur_p.cv+1,cur_p.t+1));
            }
            if(cur_p.cv*2<=100000&&!visited[cur_p.cv*2]){
                q.push(loc(cur_p.cv*2,cur_p.t+1));
            }
        }

    }
}

int main(){
    cin>>n>>k;
    min_time=INT_MAX;
    bfs(n);
    cout<<min_time<<'\n'<<cnt;

    
    
    
    

    
}

