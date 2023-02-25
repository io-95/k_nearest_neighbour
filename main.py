import csv
import math

line_test = 0
line_data = 0

def main():
	data = []
	readfile(data)
	normalization(data)
	
	#devide data in test and data
	test = []
	test.extend(data[-line_test:])
	data = data[:len(data) - line_test]
	k_nearest_neighbour(data, test)

	
def readfile(array):
	global line_test
	global line_data

	#read data from file
	with open('app1.data', newline='') as csvfile:
		reader = csv.reader(csvfile, delimiter=',')
		for row in reader:
			array.append([float(num) for num in row])

	line_data = len(array)

	#read test data from file
	with open('app1.test', newline='') as csvfile:
		reader = csv.reader(csvfile, delimiter=',')
		for row in reader:
			array.append([float(num) for num in row])

	line_test = len(array) - line_data

def normalization(array):
	for i in range(len(array[0])):
		min = math.inf
		max = -1
		for j in range(len(array)):
			if array[j][i] > max:
				max = array[j][i]
			if array[j][i] < min:
				min = array[j][i]
		
		for j in range(len(array)):
			array[j][i] = (array[j][i] - min) / (max - min) 

def k_nearest_neighbour(data, test):
	correct = 0
	false = 0
	
	for i in range(len(test)):
		dist_list = []
		for j in range(len(data)):
			dist_list.append([
				manhatten_distance(data[j], test[i]),
				data[j][15]
				])
		dist_list.sort()
		if dist_list[0][1] == test[i][15]:
			correct += 1
		else:
			false += 1

	print("correct: ", correct)
	print("false: ", false)

def manhatten_distance(pointA, pointB):
	dist = 0
	for i in range(len(pointA) - 1):
		sum = pointA[i] - pointB[i]
		sum = abs(sum)
		dist += sum

if __name__ == '__main__':
	main()
