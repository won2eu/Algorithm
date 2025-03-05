#include <iostream>
#include <algorithm>
using namespace std;

int arr[100];
int main()
{   
    int a, b, c;
    cin >> a  >> b >> c;

    for (int i = 0; i < 3; i++) {
        int start, end;
        cin >> start >> end;

        for (int j = start; j < end; j++) {
            arr[j] += 1;

        }

    }
    int sum = 0;
    for (int i : arr) {
        if (i == 1) {
            sum += a;
        }

        else if (i == 2) {
            sum += b*2;
        }

        else if (i == 3) {
            sum += c*3;
        }
    }

    cout << sum;
    return 0;
}
