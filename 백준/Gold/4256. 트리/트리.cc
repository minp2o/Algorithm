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

int tc;
int pre[1001];
int in[1001];
int n;



void make_post(int start, int end, int root){
    for(int i=start;i<=end;i++){
        if(pre[root]==in[i]){
            make_post(start,i-1,root+1);
            make_post(i+1,end,root+1 + i - start);
            cout<<pre[root]<<" ";
        }
    }
}

int main(){
    cin>>tc;
    for(int ii=0;ii<tc;ii++){
        cin>>n;
        for(int i=0;i<n;i++){
            cin>>pre[i];
        }
        for(int i=0;i<n;i++){
            cin>>in[i];
        }
        

        make_post(0,n-1,0);
        cout<<endl;
    }
    

    
    
    
    

    
}

