#include <iostream>
#include <algorithm>
using namespace std;


int main(){
	int n, reward, maxc=0, a,b,c, tmp;

	cin >> n;
	
	for(int i=0;i<n;i++){
			cin >> a >> b >> c;
	
		for(int j=0 ; j<3; j ++){
			if(a==b && b==c){
				reward = 10000+b*1000;
			}
			else if(a==b || b==c){
				reward = 1000+b*100;
			}
			
			else if(a==c){
				reward = 1000+a*100;

			}
			else {
				tmp = max(a,b);
				tmp = max(tmp,c);
				reward = tmp*100;
			}	
			if(reward > maxc){
			maxc = reward;
	}
		}
	

}
	cout << maxc;
	return 0;

}

