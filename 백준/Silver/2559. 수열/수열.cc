#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <string>
#include <numeric>
using namespace std;

int main()
{   
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int N, K;
    cin >> N >> K;
    vector<int> arr(N, 0);
    int maxSum = 0;

    for (int i = 0; i < N; i++) {
        cin >> arr[i];
        
    }

    int sum = 0;
    for (int i = 0; i < K; i++) {
        sum += arr[i];
    }

    maxSum = sum;

    for (int i = K; i < N; i++) {
        sum += arr[i] - arr[i - K];
        maxSum = max(maxSum, sum);
    }
   
    cout << maxSum;
    return 0;
}