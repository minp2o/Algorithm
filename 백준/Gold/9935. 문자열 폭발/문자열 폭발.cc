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

int depth[1000001];
stack<char> st;

int main(){
    string str;
    string tg;
    string answer="";
    int idx=0;  //depth배열을 가리키는 인덱스
    cin>>str>>tg;


    for(char c:str){
        st.push(c);
        if(c==tg[0]&&depth[idx]>0){
            depth[++idx]++;
        }else if(c==tg[depth[idx]]){
            if(depth[idx]+1==tg.size()){
                depth[idx]=0;
                if(idx>0){
                    idx--;
                }
                for(int i=0;i<tg.size();i++){
                    st.pop();
                }
            }else{
                depth[idx]++;
            }
        }else{
            for(int i=0;i<=idx;i++){
                depth[i]=0;
            }
            idx=0;

        }
    }
    if(st.empty()){
        cout<<"FRULA";
        return 0;

    }
    while(!st.empty()){
        answer+=st.top();
        st.pop();
    }
    reverse(answer.begin(),answer.end());
    cout<<answer;
    
    
    
    
    
    

    
}

