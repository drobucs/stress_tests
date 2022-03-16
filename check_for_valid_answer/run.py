import random
import io
import os
import time

TESTS = 100    							# number of tests
FAILED = 0         						# number of faild tests
ANSWER = ""        						# answer
TIME = 0.0         						# time of solve
test_file        = 'test.txt'			# file for tests
failed_test_file = 'failed_tests.txt' 	# file for faild tests
log_file         = 'logs.txt'       	# file for logs
solve_out 		 = 'out_solve.txt'  	# out of solve
solve_file       = 'solve.cpp'			# file for solve   (.cpp)
checker_file     = 'checker.cpp'    	# file for checker (.cpp)


#generate your test in test.txt
def gen(file):
	a = random.randint(-1, 1)
	b = random.randint(-1, 1)
	with open(file, 'w') as f:
		f.write(str(a) + " " + str(b))

#gen_somthing
def gen_parametrs():
	return ""

# logs
def log(flag, test_number, time):
	if flag == False:
		print_log(failed_test_file, test_number, time)
	print_log(log_file, test_number, time)

#print logs
def print_log(file, test_number, time):
	global ANSWER
	test = ""
	with open(test_file, "r") as f:
		test = f.read()
	with open(file, "a") as f:
		f.write("[ test_" + str(test_number) + " ]\n\n")
		f.write("test:\n\n")
		f.write(test)
		f.write("\n\nanswer:\n" + ANSWER + "\n")
		f.write("\ntime: " + str(round(time, 5)) + " sec")
		f.write("\n-------------------------------------\n")

# checks for Smart == Stupid , logs, faild_tests
def check(test_number, time):
	global FAILED
	res = os.popen("./" + checker_file[:len(checker_file) - 4] + " " + test_file + " " + solve_out).read()
	if res == "failed":
		print("[    WA    ]", end = ' ')
		log(False, test_number, time)
		FAILED += 1
	else:
		print("[    OK    ]", end = ' ')
		log(True, test_number, time)

# write answer to out_solve.txt
def writeAnswers(answer):
	with open(solve_out, "w") as f:
		f.write(answer)

# run without parametrs
def run(N):
	global ANSWER, TIME
	for i in range(1, N + 1):
		gen(test_file)
		start = time.perf_counter();
		ANSWER = os.popen("./" + solve_file[:len(solve_file) - 4] + " < " + test_file).read()
		end = time.perf_counter()
		TIME += end - start;
		writeAnswers(ANSWER)
		check(i, end - start)
		print("[  test_" + str(i) + "  ]")


# clear file
def clear(file):
	with open(file, "w") as f:
		f.write("")


clear(failed_test_file)
clear(log_file)


print("\ncompile " + solve_file + "...")
os.popen("python3 cpl.py " + solve_file)

print("\ncompile " + checker_file + "...")
os.popen("python3 cpl.py " + checker_file)

time.sleep(1)

print("\nstart " + str(TESTS) + " tests\n")

run(TESTS)


print("-----------------------------------------------------")
print("TIME: " + str(round(TIME, 5)) + " sec")
print("TESTS: " + str(TESTS))
print("ACCEPT: " + str(TESTS - FAILED))
print("FAILED: " + str(FAILED))
