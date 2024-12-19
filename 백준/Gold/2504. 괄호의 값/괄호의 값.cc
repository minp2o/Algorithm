#include <iostream>
#include <map>
#include <vector>
#include <queue>
#include <tuple>
#include <algorithm>
#include <set>
#include <sstream>
#include <string>
#include <stack>
using namespace std;

int answer=0;
stack<char> st;
char pre;


int main(){
    string str;
    cin>>str;
    int tmp1=1;
    int tmp2=0;
    pre='e';
    
    for(char c:str){
        if(st.empty()){
            if(c==')'||c==']'){
                cout<<0;
                return 0;
            }
        }
        if(c=='('){
            st.push(c);
            tmp1*=2;
        }else if(c=='['){
            st.push(c);
            tmp1*=3;
        }else if(c==')'){
            if(st.top()!='('){
                cout<<0;
                return 0;
            }
            st.pop();
            if(pre=='('){
                tmp2+=tmp1;
                
                tmp1/=2;

            }else{
                tmp1/=2;
            }
            
        }else if(c==']'){
            if(st.top()!='['){
                cout<<0;
                return 0;
            }
            st.pop();
            if(pre=='['){
                tmp2+=tmp1;
                tmp1/=3;

            }else{
                tmp1/=3;
            }
        }
        pre=c;
    }
    cout<<(st.empty()?tmp2:0);

    
    
    
    

    
}

