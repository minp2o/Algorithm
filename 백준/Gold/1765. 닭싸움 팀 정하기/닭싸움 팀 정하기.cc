#include <iostream>
#include <algorithm>
#include <vector>
#include <tuple>
#include <map>
#include <set>


using namespace std;

int n, m;
set<int> E[1001];
set<int> F[1001];
int unf[1001];

void input() {
	cin >> n >> m;
	while (m--) {
		char EorF;
		int tmp1, tmp2;
		cin >> EorF >> tmp1 >> tmp2;
		if (EorF == 'E') {
			E[tmp1].insert(tmp2);
			E[tmp2].insert(tmp1);
		}
		else {
			F[tmp1].insert(tmp2);
			F[tmp2].insert(tmp1);
		}
	}
}

int find(int a) {
	if (unf[a] == a) {
		return a;
	}
	else {
		return unf[a]=find(unf[a]);
	}
}

void uni(int a, int b) {
	int fa = find(a);
	int fb = find(b);
	unf[fa] = fb;
	
}


int main() {

	input();
	// 원수의 원수 친구 셋에 넣기
	for (int i = 1;i <= n;i++) {
		for (int j : E[i]) {
			for (int k : E[j]) {
				if (k != i) {
					F[i].insert(k);
					F[k].insert(i);
				}
			}
		}
	}

	for (int i = 1;i <= n;i++) {
		unf[i] = i;
	}

	for (int i = 1;i <= n;i++) {
		for (int j : F[i]) {
			uni(i, j);
		}
	}

	for (int i = 1;i <= n;i++) {
		find(i);
	}

	int ans = 0;

	for (int i = 1;i <= n;i++) {
		if (unf[i] == i) {
			ans++;
		}
	}

	cout << ans;
	
	







}

