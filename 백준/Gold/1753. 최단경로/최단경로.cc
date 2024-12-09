#include <iostream>
#include <map>
#include <vector>
#include <queue>
#include <tuple>
#include <algorithm>
#include <set>
#include <sstream>
#include <string>
#include <limits.h>

using namespace std;

struct myCompare{
    bool operator()(pair<int,int>& p1, pair<int,int>& p2){
        return p1.first>p2.first;
    }
};

int v,e,k;  //정점 개수, 간선 개수, 시작점
vector<pair<int,int>> linked_list[20001];   // 각 정점 인접 리스트
int table[20001];   // 최단경로테이블
priority_queue<pair<int,int>,vector<pair<int,int>>,myCompare> pQ;       // (거리,정점)의 우선순위큐


void make_table(int start){

    //초기화
    pQ.push(make_pair(0,start));
    for(int i=1;i<=v;i++){
        table[i]=INT_MAX;
    }
    table[start]=0;

    while(!pQ.empty()){
        pair<int,int> cur_p=pQ.top();
        for(pair<int,int> p:linked_list[cur_p.second]){
            if(p.first+cur_p.first<table[p.second]){
                table[p.second]=p.first+cur_p.first;
                pQ.push(make_pair(p.first+cur_p.first,p.second));
            }
        }
        
        pQ.pop();
    }
}

int main(){

    cin>>v>>e>>k;
    for(int i=0;i<e;i++){
        int a,b,c;
        cin>>a>>b>>c;
        linked_list[a].push_back(make_pair(c,b));
    }
    
    
    make_table(k);
    for(int i=1;i<=v;i++){
        if(table[i]==INT_MAX){
            cout<<"INF"<<endl;
        }else{
            cout<<table[i]<<endl;
        }
    }
    
    

    
}

