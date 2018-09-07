#include <iostream>
using namespace std;

int main(){
	int n;
	int cnt =0;
	int total =0;
	cin >> n;
	
	int score[n];
	for(int i=0; i<n; i++){
		cin >> score[i];
		if(score[i] == 1){
			cnt += 1;
			total += cnt;
		}
		else if(score[i] == 0){
			cnt = 0;
		}
	}
	cout << total;
	
	return 0;
}
