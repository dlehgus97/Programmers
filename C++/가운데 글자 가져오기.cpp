//정답
#include <string>

using namespace std;

string solution(string s) {
    string answer = "";
    int n = s.size();
    if(n % 2 == 0){
        answer = s[(n/2)-1];
        answer += s[n/2];
    }
    else
        answer = s[n/2];
    return answer;
}


//참고로 만든 코드 
#include<iostream>
#include<string>

using namespace std;

int main() {
	string s;
	cin >> s;
	if (s.size() % 2 != 0)
		cout << s[s.size() / 2];
	else
		cout << s[(s.size() / 2) - 1] << s[(s.size() / 2)] << endl;


}
