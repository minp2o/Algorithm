#define _CRT_SECURE_NO_WARNINGS
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

int N;
vector<int> v;
int dp[1001];
int ans=1;

int main(){
	cin>>N;

	for(int i=0;i<N;i++){
		int tmp;
		cin>>tmp;
		v.push_back(tmp);
	}
	for(int i=0;i<N;i++){
		dp[i]=1;
	}
	for(int i=0;i<N;i++){
		for(int j=0;j<i;j++){
			if(v[i]>v[j]){
				dp[i]=max(dp[i],dp[j]+1);
				ans=max(ans,dp[i]);
			}
		}
	}
	cout<<ans;
		
	
	
    
    
    

    
}

