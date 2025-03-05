#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;


pair<int, int> time_to_minute(int n){
    int hour = n/100;
    int minute = n %100;
        
    return make_pair(hour,minute);
}

int time_to_second(int hour, int minute){
    return 3600 * hour + 60 * minute;
}

int solution(vector<int> schedules, vector<vector<int>> timelogs, int startday) {
    int cnt = 0;
    //2차원 배열 rotate
    for(auto& inner : timelogs){
        rotate(inner.begin(),inner.end()-startday+1,inner.end());
    }
    for(int i=0; i<timelogs.size(); i++){
        for (int j=0; j<7; j++){
            cout << timelogs[i][j] << " ";
        }
        cout << "\n";
    }
    
    cnt = 0;
    for(int i=0; i<timelogs.size(); i++){
        for (int j=0; j<7; j++){
            if(j!=5 && j!=6){
                pair<int,int> timelog = time_to_minute(timelogs[i][j]);
                pair<int,int> schedule = time_to_minute(schedules[i]);
                
                int ts = time_to_second(timelog.first, timelog.second);
                int ss = time_to_second(schedule.first, schedule.second);
                
                cout << ts << " " << ss << "\n"; 
                if(ts - ss > 600){
                    cout << i << " " << j << "\n";
                    break;
                }
            
    }
    if(j == 6){
                cnt += 1;
            }
    }
        
    
}
    return cnt;
}