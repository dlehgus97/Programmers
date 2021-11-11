//answer 

#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
    vector<int> answer;
    for (int i = 0; i < commands.size(); i++) {
        vector<int> tmp;  //임시로 저장해준다. 
        for (int j = commands[i][0] - 1; j < commands[i][1]; j++)  //1이 두번째 자리가 아닌 첫번째 자리이기 떄문에 -1 을해준다.
            tmp.push_back(array[j]);
        sort(tmp.begin(), tmp.end());
        answer.push_back(tmp[commands[i][2] - 1]);
    }
    return answer;
}
