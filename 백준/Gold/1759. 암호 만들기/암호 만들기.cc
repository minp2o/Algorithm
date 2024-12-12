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

// 길이 L
// 모음>=1
// 자음>=2
// 오름차순

int l,c;
vector<char> alphas;
char answer[16];
char moeum[5]{'a','e','i','o','u'};


void dfs(int level,int m, int z, char answer[16], int start){
    if(level==l){
        if(m>=1&&z>=2){
            for(int i=0;i<l;i++){
                cout<<answer[i];
            }
            cout<<'\n';
        }
    }else{
        for(int i=start;i<c;i++){
            answer[level]=alphas[i];
            bool ch=false;
            for(char mm:moeum){
                if(mm==alphas[i]){
                    ch=true;
                    break;
                }
            }
            if(ch){
                dfs(level+1,m+1,z,answer,i+1);
            }else{
                dfs(level+1,m,z+1,answer,i+1);
            }
        }
    }
}

int main(){


    cin>>l>>c;

    for(int i=0;i<c;i++){
        char tmp;
        cin>>tmp;
        alphas.push_back(tmp);
    }

    sort(alphas.begin(),alphas.end());

    dfs(0,0,0,answer,0);
    




    
    
    
    

    
}

