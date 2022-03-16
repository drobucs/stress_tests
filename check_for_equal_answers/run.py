import random
import io
import os
import time

TESTS = 110       						# number of tests
FAILED = 0        						# number of faild tests
SMART = ""        						# smart answer
STUPID = "" 	  						# stupid answer
SMART_TIME = 0.0  						# time of smart solve
STUPID_TIME = 0.0 						# time of stupid solve
test_file        = 'test.txt'			# file for tests
failed_test_file = 'failed_tests.txt' 	# file for faild tests
log_file         = 'logs.txt'       	# file for logs
smart_file       = 'smart.cpp'			# file for smart solve   (.cpp)
stupid_file      = 'stupid.cpp'			# file for stupid solve  (.cpp)

#generate your test in test.txt
def gen(file):
	a = random.randint(-1, 1)
	b = random.randint(-1, 1)
	with open(file, 'w') as f:
		f.write(str(a) + " " + str(b))

#gen_somthing
def gen_parametrs():
	return ""


#logs
def log(flag, test_number, smart_t, stupid_t):
	if flag == False:
		print_log(failed_test_file, test_number, smart_t, stupid_t)		
	print_log(log_file, test_number, smart_t, stupid_t)

#print logs
def print_log(file, test_number, smart_t, stupid_t):
	global SMART, STUPID
	test = ""
	with open(test_file, "r") as f:
		test = f.read()
	with open(file, "a") as f:
		f.write("[ test_" + str(test_number) + " ]\n\n")
		f.write("test:\n\n")
		f.write(test)
		f.write("\n\nsmart: " + SMART + "\n")
		f.write("stupid: " + STUPID + "\n")
		f.write("smart time: " + str(round(smart_t, 5)) + " sec\n")
		f.write("stupid time: " + str(round(stupid_t, 5)) + " sec")
		f.write("\n-------------------------------------\n")

# checks for Smart == Stupid , logs, faild_tests
def check(test_number, smart_t, stupid_t):
	global FAILED, SMART, STUPID
	if SMART != STUPID:
		print("[    WA    ]", end = ' ')
		log(False, test_number, smart_t, stupid_t)
		FAILED += 1
	else:
		print("[    OK    ]", end = ' ')
		log(True, test_number, smart_t, stupid_t)


# run without parametrs
def run(N):
	global SMART, STUPID, SMART_TIME, STUPID_TIME
	for i in range(1, N + 1):
		gen(test_file)

		start = time.perf_counter()
		SMART = os.popen("./" + smart_file[:len(smart_file) - 4] + ".o < " + test_file).read()
		end = time.perf_counter()
		smart_t = end - start
		SMART_TIME += end - start

		start = time.perf_counter();
		STUPID = os.popen("./" + stupid_file[:len(stupid_file) - 4] + ".o < " + test_file).read()
		end = time.perf_counter()
		stupid_t = end - start
		STUPID_TIME += end - start

		check(i, smart_t, stupid_t)
		print("[  test_" + str(i) + "  ]")

# clear file
def clear(file):
	with open(file, "w") as f:
		f.write("")


clear(failed_test_file)
clear(log_file)

print("\ncompile " + stupid_file + "...")
os.popen("python3 cpl.py " + stupid_file)

print("\ncompile " + smart_file + "...")
os.popen("python3 cpl.py " + smart_file)

time.sleep(1)

print("\nstart " + str(TESTS) + " tests\n")

start = time.perf_counter()
run(TESTS)


print("-----------------------------------------------------")
print("SMART_TIME: " + str(round(SMART_TIME, 5)) + " sec")
print("STUPID_TIME: " + str(round(STUPID_TIME, 5)) + " sec")
print("TESTS: " + str(TESTS))
print("ACCEPT: " + str(TESTS - FAILED))
print("FAILED: " + str(FAILED))

