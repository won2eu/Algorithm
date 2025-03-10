#include <iostream>
#include <algorithm>
#include <map>
#include <string>
using namespace std;

int main()
{   
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    map <int, string> poketmon;
    map <string, int> poketmon2;
    int N, M, num;
    string str;
    cin >> N >> M;
    
    for (int i = 1; i <= N; i++) {
        cin >> str;
        poketmon[i] = str;
        poketmon2[str] = i;
    }
    
    for (int i = 1; i <= M; i++) {
        cin >> str;
        if (isdigit(str[0]) != 0) {
            num = stoi(str);
            cout << poketmon[num] << "\n";
        }
        else {
            cout << poketmon2[str] << "\n";
        }
    }
    return 0;
}