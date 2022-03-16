import os, sys

a = sys.argv

for i in range(1, len(a)):
	s = str(a[i])
	os.popen("g++ " + s + " -o " + s[:len(s) - 4])
