#include <iostream>
using namespace std;

int main(){
	int n,m, a,b;
	cin >>n >>m;
	int arr[n][m];
	
	
	for(int i=0; i <n; i++){
		for(int j=0; j<m; j++){
			cin >> arr[i][j];
		}
	}
	
	cin >> a >> b;
	
	cout << arr[a][b];
	
	return 0;
}
