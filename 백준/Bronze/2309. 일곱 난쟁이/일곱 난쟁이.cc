#include <iostream>
#include <algorithm>
using namespace std;


int main()
{   
    int arr[8];
    
    for (int i = 0; i < 9; i++) {
        cin >> arr[i];
    };

    int n = sizeof(arr) / sizeof(arr[0]);
    sort(arr, arr+n);
   

    do {
        int sum = 0;
        for (int i = 0; i < 7; i++) {
            sum += arr[i];

            if (sum == 100) {
                sort(arr, arr + 7);
                for (int i = 0; i < 7; i++) {
                    cout << arr[i] << "\n";
                }
                return 0;
            }



        };
    } while(next_permutation(&arr[0],&arr[0]+9));

    return 0;
}
