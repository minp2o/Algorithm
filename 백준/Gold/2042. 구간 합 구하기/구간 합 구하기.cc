// 백준 2042
// 세그먼트 트리
// 세그먼트 트리는 구간합 알고리즘으로 배열의 원소를 업데이트 하는데
// O(N)의 시간이 걸리는 prefix sum를 보완하여 O(logN)로 줄여준다.

// 1. 트리 초기화 하기
// 2^k >= N 인 k 최솟값 찾기
// N이 8이면 k는 3이고, 배열의 크기는 2^k * 2 즉 16
// start index는 2^k 즉 8
// 구간 합: A[N] = A[2N]+A[2N+1]
// 
// 2. 질의값 구하기
// 질의 인덱스를 세그먼트 트리 인덱스로 변경
// seg_i = q_i + 2^k -1
// 질의값 구하는 과정
// start_index % 2 = 1 이면 해당 노드 선택
// end_index % 2 = 0 이면 해당 노드 선택
// start_index depth 변경: start_index = (start_index+1)/2
// end_index depth 변경: end_index = (end_index-1)/2
// 반복하다가 end_index<start_index면 종료

// 3. 데이터 업데이트하기
// 바뀐 원소부터 부모 끝까지 다 바꾸면 끝 (이게 log(N)으로 장점)



// N이 최대 100만이므로 k는 20
// 트리 크기는 2^21


#include <iostream>
#include <algorithm>
#include <vector>
#include <tuple>
#include <map>
#include <set>


using namespace std;

int N, M, K;
const long long tree_size = 1 << 21;
long long tree[tree_size];



void input() {
	cin >> N >> M >> K;
}

// k값 찾기
long long find() {
	long long k = 0;
	while (1) {
		if ((1 << k) >= N) break;
		k++;
	}
	return k;
}

// 트리 초기화하기
void initial(long long k) {
	long long s_i = 1LL << k;
	for (int i = 0;i < N;i++) {
		long long tmp;
		cin >> tmp;
		tree[s_i++] = tmp;
	}

	s_i = 1LL << k;

	for (long long i = s_i - 1;i > 0;i--) {
		tree[i] = tree[2 * i] + tree[2 * i + 1];
	}
}

void update(long long w, long long e, long long k) {
	long long what = w + (1LL << k) - 1;
	long long diff = e - tree[what];
	tree[what] = e;
	what /= 2;
	while (what > 0) {
		tree[what] += diff;
		what /= 2;
	}
}

long long tree_sum(long w, long e, long k) {
	long long s_i = w + (1LL << k) - 1;
	long long e_i = e + (1LL << k) - 1;


	long long what_to_add = 0;
	while (s_i <= e_i) {
		if (s_i % 2 == 1) {
			what_to_add += tree[s_i];
		}

		if (e_i % 2 == 0) {
			what_to_add += tree[e_i];
		}

		s_i = (s_i + 1) / 2;
		e_i = (e_i - 1) / 2;
	}

	return what_to_add;
}



int main() {

	input();
	long long k = find();

	initial(k);


	/*for (int i = 0;i < 16;i++) {
		cout << tree[i] << " ";
	}*/

	for (int tc = 0;tc <M + K;tc++) {
		long long q, w, e;
		cin >> q >> w >> e;
		if (q == 1) {
			//w번째 수를 e로 바꾸기
			update(w, e, k);
		}
		else if (q == 2) {
			//w번째 수부터 e번째 수까지의 합 구하기
			cout << tree_sum(w, e, k) << endl;

		}

	}









}

