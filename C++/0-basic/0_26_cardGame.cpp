#include <iostream>
using namespace std;

int main(){
	int arr[2][10];
	int acnt = 0;
	int bcnt = 0;
	
	//입력 
	for(int i=0; i<2; i++){
		for(int j=0; j<10; j++){
			cin >> arr[i][j];
		}
	} 
	
	//비교 
	for(int j=0;j<10;j++){
		if(arr[0][j] > arr[1][j]){
			acnt +=1;
		}
		else if(arr[0][j] == arr[1][j]){
			acnt += 1;
			bcnt += 1;
		}
		else{
			bcnt += 1;
		}
	} 

	if(acnt>bcnt){
		cout << 'A';
	}else if(acnt == bcnt){
		cout << 'D';
	}else{
		cout << 'B';
	}
	return 0;
}
