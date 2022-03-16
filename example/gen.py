import random
import io
import os
import time

TESTS = 100

def gen():
	a = random.randint(0, 10)
	b = random.randint(0, 10)
	with open('test.txt', 'w') as f:
		f.write(str(a) + " " + str(b) + '\n')

def check():
	ans = os.popen("./checker test.txt outSmart.txt").read()
	print(ans, end = ' ')
	if ans == "failed":
		print("WA")
		exit(0)

def run(cnt):
	for i in range(0, cnt):
		print("test " + str(i + 1) + " -----> ", end = ' ')
		gen()
		Smart = os.popen("./smart < test.txt").read()
		with open('outSmart.txt', 'w') as f:
			f.write(Smart)
		check()
		print("OK")
		
run(TESTS)









# def run(cnt):
# 	for i in range(0, cnt):
# 		print("test " + str(i + 1) + " -----> ", end = ' ')
# 		gen()
# 		Smart = os.popen("./smart < test.txt").read()
# 		Stupid = os.popen("./stupid < test.txt").read()
# 		with open('outSmart.txt', 'w') as f:
# 			f.write(Smart)
# 		with open('outStupid.txt', 'w') as f:
# 			f.write(Stupid)
# 		check(Smart, Stupid)
# 		print("OK")