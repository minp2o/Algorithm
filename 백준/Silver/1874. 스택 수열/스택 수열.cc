#include <iostream>
#include <map>
#include <vector>
#include <queue>
#include <tuple>
#include <algorithm>
#include <set>
#include <stack>
#include <sstream>
#include <string>
using namespace std;

int n;
stack<int> st;
vector<char> v;


int main(){
    cin>>n;
    bool trap=false;
    int cnt=1;


    for(int i=1;i<=n;i++){
        int tmp;
        cin>>tmp;
        while(1){
            if(tmp>=cnt){
                st.push(cnt);
                v.push_back('+');
                cnt++;
            }else if(tmp<cnt){
                if(st.top()!=tmp){
                    trap=true;
                    break;
                }
                st.pop();
                v.push_back('-');
                break;

            }
        }
        if(trap) break;

    }
    if(!trap){
        for(char c:v){
            cout<<c<<'\n';
        }
    }else{
        cout<<"NO";
    }
    
    


    
    
    
    

    
}




