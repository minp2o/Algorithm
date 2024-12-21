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

vector<pair<int,int>> v;

int main(){
    int n;
    cin>>n;

    for(int i=0;i<n;i++){
        int s,e;
        cin>>s>>e;
        v.push_back(make_pair(s,1));
        v.push_back(make_pair(e,-1));

    }

    sort(v.begin(),v.end());

    int cnt=0;
    int ans=0;

    for(pair<int,int> p:v){
        cnt+=p.second;
        ans=max(cnt,ans);
    }

    cout<<ans;
    
    
    
    

    
}

