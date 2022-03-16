#include <iostream>
#include <string>
#include <fstream>

using namespace std;


signed main(int argc, char* argv[]) {
	
	if (argc != 3) {
		cout << "\n\nchecker.cpp: need 3 args\n\n";
		return -1;
	}

	ifstream in(argv[1]);

	// input test with 'in'

	int a, b;
	in >> a >> b;

	in.close();
	in.open(argv[2]);

	// input output of solve with 'in'

	int c;
	in >> c;

	in.close();

	// check for valid answer
	// if valid   cout << "accept";
	// if invalid cout << "faild";

	if (c == a + b) {
		cout << "accept";
	} else 
		cout << "failed";


	return 0;
}