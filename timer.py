import time

def do_my_sum(xs):
	sum = 0
	for v in xs:
		sum += v
	return sum

sz = 10000000
test_data = range(sz)

t0 = time.clock()
my_result = do_my_sum(test_data)
t1 = time.clock()
print("my_result	= {0} (time taken = {1:.4f} seconds)".format(my_result, t1-t0))

t2 = time.clock()
their_result = sum(test_data)
t3 = time.clock()
print("their_result = {0} (time taken = {1:.4f} seconds)".format(their_result, t3-t2))