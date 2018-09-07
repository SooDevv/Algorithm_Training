#include <iostream>
#include <algorithm>
using namespace std;

int main(){
	int arr[10];
	int sum =0; 
	
	for(int i=0; i<10; i++){
		cin >> arr[i];
		sum += arr[i];
	}
	sort(arr, arr+10);
	
	//ÃÖºó°ª mode
	int tmp = arr[0];
	int mode = tmp;
	int cnt = 1;
	int freq = 1;
	
	for(int i=1;i<10;i++){
		if(tmp == arr[i]){
			cnt +=1;
			if(cnt > freq){
				mode = arr[i];
				freq = cnt;
			}
		}
		else if(tmp != arr[i]){
			tmp = arr[i];
			cnt = 1;	
		}
		
	}
	cout << sum/10 <<endl << mode;
	 
	return 0;
}
