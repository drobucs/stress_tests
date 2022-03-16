import random
import io
import os
import time

TESTS = 100
FAILED = 0 

def gen():
	#generate your test in test.txt
	a = random.randint(0, 10)
	b = random.randint(0, 10)
	with open('test.txt', 'w') as f:
		f.write(str(a) + " " + str(b) + '\n')

def check(cnt):
	global FAILED
	res = os.popen("./checker test.txt out_solve.txt").read()
	if res == "accept":
		print("[    OK    ]", end = ' ')
	elif res == "failed":
		print("[    WA    ]", end = ' ')
		s = ""
		with open("test.txt", "r") as f:
			s = f.read()
		with open("failed_tests.txt", "a") as f:
			f.write("[ test_" + str(cnt) + " ]\n")
			f.write(s + "\n")
			f.write("--------------------------------------------\n")
		FAILED += 1
	print("[    test_" + str(cnt) + "    ]")


def writeAnswers(answer):
	with open("out_solve.txt", "w") as f:
		f.write(answer)

def run(cnt):
	for i in range(1, cnt + 1):
		gen()
		answer = os.popen("./solve < test.txt").read()
		writeAnswers(answer)
		check(i)


with open("failed_tests.txt", "w") as f:
	f.write("")

run(TESTS)
print("-----------------------------------------------------")
print("Number  of tests: " + str(TESTS))
print("ACCEPT: " + str(TESTS - FAILED))
print("FAILED: " + str(FAILED))
