#include <iostream>
using namespace std;

int main(){
	int n;
	int cnt =0;
	cin >> n;
	
	for(int i=1; i<n+1; i++){
		if(n%i == 0){
			cnt +=1;
		}
	}
	if(cnt>2){
		cout << "NO";
	}
	else{
		cout << "YES";
	}
	return 0;
}
