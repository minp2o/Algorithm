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
int relations[201][201];
int travel[1001];
int unf[201];

int find(int a){
    if(unf[a]==a) return a;
    else{
        return unf[a]=find(unf[a]);
    }
}

void un(int a, int b){
    int fa=find(a);
    int fb=find(b);
    if(fa!=fb) unf[fa]=fb;
}

int main(){
    cin>>n>>m;
    for(int i=1;i<=n;i++){
        for(int j=1;j<=n;j++){
            cin>>relations[i][j];
        }
    }
    for(int i=0;i<m;i++){
        cin>>travel[i];
    }
    for(int i=1;i<=n;i++){
        unf[i]=i;
    }

    for(int i=1;i<n;i++){
        for(int j=i+1;j<=n;j++){
            if(relations[i][j]==1){
                un(i,j);
            }
        }
    }
    int repre=find(travel[0]);
    string answer="YES";
    for(int i=1;i<m;i++){
        if(repre!=find(travel[i])){
            answer="NO";
            break;
        } 
    }

    cout<<answer;

    

    
}

