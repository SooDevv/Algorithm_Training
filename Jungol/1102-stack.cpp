//1102: 스택 
#include <iostream>
using namespace std;

int main(){
	int num	= 0;
	int order = 0;
	char ch =0;
		 
	cin >> order;
	
	int *arr = new int[order]; // 스택

	for(int i=0; i<order; i++){
		cin >> ch;
		switch(ch)
		{
			case 'i':
				cin >> arr[num];
				num++;
				break;
			case 'o':
				num--;
				if(num <0)
				{
					num =0;
					cout << "empth" << '\n';
					arr[num] = 0;
					break;
				}
			case 'c':
				cout << num << '\n';
				break;
			default:
				cout << "order error" << '\n';
				break;
		}
	} 
	delete[] arr;
	return 0;
}
