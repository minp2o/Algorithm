#include <iostream>
#include <algorithm>
#include <vector>
#include <tuple>
#include <map>
#include <set>
#include <queue>


// 불이 켜져있는 방 -> 들어감 -> 불 킴


using namespace std;

int N, M;
vector<pair<int, int>> hut[110][110];
int ans=1;
int dy[4]{ -1,1,0,0 };
int dx[4]{ 0,0,-1,1 };
bool light[101][101];
bool light_visited[101][101];
bool visited[101][101];
bool can;


void input() {
	cin >> N >> M;
	int x, y, a, b;
	for (int i = 0;i < M;i++) {
		cin >> x >> y >> a >> b;
		hut[x][y].push_back(make_pair(a, b));
	}
}

void dfs(int y,int x) {

	visited[y][x] = true;
	//불켜기
	for (pair<int, int> &np : hut[y][x]) {
		if (!light[np.first][np.second]) {
			ans++;
			light[np.first][np.second] = true;

			can = false;
			for (int i = 0;i < 4;i++) {
				int ny = np.first + dy[i];
				int nx = np.second + dx[i];
				if(0<=ny&&ny<=N&&0<=nx&&nx<=N&&visited[ny][nx]){
					can = true;
					break;
				}
			}
			if(can) dfs(np.first,np.second);
			
		}
	}
	for (int i = 0;i < 4;i++) {
		
		int ny = y + dy[i];
		int nx = x + dx[i];
		if (0 <= ny && ny <= N && 0 <= nx && nx <= N && light[ny][nx] && !visited[ny][nx]) {
			dfs(ny, nx);
		}
	}
}



int main() {

	input();
	light[1][1] = true;
	

	dfs(1, 1);
	
	cout << ans;





}

