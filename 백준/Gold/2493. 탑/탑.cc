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
int tops[5000001];
stack<pair<int,int>> sk;    //높이, 위치
int answer[5000001];

int main(){
    scanf("%d",&n);
    for(int i=1;i<=n;i++){
        scanf("%d",&tops[i]);
    }



    for(int i=1;i<=n;i++){
            
        while(!sk.empty()){
            if(tops[i]>=sk.top().first){    //지금 i가 가리키는 탑이 스택의 top 이상일 경우 
                sk.pop();
            }else{  // 지금 i가 가리키는 탑이 스택의 top보다 작을 경우
                answer[i]=sk.top().second;
                break;
            }
        }

        if(sk.empty()){
            answer[i]=0;
            sk.push(make_pair(tops[i],i));
            continue;
        }



        sk.push(make_pair(tops[i],i));

    }
    for(int i=1;i<=n;i++){
        printf("%d ",answer[i]);
    }

    
    
    
    
}

