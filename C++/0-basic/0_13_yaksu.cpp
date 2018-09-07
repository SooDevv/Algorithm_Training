#include <iostream>
using namespace std;

int main(){
	int p, q;
	int cnt = 0;
	int result=0;
	
	cin >> p >> q;
	
	for(int i=1; i<p+1; i++){
		if(p%i == 0){
			cnt+=1;
			if(q == cnt){
				result = i;
			}
		}
	}
	
	cout << result;
	return 0;
}
