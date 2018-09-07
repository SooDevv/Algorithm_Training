#include <iostream>
using namespace std;

int main(){
	int n,m;
	int IsPrimeNumber(int n);
	
	cin >> n >> m;
	
	for(int i=n; i<m+1;i++){
		if(IsPrimeNumber(i)){
			cout << i <<' ';
		}
	}
	
	return 0;
}

int IsPrimeNumber(int n){
	int last = n/2; // 약수가 없는 수가 소수이므로 2부터 자기 자신/2 
	
	if(n<=1){
		return 0;
	}
	for(int i =2; i<last+1; i++){
		if(n%i ==0){
			return 0;
		}
	}
	return 1;
}
