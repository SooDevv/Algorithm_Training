#include <iostream>
using namespace std;

int main(){
	int a,b;
	char cal;
	
	cin >> a >> cal >> b;
	
	if(cal == '+'){
		cout << a + b;
	}else if(cal == '-'){
		cout << a - b;
	}else if(cal == '*'){
		cout << a*b;
	}else{
		cout << a/b;
	}
	return 0;
}
