#include <iostream>
#include <algorithm>
#include <vector>
#include <tuple>
#include <map>
#include <set>
#include <limits.h>;


using namespace std;

int R, C;
vector<char> board[101][101];	
string mani;
int dy[10]{ 0,1,1,1,0,0,0,-1,-1,-1 };
int dx[10]{ 0,-1,0,1,-1,0,1,-1,0,1 };
pair<int, int> cur_loc;
vector<pair<int, int>> moved_arduino;

void input() {
	cin >> R >> C;
	for (int i = 0;i < R;i++) {
		string tmp;
		cin >> tmp;
		for (int j = 0;j < C;j++) {
			if (tmp[j] == 'I') cur_loc = {i,j};
			if (tmp[j] == '.') continue;
			board[i][j].push_back(tmp[j]);
		}

	}

	
	cin >> mani;
	
}

void mad(pair<int, int> cur_loc) {
	moved_arduino.clear();
	for (int i = 0;i < R;i++) {
		for (int j = 0;j < C;j++) {
			if (!board[i][j].empty()&&board[i][j][0] == 'R') {
				int where;
				int min_dist = INT_MAX;
				for (int d = 1;d <= 9;d++) {
					int dist = abs(cur_loc.first - (i + dy[d])) + abs(cur_loc.second - (j + dx[d]));
					if (dist < min_dist) {
						min_dist = dist;
						where = d;
					}
				}
				moved_arduino.push_back(make_pair(i + dy[where], j + dx[where]));
			}
		}
	}
	for (int i = 0;i < R;i++) {
		for (int j = 0;j < C;j++) {
			board[i][j].clear();
		}
	}
	board[cur_loc.first][cur_loc.second].push_back('I');
	for (pair<int, int> p : moved_arduino) {
		board[p.first][p.second].push_back('R');
	}
}



int main() {

	input();
	int cnt = 0;
	bool win = true;
	for (char m : mani) {

	/*	for (int i = 0;i < R;i++) {
			for (int j = 0;j < C;j++) {
				if (board[i][j].empty()) cout << '.';
				else if (board[i][j][0] == 'I') cout << 'I';
				else cout << 'R';
			}
			cout << endl;
		}
		cout << endl;*/

		int move = m - '0';
		// 1. 종수 움직임
		board[cur_loc.first][cur_loc.second].clear();
		cur_loc = { cur_loc.first + dy[move],cur_loc.second + dx[move] };
		board[cur_loc.first][cur_loc.second].push_back('I');


		cnt++;



		// 2. 미친놈으로 간다면
		if (board[cur_loc.first][cur_loc.second].size() >= 2) {

			win = false;
			break;

		}


		// 3. 아두이노 움직이기
		mad(cur_loc);

		// 4. 미친+아두 -> 패배, 폭발
		for (int i = 0;i < R;i++) {
			if (!win) break;
			for (int j = 0;j < C;j++) {
				if (board[i][j].size() >= 2) {
					if (board[i][j][0] == 'I' && board[i][j].back() == 'R') {
						win = false;
						break;
					}
					else {
						board[i][j].clear();
					}
				}
			}
		}
		if (!win) break;
		
	}
	if (win) {
		for (int i = 0;i < R;i++) {
			for (int j = 0;j < C;j++) {
				if (board[i][j].empty()) cout << '.';
				else if (board[i][j][0] == 'I') cout << 'I';
				else cout << 'R';
			}
			cout << endl;
		}
	}
	else {
		cout << "kraj" << " " << cnt;
	}
	






}

