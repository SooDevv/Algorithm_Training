#include <iostream>
using namespace std;

int main(){
	int cnt;
	int play[3][4];
	
	for(int i=0; i<3 ;i++){
		for(int j=0; j<4; j++){
			cin >> play[i][j]; 
		}
	}
	
	for(int i=0; i<3; i++){
		cnt = 0;
		for(int j=0; j<4; j++){
			if(play[i][j] == 0){
				cnt += 1;
			}
		}
		if(cnt==1){
			cout << 'A' <<endl;
		}
		else if(cnt==2){
			cout << 'B' <<endl;
		}else if(cnt==3){
			cout << 'C' <<endl;
		}else if(cnt==4){
			cout << 'D' <<endl;
		}else{
			cout << 'E' <<endl;
		}
	}
	return 0;
}
