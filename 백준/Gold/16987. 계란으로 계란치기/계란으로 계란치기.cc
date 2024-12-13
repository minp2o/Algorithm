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

int n;
pair<int,int> eggs[10]; //내구도, 무게
int answer;
bool ch;

bool is_all_broken(int l){
    bool ch=true;
    for(int i=0;i<n;i++){
        if(i!=l){
            if(eggs[i].first>0){
                ch=false;
                break;
            }
        }
    }
    return ch;
}

void dfs(int l){
    
    if(l==n){
        int tmp=0;
        for(int i=0;i<n;i++){
            if(eggs[i].first<=0) tmp++;
        }
        answer=max(answer,tmp);
    }else{
        if(eggs[l].first<=0||is_all_broken(l)){
            dfs(l+1);
        }else{
            for(int i=0;i<n;i++){
                if(i!=l&&eggs[i].first>0){
                    eggs[l].first-=eggs[i].second;
                    eggs[i].first-=eggs[l].second;
                    dfs(l+1);
                    eggs[l].first+=eggs[i].second;
                    eggs[i].first+=eggs[l].second;

                }
            }
        }
    }
}

int main(){
    answer=0;
    cin>>n;
    for(int i=0;i<n;i++){
        int e,w;
        cin>>e>>w;
        eggs[i]=make_pair(e,w);

        

    }
    dfs(0);
    cout<<answer;


    
    
    
    

    
}

