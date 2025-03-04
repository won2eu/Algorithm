#include <iostream>
#include <algorithm>
using namespace std;

int arr[26];

int main()
{   
    string str;
    
    cin >> str;

    for (int i = 0; i < str.length(); i++) {
        int cnt = count(str.begin(), str.end(), str[i]);
        arr[str[i] - 'a'] = cnt;
    }
   
    for (int i = 0; i < 26; i++) {
        cout << arr[i] << " ";
    }
    return 0;
}
