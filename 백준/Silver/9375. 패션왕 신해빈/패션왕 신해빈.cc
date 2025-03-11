#include <bits/stdc++.h>
using namespace std;


vector<string> split(const string& input, string delimiter) {
	auto start = 0;
	auto end = input.find(delimiter);
	vector<string> result;
	while (end != string::npos) {
		result.push_back(input.substr(start, end - start));
		start = end + delimiter.size();
		end = input.find(delimiter, start);
	}
	result.push_back(input.substr(start));
	return result;
}

int main() {
	int T, n;
	string clothe;
	cin >> T;

	for (int i = 0; i < T; i++) {
		cin >> n;
		cin.ignore();
		map<string, int> clt;
		int cnt=1;
		for (int j = 0; j < n; j++) {
			getline(cin, clothe);
			vector<string> split_clothe = split(clothe, " ");
			if (clt[split_clothe[1]] > 0) {
				clt[split_clothe[1]]++;

			}
			else {
				clt[split_clothe[1]] = 1;
			}
		}

		
		for (auto& pair : clt) {
			cnt *= (pair.second + 1);
		}
		cout << cnt-1 << "\n";
	}


	return 0;
}
