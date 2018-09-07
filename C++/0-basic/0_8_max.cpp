#include <iostream>
using namespace std;

int main(){
	int a,b,c;
	int tmp;
	
	cin >> a >> b >> c;
	tmp = max(a,b);
	cout << max(tmp, c);
	
	return 0;
}
