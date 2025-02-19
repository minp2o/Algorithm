#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>
#include <vector>
#include <tuple>
#include <stdio.h>


using namespace std;



int unf[1000001];
int n, m;

int find(int num) {
	if (num == unf[num]) {
		return num;
	}
	else {
		return unf[num]=find(unf[num]);
	}
}

void uni(int a, int b) {
	if (a == b) return;

	int fa = find(a);
	int fb = find(b);
	unf[fb]=fa;
}

int main() {


	scanf("%d %d", &n, &m);
	for (int i = 0;i <= n;i++) {
		unf[i] = i;
	}
	for (int i = 0;i < m;i++) {
		int opt, a, b;
		scanf("%d %d %d", &opt, &a, &b);
		if (!opt) {
			uni(a, b);
		}
		else {
			if (find(a) == find(b)) printf("YES\n");
			else printf("NO\n");
		}
	}
	





}





