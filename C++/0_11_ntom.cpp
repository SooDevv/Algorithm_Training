#include <iostream>
using namespace std;

int main(){
	int n, m;
	int cnt;
	
	cin >> n >> m;
	
	for(int i=n; i<m+1; i++){
		cnt += 1;
		cout << i << " ";
		if(cnt == 8){
			cout << endl;
			cnt =0;
		}
	}
	return 0;
}
