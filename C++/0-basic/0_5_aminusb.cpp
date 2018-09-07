#include <iostream>
using namespace std;

int main(){
	int a, b;
	int result;
	
	cin >> a >> b;
	
	if(a-b <0){
		result = -1;
	}
	else{
		result = a - b;
	}
	cout << result;
	return 0;
}
