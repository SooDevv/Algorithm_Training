#include <iostream>
#include <bitset>
using namespace std;

int main(){
	int n;
	cin >> n;
	
	int result = 0; 
	for(int i=1; n>0; i*=10){
		int binary = n%2;
		result += binary*i;
		n /=2;
	}
	cout << result;
	
	return 0;
}

