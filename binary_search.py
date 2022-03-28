import math
import random 
import time

# this project proves that binary search is faster than naive search
# first naive search
def naive_search(arr, target):
	for i in range(len(arr)):
		if arr[i] == target:
			return i

	return -1

# then binary search
def binary_search(arr, target):
	low = 0
	high = len(arr) - 1

	while low <= high:
		middle = math.floor((high + low) / 2)
		guess = arr[middle]

		if guess == target:
			return middle
		elif guess < target:
			low = middle + 1
		else:
			high = middle - 1

	return -1


if __name__ == '__main__':
	# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	target = 1000

	# let's do some time analysis 
	length = 1000
	# intialize a random sorted list of 1000 items 
	sorted_list = set()

	while len(sorted_list) < length:
		sorted_list.add(random.randint(-3*len(sorted_list), 3*len(sorted_list)))
	
	#finally let's convert that set into a sorted list
	sorted_list = sorted(list(sorted_list)) 

	# for naive search
	naive_search_start = time.time()
	naive_serach_result = naive_search(sorted_list, target)
	naive_search_end = time.time()

	# for binary search
	binary_search_start = time.time()
	binary_search_result = binary_search(sorted_list, target)
	binary_search_end = time.time()

	print(f'Binary search resutl: {binary_search_result} and it took {binary_search_end - binary_search_start}')
	print(f'naive search result: {naive_serach_result} and it took {naive_search_end - naive_search_start}')
