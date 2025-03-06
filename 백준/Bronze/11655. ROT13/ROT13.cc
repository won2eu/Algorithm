#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <string>
using namespace std;


int main()
{   
    string str;
    getline(cin, str);
    
    for (int i = 0; i < str.length(); i++) {
        if (str[i] != ' ' && isalpha(str[i]))
        {
            if ((str[i]<97 && str[i]>77) || str[i] >= 110) {
                str[i] -= 13;
            }

            else {
                str[i] += 13;
            }
        }
    }
    cout << str;
    
    
    return 0;
}
