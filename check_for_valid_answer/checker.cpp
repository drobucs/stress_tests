#include <iostream>
#include <string>
using namespace std;

signed main(int argc, char* argv[]) {
	
	if (argc == 1) {
		cout << "!!!____No args____!!!\n";
		return 0;
	}

	// вводим тест
	freopen(argv[1], "r", stdin);

	int a, b;
	cin >> a >> b;


	// вводим output решения
	freopen(argv[2], "r", stdin);
	int c;
	cin >> c;


	// проверяем на валидность
	if (a * b == c) {
		cout << "accept";
	} else 
		cout << "failed";


	return 0;
}