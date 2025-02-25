#include <iostream>
#include <algorithm>
#include <vector>
#include <tuple>
#include <map>
#include <set>
#include <queue>
#include <limits.h>


using namespace std;



int N, P, K;
vector<pair<int, int>> graph[1001];	//이어진 정점번호, 가격
int dist[1001];

void input() {
	cin >> N >> P >> K;
	int q, w, e;
	for (int i = 0;i < P;i++) {
		cin >> q >> w >> e;
		graph[q].push_back(make_pair(w, e));
		graph[w].push_back(make_pair(q, e));

	}
}

int dijkstra(int &num) {
	priority_queue<pair<int, int>, vector<pair<int,int>>, greater<pair<int,int>>> pq;
	for (int i = 1;i <= N;i++) {
		dist[i] = INT_MAX;
	}
	dist[1] = 0;
	for (pair<int, int> p : graph[1]) {
		
		if (p.second > num) {
			if (dist[1] + 1 < dist[p.first]) {
				dist[p.first] = dist[1] + 1;
				pq.push({dist[p.first],p.first});
			}
		}
		else {
			if (dist[1] < dist[p.first]) {
				dist[p.first] = dist[1];
				pq.push({ dist[p.first],p.first });
			}
		}
	}
	while (!pq.empty()) {
		pair<int, int> cur_p = pq.top();
		pq.pop();
		for (pair<int, int> p : graph[cur_p.second]) {
			if (p.second > num) {
				if (dist[cur_p.second] + 1 < dist[p.first]) {
					dist[p.first] = dist[cur_p.second] + 1;
					pq.push({ dist[p.first],p.first });
				}
			}
			else {
				if (dist[cur_p.second] < dist[p.first]) {
					dist[p.first] = dist[cur_p.second];
					pq.push({ dist[p.first],p.first });
				}
			}
		}

	}
	return dist[N];
	
}

int main() {

	input();
	int lt = 0;
	int rt = 1000000;
	int mid;
	int ans = -1;
	while (lt <= rt) {
		mid = (lt + rt) / 2;
		if (dijkstra(mid) <= K) {
			ans = mid;
			rt = mid - 1;
		}
		else {
			lt = mid + 1;
		}
		
	}
	cout << ans;





}

