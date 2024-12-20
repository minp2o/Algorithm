#include <iostream>
#include <map>
#include <vector>
#include <queue>
#include <tuple>
#include <algorithm>
#include <set>
#include <sstream>
#include <string>
using namespace std;

int n,m;
string battleground[101];
bool visited[101][101];
int al,en;
int tmp;
int dy[4]{-1,1,0,0};
int dx[4]{0,0,-1,1};


struct Point{
    int y;
    int x;
    int c;
    Point(int y,int x,int c){
        this->y=y;
        this->x=x;
        this->c=c;
    }
};

void dfs(Point p){
    tmp++;
    visited[p.y][p.x]=true;
    for(int i=0;i<4;i++){
        int ny=p.y+dy[i];
        int nx=p.x+dx[i];
        if(0<=ny&&ny<n&&0<=nx&&nx<m&&!visited[ny][nx]&&battleground[ny][nx]==p.c){
            dfs(Point(ny,nx,p.c));
        }
    }
}

int main(){
    cin>>m>>n;
    for(int i=0;i<n;i++){
        cin>>battleground[i];
    }

    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            if(!visited[i][j]){
                tmp=0;
                dfs(Point(i,j,battleground[i][j]));
                if(battleground[i][j]=='W'){
                    al+=tmp*tmp;
                }else{
                    en+=tmp*tmp;
                }
            }
        }
    }
    cout<<al<<" "<<en;

    
    
    
    

    
}

