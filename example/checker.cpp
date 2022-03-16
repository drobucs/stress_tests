#include <iostream>
#include <string>
using namespace std;

signed main(int argc, char* argv[]) {
	
	if (argc == 1) {
		cout << "<--------No args------->\n";
		return 0;
	}

	string s1 = string(argv[1]);
	string s2 = string(argv[2]);

	freopen(argv[1], "r", stdin);

	int a, b;
	cin >> a >> b;

	freopen(argv[2], "r", stdin);
	int c;
	cin >> c;

	if (a * b == c) {
		cout << "accept";
	} else 
		cout << "failed";


	return 0;
}