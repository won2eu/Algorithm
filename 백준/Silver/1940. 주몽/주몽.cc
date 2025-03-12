#include <bits/stdc++.h>
using namespace std;

void print(const vector<int>& b) {
	for (int num : b) cout << num << " ";
	cout << endl;
}

vector<string> split(const string& input, string delimiter) {
	vector<string> result;
	auto start=0;
	auto end = input.find(delimiter);
	while (end != string::npos) {
		result.push_back(input.substr(start, end - start));
		start = end + delimiter.size();
		end = input.find(delimiter, start);
	}

	result.push_back(input.substr(start));
	return result;
}

int combi(int start,int M ,vector<int>& b, vector<int>& ss) {
	int cnt = 0;

	if (b.size() == 2) {
		if (b[0] + b[1] == M) {
			return 1;
		}
		return 0;
	}
	for (int i = start + 1; i < ss.size(); i++) {
		b.push_back(ss[i]);
		cnt += combi(i,M, b, ss);
		b.pop_back();
	}
	return cnt;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);
	int N, M;
	int suit;

	cin >> N;
	cin >> M;
	vector<int> ss;
	vector<int> b;
	for (int i = 0; i < N; i++) {
		cin >> suit;
		ss.push_back(suit);
	}

	int cnt = combi(-1, M, b, ss);
	cout << cnt;
	return 0;
}
