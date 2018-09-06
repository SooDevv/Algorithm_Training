#include <iostream>
using namespace std;

int main(){
	int n;
	string result;
	
	cin >> n;
	
	if(n%2 == 0){
		result = "even";
	}else{
		result = "not even";
	}
	cout << result;
	return 0;
}
