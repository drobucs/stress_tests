#include <iostream>
#include <cmath>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
#include <queue>
#include <set>
#include <bitset>
#include <cstring>

using namespace std;


#define all(x) x.begin(), x.end()

signed main(int argc, char **argv) {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);

	FILE* file = fopen(argv[1], "r");
	string str = "", f = "";
	for (int i = 0; i < strlen(argv[2]); ++i) {
		str += argv[2][i];
	}
	char buffer[4097];
	buffer[4096] = '\0';
	int n = fread(buffer, 1, 4096, file);


	while (n != 0) {
		for (int i = 0; i < n; ++i) {
			f += buffer[i];
		}
		n = fread(buffer, 1, 4096, file);
	}
	// cout << f << "\n";
	// cout << str << "\n";
	for (int i = 0; i < (int)f.size() - (int)str.size() + 1; ++i) {
		bool ok = 1;
		for (int j = 0; j < (int)str.size(); ++j) {
			if (str[j] != f[i + j]) 
				ok = 0;
		}
		if (ok) {
			cout << "Yes\n";
			fclose(file);
			return 0;
		}
	}
	cout << "No\n";
	fclose(file);
	return 0;
}