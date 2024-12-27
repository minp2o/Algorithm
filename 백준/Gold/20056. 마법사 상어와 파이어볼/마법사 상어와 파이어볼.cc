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

int n,m,k;  // 격자 크기, 파이어볼 개수, 반복 횟수
int dy[8]{-1,-1,0,1,1,1,0,-1};
int dx[8]{0,1,1,1,0,-1,-1,-1};

struct fireBall{
    int r;
    int c;
    int m;
    int s;
    int d;
    fireBall(int r,int c,int m,int s,int d){
        this->r=r;
        this->c=c;
        this->m=m;
        this->s=s;
        this->d=d;
    }
};

vector<fireBall> board[51][51]; // 파이어볼들의 정보 저장하는 격자

void input(){
    cin>>n>>m>>k;
    for(int i=0;i<m;i++){
        int r,c,m,s,d;
        cin>>r>>c>>m>>s>>d;
        board[r-1][c-1].push_back(fireBall(r-1,c-1,m,s,d));
    }
}

void game(){
    // 파이어볼 이동
    vector<fireBall> moved_fB;  // 이동한 파이어볼들 집합
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            if(!board[i][j].empty()){
                for(fireBall fB:board[i][j]){
                    fB.r = (fB.r + fB.s*dy[fB.d] + n*1000) % n;
                    fB.c = (fB.c + fB.s*dx[fB.d] + n*1000) % n;


                    moved_fB.push_back(fB);

                }
                board[i][j].clear();
            }
        }
    }
    for(fireBall mFB:moved_fB){
        board[mFB.r][mFB.c].push_back(mFB);
    }

    //같은 칸에 2개 이상의 파이어볼 나누기
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            if(board[i][j].size()>=2){
                //파볼 질량합 구하기
                int cnt=0;  //파볼 개수
                int tot_m=0;
                int tot_s=0;

                for(fireBall fB:board[i][j]){
                    cnt++;
                    tot_m+=fB.m;
                    tot_s+=fB.s;
                }
                
                //파볼의 방향이 모두 홀수이거나 짝수이면
                bool all=true;
                bool isOdd=false;
                if(board[i][j][0].d%2==1){
                    isOdd=true;
                }
                for(fireBall fB:board[i][j]){
                    if(fB.d%2==0&&isOdd==true){
                        all=false;
                        break;
                    }else if(fB.d%2==1&&isOdd==false){
                        all=false;
                        break;
                    }
                }

        


               

                board[i][j].clear();
                if(all){
                    if(tot_m/5>0){
                        board[i][j].push_back(fireBall(i,j,tot_m/5,tot_s/cnt,0));
                        board[i][j].push_back(fireBall(i,j,tot_m/5,tot_s/cnt,2));
                        board[i][j].push_back(fireBall(i,j,tot_m/5,tot_s/cnt,4));
                        board[i][j].push_back(fireBall(i,j,tot_m/5,tot_s/cnt,6));


                    }
                }else{
                    if(tot_m/5>0){
                        board[i][j].push_back(fireBall(i,j,tot_m/5,tot_s/cnt,1));
                        board[i][j].push_back(fireBall(i,j,tot_m/5,tot_s/cnt,3));
                        board[i][j].push_back(fireBall(i,j,tot_m/5,tot_s/cnt,5));
                        board[i][j].push_back(fireBall(i,j,tot_m/5,tot_s/cnt,7));
                    }
                }
            }
        }
    }
    
}

int main(){

    //입력받기
    input();

    for(int i=0;i<k;i++){
        game();
    }
    int answer=0;
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            if(!board[i][j].empty()){
                for(fireBall fB:board[i][j]){
                    answer+=fB.m;
                }
            }
        }
    }
    cout<<answer;

    



    
}

