#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main()
{
    vector<char> vec;
    string str;

    cin >> str;

    for (char i : str) {
        vec.push_back(i);
    }

    while (vec.size() > 1){
        int front = vec.front();
        vec.erase(vec.begin());

        int end = vec.back();
        vec.pop_back();

        if (end != front) {
            cout << 0;
            return 0;
        }

    }

    cout << 1;
    
    return 0;
}
