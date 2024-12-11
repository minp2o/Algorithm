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

int n;
int tops[1000001];
stack<int> sk;    //높이, 위치
int answer[1000001];

int main(){
    scanf("%d",&n);
    for(int i=1;i<=n;i++){
        scanf("%d",&tops[i]);
    }



    for(int i=n;i>=1;i--){
            
        while(!sk.empty()){
            if(tops[i]>=sk.top()){    //지금 i가 가리키는 탑이 스택의 top 이상일 경우 
                sk.pop();
            }else{  // 지금 i가 가리키는 탑이 스택의 top보다 작을 경우
                answer[i]=sk.top();
                break;
            }
        }

        if(sk.empty()){
            answer[i]=-1;
            sk.push(tops[i]);
            continue;
        }



        sk.push(tops[i]);

    }
    for(int i=1;i<=n;i++){
        printf("%d ",answer[i]);
    }

    
    
    
    
}

