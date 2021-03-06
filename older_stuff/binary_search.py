from modules.test import *
from modules.searches import *
import time

'''
xs = [2,3,5,7,11,13,17,23,29,31,37,43,47,53]
test(search_binary(xs, 20) == -1)
test(search_binary(xs, 99) == -1)
test(search_binary(xs, 1) == -1)

for (i, v) in enumerate(xs):
	test(search_binary(xs, v) == i)
'''


bigger_vocab = load_words_from_file("vocab.txt")
print("There are {0} words in the vocab, starting with\n {1} "
      .format(len(bigger_vocab), bigger_vocab[:6]))


book_words = get_words_in_book("alice_in_wonderland.txt")
print("There are {0} words in the book, the first 100 are \n{1}".
      format(len(book_words), book_words[:100]))


t0 = time.clock()
missing_words = find_unknown_words(bigger_vocab, book_words)
t1 = time.clock()
print("There are {0} unknown words.".format(len(missing_words)))
print("That took {0:.4f} seconds.".format(t1-t0))

# There are 3396 unknown words.
# Linear search took 26.6426 seconds.
# Binary search took 0.1462 seconds (without print statements).

search_binary(bigger_vocab, "magic")
