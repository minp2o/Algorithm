#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>
#include <vector>
#include <tuple>
#include <map>


using namespace std;

int N;
long long M;
long long trees[1000001];

void input() {
	cin >> N >> M;
	for (int i = 0;i < N;i++) {
		cin >> trees[i];
	}
}

int bs() {
	int lt = 0;
	int rt = 1000000000;
	long long len = 0;
	long long mid=(lt+rt)/2;
	long long ans;
	while (lt <= rt) {
		mid = (lt + rt) / 2;
		len = 0;
		for (int i = 0;i < N;i++) {
			if (trees[i] > mid) len += (trees[i] - mid);
		}
		if (len >= M) {
			ans = mid;
			lt = mid + 1;
		}
		else {
			rt = mid - 1;
		}
	}
	return ans;
}



int main() {

	input();
	cout << bs();
	





}

