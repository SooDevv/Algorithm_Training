#include <iostream>
using namespace std;

int main(){
	int arr[9];
	int min =0;
	int secondmin;
	int tmp;
	
	for(int i=0;i<9;i++){
		cin >> arr[i];
	}
	
	min = arr[0];
	secondmin = min;
	
	for(int i =1; i<9;i++){
		if(arr[i] < min){
			secondmin = min;
			tmp = i;
			min = arr[i];
		}
		else if((min<arr[i] && arr[i] < secondmin) || min ==secondmin){
			secondmin = arr[i];
			tmp = i+1;
		}
	}
	cout << secondmin << endl << tmp;
	
	
	
	return 0;
}
