#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <string>
using namespace std;

int main()
{
    int N;
    cin >> N;
    string pattern;
    cin >> pattern;
    string req;
    int starNum = 0;
    bool roop_flag = false;

    for (int i = 0; i < pattern.length(); i++) {
        if (pattern[i] == '*') {
            starNum = i;
            break;
        }
    }


    for (int i = 0; i < N; i++) {
        cin >> req;
        roop_flag = false;
        for (int j = 0; j < starNum; j++) {
            if (req[j] != pattern[j]) {
                cout << "NE" << "\n";
                roop_flag = true;
                break;
            }
        }
        if (roop_flag == true) {
            continue;
        }
        string prefix = pattern.substr(0, starNum);
        string suffix = pattern.substr(starNum + 1); //*이후의 문자열

        if (!(req.length() >= suffix.length() &&
            req.substr(req.length()-suffix.length()) == suffix)){
            cout << "NE" << "\n";
            roop_flag = true;
        }
        if (req.length() < prefix.length() + suffix.length() && req.length() >= suffix.length() && req.substr(req.length() - suffix.length()) == suffix) {
            cout << "NE" << "\n";
            roop_flag = true;
        }

        if (roop_flag == true) {
            continue;
        }
        
        cout << "DA" << "\n";


    }
    
    
    return 0;
}
