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


int N, tmp, ans;
vector<int> v;

int main(){
	cin>>N;
	ans=1;
	cin>>tmp;
	v.push_back(tmp);
	for(int i=1;i<N;i++){
		cin>>tmp;
		if(tmp>*(v.end()-1)) {
			v.push_back(tmp);
			ans++;
		}else{
			auto idx = lower_bound(v.begin(),v.end(),tmp) - v.begin();
			v[idx]=tmp;
		}
		
		
	}
	cout<<ans;
    
    
    
    

    
}

