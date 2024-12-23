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

int n,k,r;
int farm[101][101];
bool lines[250][250];
bool visited[101][101];
bool cows[101][101];
int dy[4]{-1,1,0,0};
int dx[4]{0,0,-1,1};
int ans;

struct Point{
    int y;
    int x;
    Point(int y,int x){
        this->y=y;
        this->x=x;
    }
};

void bfs(int y,int x){
    visited[y][x]=true;
    queue<Point> q;
    q.push(Point(y,x));
    while(!q.empty()){
        Point cur_p=q.front();
        //cout<<cur_p.y<<" "<<cur_p.x<<endl;
        q.pop();
        for(int i=0;i<4;i++){
            int ny=cur_p.y+dy[i];
            int nx=cur_p.x+dx[i];
            int yy=2*cur_p.y-1;
            int xx=2*cur_p.x-1;
            int nyy=2*ny-1;
            int nxx=2*nx-1;
            if(1<=ny&&ny<=n&&1<=nx&&nx<=n&&visited[ny][nx]==false&&lines[(yy+nyy)/2][(xx+nxx)/2]==false){
                q.push(Point(ny,nx));
                visited[ny][nx]=true;
                if(farm[ny][nx]!=0){
                   
                    cows[farm[y][x]][farm[ny][nx]]=true;
                    cows[farm[ny][nx]][farm[y][x]]=true;
                }
            }
        }
    }
}

int main(){
    
    cin>>n>>k>>r;   //농장 크기, 소 마리수, 길 수
    for(int i=0;i<r;i++){
        int q,w,e,t;
        cin>>q>>w>>e>>t;
        q=2*q-1;
        w=2*w-1;
        e=2*e-1;
        t=2*t-1;
        
        lines[(q+e)/2][(w+t)/2]=true;
        
    }        
    int cnt=1;
    for(int i=0;i<k;i++){
        int y,x;
        cin>>y>>x;
        farm[y][x]=cnt;
        cnt++;
    }
    for(int i=1;i<=k;i++){
        cows[i][i]=true;
    }
    
    for(int i=1;i<=n;i++){
        for(int j=1;j<=n;j++){
            if(farm[i][j]!=0){  //소를 만남
                for(int ii=1;ii<=n;ii++){
                    for(int jj=1;jj<=n;jj++){
                        visited[ii][jj]=false;  // 방문 초기화
                    }
                }

                bfs(i,j);
            }
        }
    }
    for(int i=1;i<=k;i++){
        for(int j=1;j<=k;j++){
            if(cows[i][j]==false){
                ans++;
            }
        }
    }
    // for(int i=1;i<=n;i++){
    //     for(int j=1;j<=n;j++){
    //         cout<<cows[i][j]<<" ";
    //     }cout<<endl;
    // }
    cout<<ans/2;
    

    
    


    
    
    
    

    
}

