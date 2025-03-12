#include <bits/stdc++.h>

using namespace std;

int solution(vector<int> wallet, vector<int> bill) {
    int answer = 0;
    int min_wallet = *min_element(wallet.begin(),wallet.end());
    int max_wallet = *max_element(wallet.begin(),wallet.end());
    int min_bill = *min_element(bill.begin(),bill.end());
    int max_bill = *max_element(bill.begin(),bill.end());
    
    cout << min_bill << " " << min_wallet << " " << max_bill << " " << max_wallet;

    while (min_bill > min_wallet || max_bill>max_wallet){
        if (bill[0] > bill[1]){
            bill[0] /= 2;
        }
        else{
            bill[1] /= 2;
        }
        
        min_bill = *min_element(bill.begin(),bill.end());
        max_bill = *max_element(bill.begin(),bill.end());
        answer++;
    }
    
    return answer;
}