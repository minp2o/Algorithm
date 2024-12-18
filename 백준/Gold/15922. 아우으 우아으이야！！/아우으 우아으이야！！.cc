#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int n;
    int answer = 0;
    pair<int, int> line[100001];

    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> line[i].first >> line[i].second;
    }


    // 첫 번째 선분 초기화
    int lt = line[0].first;
    int rt = line[0].second;

    for (int i = 1; i < n; i++) {
        if (line[i].first > rt) {
            // 현재 선분이 이전 선분과 겹치지 않는 경우
            answer += (rt - lt); // 이전 선분 길이를 더함
            lt = line[i].first; // 새로운 선분 시작점 갱신
            rt = line[i].second; // 새로운 선분 끝점 갱신
        } else {
            // 현재 선분이 이전 선분과 겹치는 경우
            rt = max(rt, line[i].second); // 끝점 확장
        }
    }

    // 마지막으로 남은 선분 길이 추가
    answer += (rt - lt);

    cout << answer;

    return 0;
}
