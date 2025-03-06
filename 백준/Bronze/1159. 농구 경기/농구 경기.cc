#include <iostream>
#include <algorithm>
#include <vector>
#include <map>

using namespace std;
map<char, int> dict;
string arr[150];

int main()
{
    int N;
    cin >> N;
    string name;

    for (int i = 0; i < N; i++) {
        cin >> name;
        if (dict.find(name[0]) != dict.end()) {
            dict[name[0]]++;
        }
        else {
            dict[name[0]] = 1;
        }
    }
    int cnt=0;
    for (auto i : dict) {
        if (i.second >= 5) {
            cnt += 1;
            cout << i.first;
        }
    }
    if (cnt == 0) {
        cout << "PREDAJA";
    }
    
    
    return 0;
}
