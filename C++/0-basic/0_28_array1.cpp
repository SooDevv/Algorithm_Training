#include <iostream>
using namespace std;

int main(){
	int n, m;
	cin >> n >>m;
	
	for(int i=1; i<n*m+1
	 ; i++){
		cout << i <<" ";
		if(i%m==0){
			cout << endl;
		}
	}
	return 0;
}
