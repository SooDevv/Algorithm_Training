#include <iostream>
using namespace std;

int main(){
	
	int arr[9];
	int max =0;
	int tmp;
	
	for(int i=0;i<9;i++){
		cin >> arr[i];
		if(arr[i]>max){
			max = arr[i];
			tmp = i+1;
		}
	}
	
	cout << max << endl << tmp;
	return 0;
}
