import random
import io
import os
import time

TESTS = 100
FAILED = 0

#generate your test in test.txt
def gen():
	n = random.randint(0, 10000)
	with open('test.txt', 'w') as f:
		for i in range(0, n):
			f.write(chr(random.randint(32, 127)))

#gen_somthing
def gen_somthing():
	m = random.randint(1, 5)
	string = ""
	for i in range(0, m):
		r = random.randint(32, 127)
		if r == ord('\"') or r == ord('\'') or r == ord('`') or r == ord('\\') or r == ord('$'):
			r += 1
		string += (chr(r))
	return  "\"" + string + "\""

def check(Smart, Stupid, test_number, string):
	global FAILED
	if Smart != Stupid:
		print("[    WA    ]", end = ' ')
		s = ""
		with open("test.txt", "r") as f:
			s = f.read()
		with open("failed_tests.txt", "a") as f:
			f.write("[ test_" + str(test_number) + " ]\n\n")
			f.write(s + "\n")
			f.write("\nstring = " + string + "\n")
			f.write("\nsmart : " + Smart + "\n")
			f.write("stupid : " + Stupid + "\n")
			f.write("-------------------------------------\n")
		FAILED += 1
	else:
		print("[    OK    ]", end = ' ')
	s = ""
	with open("test.txt", "r") as f:
		s = f.read()
	with open("logs.txt", "a") as f:
		f.write("[ test_" + str(test_number) + " ]\n\n")
		f.write(s + "\n")
		f.write("\nstring = " + string + "\n")
		f.write("\nsmart : " + Smart + "\n")
		f.write("stupid : " + Stupid + "\n")
		f.write("-------------------------------------\n")



def run(N):
	for i in range(1, N + 1):
		gen()
		string = gen_somthing()
		Smart = os.popen("./smart test.txt " + string).read()
		Stupid = os.popen("./stupid test.txt " + string).read()
		check(Smart, Stupid, i, string)
		print("[  test_" + str(i) + "  ]")



with open("failed_tests.txt", "w") as f:
	f.write("")
with open("logs.txt", "w") as f:
	f.write("")

print("start\n")
#os.popen("python3 cpl.py stupid.cpp smart.cpp")
run(TESTS)
print("-----------------------------------------------------")
print("Number  of tests: " + str(TESTS))
print("ACCEPT: " + str(TESTS - FAILED))
print("FAILED: " + str(FAILED))