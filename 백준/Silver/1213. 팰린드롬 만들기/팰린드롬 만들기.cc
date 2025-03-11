#include <bits/stdc++.h>
using namespace std;


int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);
	string str;
	map<char, int> strcnt;
	cin >> str;
	sort(str.begin(), str.end()); //정렬하고
	int limit = 0;
	int i = 0, left = 0, right = str.length() - 1;
	
	for (int i = 0; i < str.length(); i++) {
		if (strcnt[str[i]] > 0) {
			strcnt[str[i]]++;
		}
		else {
			strcnt[str[i]] = 1;
		}
	}
	char odd_char = 0;

	for (auto& pair : strcnt) {
		if (pair.second % 2 == 1) {
			limit++;
			odd_char = pair.first;
		}
	}

	if (limit > 1) {
		cout << "I'm Sorry Hansoo";
		return 0;
	}

	for (auto& pair : strcnt) {
		while (pair.second > 1) {
			str[left] = pair.first;
			str[right] = pair.first;
			left++;
			right--;
			pair.second -= 2;
		}
	}

	if (limit == 1) {
		str[str.length() / 2] = odd_char;
	}

	cout << str;

	return 0;
}
